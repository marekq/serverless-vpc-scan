#!/usr/bin/python
# @marekq
# www.marek.rocks

import os, queue, socket, threading
from ipaddress import *
from OpenSSL import SSL
from ssl import PROTOCOL_TLSv1
from datetime import datetime

# create a list for storing results and a queue
res     = []
err     = []
q1      = queue.Queue()

# worker for queue jobs
def worker():
    while not q1.empty():
        job(q1.get())
        q1.task_done()

def check_subnet():
    cidr   = os.environ['subnet']
    
    ips    = list(ip_network(cidr).hosts())
    for x in ips:
	    q1.put(str(x))

def job(ip):
    # try to retrieve the certificate by connecting to the host
    try:
        x   = get_cert(ip, '443')
        print(x)

    # if the connection fails or times out, keep on going
    except Exception as e:
        err.append(ip)
        #print('ERROR: IP '+str(ip)+'   '+str(e))
    
# get the certificate
def get_cert(host, port):
    # open the socket with a timeout of 5
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    # set the protocol to TLSv1 and remove the timeout
    osobj = SSL.Context(PROTOCOL_TLSv1)
    sock.connect((host, int(port)))
    sock.settimeout(None)

    # set up the actual connection
    oscon = SSL.Connection(osobj, sock)
    oscon.set_tlsext_host_name(host.encode())
    oscon.set_connect_state()
    oscon.do_handshake()
    
    # retrieve the certificate
    cert = oscon.get_peer_certificate()
    sock.close()
    
    # get cert valid from date
    valid_from = datetime.strptime(cert.get_notBefore().decode('ascii'), '%Y%m%d%H%M%SZ')
    vfrom = valid_from.strftime('%Y-%m-%d')

    # get cert valid till date
    valid_till = datetime.strptime(cert.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')
    vtill = valid_till.strftime('%Y-%m-%d')

    # get datetime timestamp
    now = datetime.now()
    date_time = now.strftime('%Y-%m-%d')
    
    # get cert validity days
    vdays = (valid_till - now).days

    # get some additional properties of the cert
    vcou = cert.get_issuer().countryName
    vorg = cert.get_issuer().organizationName
    vou  = cert.get_issuer().organizationalUnitName
    viss = cert.get_issuer().commonName

    # print the expiry date in human readible format
    x   = str(host)+' - '+str(vdays)+' days until certificate expiry on '+vtill+' for '+viss
    res.append(x)
    return x

    # TODO - publish the message to SNS if the functions has a NAT GW or VPC endpoint, or call to different Lambda function
    #sns.publish(TopicArn = 'arn:aws:sns:eu-west-1:123:abc', Message = x)

# the lambda handler
def handler(event, context):
    # get all the ip addresses for the CIDR (the default is 172.16.0.0/16) and submit them to a local queue.
    check_subnet()

    # launch 100 threads and start scanning the hosts.
    for x in range(1000):
        t = threading.Thread(target = worker)
        t.daemon = True
        t.start()
    q1.join()

    print(str(len(res))+' results')
    print(str(len(err))+' errors')