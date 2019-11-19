FROM amazonlinux:latest
RUN yum update --downloadonly -y && yum install python3-pip zip -y && yum clean all && rm -rf /var/cache/yum
RUN mkdir -p /tmp/a/python/ && mkdir /tmp/layer/ && cd /tmp/a/
RUN pip3 install -r https://raw.githubusercontent.com/marekq/serverless-vpc-scan/master/requirements.txt -t python/
RUN zip -r9 /tmp/layer/layer.zip python/ && echo 'wrote zip file, exiting...'
