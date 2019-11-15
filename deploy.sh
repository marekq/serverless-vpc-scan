sam package --template-file template.yaml --output-template-file packaged.yaml --s3-bucket marek-temp
sam deploy --template-file ./packaged.yaml --stack-name vpcscan1 --capabilities CAPABILITY_IAM
