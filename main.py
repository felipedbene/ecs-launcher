import boto3,json

def lambda_handler(event, context):
    
    client = boto3.client('ecs')
    
    response = client.run_task(cluster='Cluster2',
    count=1,
    launchType='FARGATE',
    networkConfiguration={
        'awsvpcConfiguration': {
            'subnets': [
                'subnet-029a18f689525931d',
            ],
            'securityGroups': [
                'sg-0f746e3d4195f1ae7'
            ],
            'assignPublicIp': 'ENABLED'
        }
    },
    taskDefinition='Zip:2'
        
        )
    return {
        'statusCode': 200,
        'body': str(response)
    }