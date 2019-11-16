#!/usr/bin/python
# @marekq
# www.marek.rocks

import boto3, os, shutil, subprocess, sys, time
lambd   = boto3.client('lambda')

# make a temporary workdir in /tmp
dirn    = '/tmp/'+str(int(time.time()))+'/'

# set a directory for the python files
dirp    = dirn+'python/'

# set a path for the temporary layer zip 
dirl    = dirn+'layer.zip'

# set a path for the layer zip destination
dirg    = os.getcwd()+"/layer"

# creating python dir in '/tmp'
print('creating '+dirp)
os.makedirs(dirp)

# read requirements file
fn  = open('./requirements.txt').read().split('\n')
for lib in fn:
    print("downloading "+lib+" into "+dirn)
    subprocess.call(["python3", "-m", "pip", "install", lib, "-t", dirp, "--upgrade"])

# create a zip file with the layer
os.chdir(dirn)

# zip the contents of the pip folders
subprocess.call(["zip", "-r9", dirl, "./python"])

# copy zip for debug to '/tmp'
subprocess.call(["cp", dirl, "/tmp/layer.zip"])

# delete the local layer dir
shutil.rmtree(dirg) 

# creating the local dir again
os.makedirs(dirg)

# copy zip to the local layer dir
subprocess.call(["cp", dirl, dirg])
print("created layer zip in "+dirn+" and "+dirl)

# unzip the zip in the local layer dir
os.chdir(dirg)
subprocess.call(["unzip", "layer.zip"])
print("unzipped zip file in "+dirg)

# cleanup /tmp files
os.remove(dirg+"/layer.zip")
shutil.rmtree(dirn) 
print("deleted "+dirn)

print("DONE")