import json
import boto3


def lambda_handler(event, context):
    if not event['body-json']['scheduled']:
        scheduled_bool = event['body-json']['scheduled']
        return {
            'statusCode': 200,
            'scheduled': scheduled_bool,
            'message': "Scheduled Trigger Set to False, Enable it to use this api",
        }
        
    if event['body-json']['start_instance']:
        s = start_instances_1(event)
        scheduled_bool = event['body-json']['scheduled']
        return {
            'statusCode': 200,
            'scheduled': scheduled_bool,
            'message': "Started instance",
            'headers': {'Content-Type': 'application/json'},
            'body': s
        }

    if event['body-json']['stop_instance']:
        s = stop_instances_1(event)
        scheduled_bool = event['body-json']['scheduled']
        return {
            'statusCode': 200,
            'scheduled': scheduled_bool,
            'message': "Stopped instance",
            'headers': {'Content-Type': 'application/json'},
            'body': s
        }


def start_instances_1(event):
    lis = list()
    ec2 = boto3.resource('ec2')
    for instance_json in event['body-json']['instances']:
        res = ec2.Instance(instance_json).start()
        lis.append(res)
    return(lis)

def stop_instances_1(event):
    lis = []
    ec2 = boto3.resource('ec2')
    for instance_json in event['body-json']['instances']:
        res = ec2.Instance(instance_json).stop()
        lis.append(res)
    return(lis)
