import boto3
import botocore
# import cfnresponse
session = boto3.Session(profile_name='development')
east = 'us-east-1'
west = 'us-west-2'
route53 = session.client('route53', east)
response = route53.list_hosted_zones()
f=response['HostedZones']