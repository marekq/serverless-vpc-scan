#!/bin/bash
# @marekq
# www.marek.rocks

RED='\033[0;31m'
NC='\033[0m'

echo -e "\n${RED} * Building the Lambda layer... ${NC}\n"
python3 build_layer.py

echo -e "\n${RED} * Running SAM validate locally to test function... ${NC}\n"
sam validate

echo -e "\n${RED} * Packaging the artifacts to S3 and preparing SAM template... ${NC}\n"
sam package --template-file template.yaml --output-template-file packaged.yaml --s3-bucket marek-temp

echo -e "\n${RED} * Deploying the SAM stack to AWS... ${NC}\n"
sam deploy --template-file ./packaged.yaml --stack-name vpcscan --capabilities CAPABILITY_IAM
