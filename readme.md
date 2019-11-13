serverless-vpc-scan
===================

Check the expiry date of your HTTPS certificates in your VPC by the use of a VPC connected Lambda functions. The function scans all available IP addresses on port 443 and reports back the certificate expiry date per IP. 

This is a very early POC which needs a lot more polishing to run reliably - please handle with care and do not use for production usecases yet! Based on initial tests, a 3GB Lambda function can check and scan a /16 range in less than 90 seconds. Further testing is needed to test the reliability and accuracy of the data. 

The to-do items for the project - please feel free to share suggestions

- [ ] Add VPC CIDR range discovery so that the user does not need to instrument this (most likely by running a describe call to discover CIDR's).
- [ ] Add SNS notification once the scan has completed to share results over email.
- [ ] Add filtering possibilities regarding certificate expiry notifications (i.e. only alert if the certificate expires in < 10 days).
- [ ] Optimize the Lambda size and socket timeout values to run as reliably as possible. 
- [ ] Add more meaningfull information to the hosts (i.e. hostname, alternative certificate names, key strength, whether its a wildcart certificate, etc)
- [ ] Store the results permanently in S3 or DynamoDB for auditing purposes.
- [ ] Add all the neccesary libraries in Lambda Layers so that deployment becomes easier and more repeatable. 
- [ ] Publish the solution in the AWS Serverless Application Repository.  
- [ ] Add more meaningful code comments and cleanup code. 
- [ ] Add the option to add the Lambda into a VPC with the correct SG's set up. 