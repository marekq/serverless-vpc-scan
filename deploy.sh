#!/bin/bash
# @marekq
# www.marek.rocks


bucketn='marek-temp'           # CHANGE THIS TO YOUR BUCKET NAME

#####

RED='\033[0;31m'
NC='\033[0m'

echo -e "\n${RED} * Downloading the Lambda Layer in an Amazon Linux 2 Docker container. Building Docker container first...${NC}\n"
docker rm al2
docker build ./docker/ -t al2

path1=`pwd`/layer
echo -e "\n${RED} * Downloading the Lambda Layer in an Amazon Linux 2 container. Building Docker container first...${NC}\n"
docker run -d --name al2 al2
docker cp al2:/tmp/layer/layer.zip $path1

echo -e "\n${RED} * Unzipping the Lambda layer... ${NC}\n"
python3 unzip_layer.py

echo -e "\n${RED} * Running SAM validate locally to test function... ${NC}\n"
sam validate

echo -e "\n${RED} * Packaging the artifacts to S3 and preparing SAM template... ${NC}\n"
sam package --template-file template.yaml --output-template-file packaged.yaml --s3-bucket $bucketn

echo -e "\n${RED} * Deploying the SAM stack to AWS... ${NC}\n"
sam deploy --template-file ./packaged.yaml --stack-name vpcscan --capabilities CAPABILITY_IAM
