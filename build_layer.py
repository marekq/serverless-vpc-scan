#!/usr/bin/python
# @marekq
# www.marek.rocks

import boto3, os, subprocess, sys, time
lambd   = boto3.client('lambda')

# make a temporary workdir in /tmp
dirn    = '/tmp/'+str(int(time.time()))+'/'

# set a directory for the python files
dirp    = dirn+'python/'

# set a path for the temporary layer zip 
dirl    = dirn+'layer.zip'

# set a path for the layer zip destination
dirg    = "/Users/marek/Documents/GitHub/serverless-vpc-scan/layer"

print('creating '+dirp)
os.makedirs(dirp)

# read requirements file
fn  = open('./requirements.txt').read().split('\n')
for lib in fn:
    print("downloading "+lib+" into "+dirn)
    subprocess.call(["python3", "-m", "pip", "install", lib, "-t", dirp, "--upgrade"])

# create a zip file with the layer
os.chdir(dirn)
subprocess.call(["zip", "-r9", dirl, "./python"])
subprocess.call(["cp", dirl, "/tmp/layer.zip"])
subprocess.call(["cp", dirl, dirg])

print("created layer zip in "+dirn+" and "+dirl)