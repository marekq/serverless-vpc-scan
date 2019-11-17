FROM amazonlinux:latest
RUN yum update --downloadonly -y && yum install python3-pip zip -y

RUN mkdir -p /tmp/a/python/ && mkdir /tmp/layer/ && cd /tmp/a/
RUN pip3 install pyOpenSSL sslyze ipaddress -t python

RUN zip -r9 /tmp/layer/layer.zip python/
RUN echo 'wrote zip file, exiting...'
