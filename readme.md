serverless-vpc-scan
===================

Automatically check the expiry date of your HTTPS certificates in your VPC by the use of a VPC connected Lambda functions and report back the results to an SNS topic. The Lambda function scans all available IP addresses on port 443 and reports back the certificate expiry date per IP. In the future, the function will be expanded to provide more scanning and CMDB like functionality.

Note; this is a very early POC which needs a lot more polishing to run reliably - please handle with care and do not use for production usecases yet! Based on initial testing, a 3GB Lambda function can check and scan a /16 range in less than 90 seconds which does make it very feasible to run these kinds of scans across large environments. However further testing is needed to test the reliability and accuracy of the data.  


Installation
------------

Make sure you have the AWS and SAM CLI's preconfigured on your machine together with 'python3' and 'python3-pip'. You also need to have the 'docker' command installed which is used to retrieve the Python libraries into a Lambda Layer. The Dockerfile for the container can be found in the 'docker/' directory.

Next, clone the Git repository to your local machine and run 'bash deploy.sh' to assemble the Lambda Layer and deploy the CloudFormation stack to your account. Once the stack has completed deploying, add the Lambda function to your VPC and ensure the environment variable contains the correct subnet for asset discovery.

On longer term, the app will be deployable automatically through the Serverless Application Repository which will be significantly easier. 


TODO items
----------

- [ ] Add VPC CIDR range discovery so that the user does not need to instrument this (most likely by running a describe call to discover CIDR's or something similar).
- [ ] Add SNS notification once the scan has completed, so you can share results to an email address easily.
- [ ] Add discovery of other undesirable certificate properties (i.e. contains a wildcard, weak cipher, CA root, creation date, etc).
- [ ] Add filtering possibilities regarding certificate expiry notifications (i.e. only alert if the certificate expires in < 10 days or has a weak cipher).
- [ ] Store the scan results permanently in S3 or DynamoDB for long(er) term auditing purposes.
- [ ] Submit the results of scans as findings to Security Hub in a meaningful way. 
- [ ] Publish the solution in the AWS Serverless Application Repository.  
- [ ] Add the option to add the Lambda into a VPC with the correct SG's set up by default. 
- [X] Add all the neccesary libraries in Lambda Layers so that deployment becomes easier and more repeatable.
- [X] Optimize the Lambda size and socket timeout values to run as reliably as possible. 
- [X] Add more meaningfull information to the hosts (i.e. hostname, alternative certificate names, key strength, whether its a wildcart certificate, etc).


Contact
-------

In case you have any suggestions, questions or remarks, pleae raise an issue or reach out to @marekq.