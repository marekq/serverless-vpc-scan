#!/usr/bin/python
# @marekq
# www.marek.rocks

import os, shutil, subprocess, sys

# set a path for the layer zip destination
dirg    = os.getcwd()+"/layer/"
dirp    = dirg+"python/"

# unzip the zip in the local layer dir
os.chdir(dirg)
shutil.rmtree(dirp) 
subprocess.call(["unzip", "layer.zip"])
print("unzipped zip file in "+dirg)

# cleanup /tmp files
os.remove(dirg+"/layer.zip")
print("DONE")
