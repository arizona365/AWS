import boto3, json
session = boto3.Session(profile_name='development')
east = 'us-east-1'
west = 'us-west-2'
ec2East = session.client('ec2', region_name = east)

ec2West = session.client('ec2', region_name = west)

def helloworld():
    hello = ec2East.describe_instances()
    
    a = hello["Reservations"]

    print(a)

helloworld()




