import boto3

c = boto3.client('ec2')

def handler(event, context):
	x = c.describe_network_interfaces()

	print(x)

