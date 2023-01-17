# make a program that make a insert in dynamoDB table
# using boto3 lib
import boto3
import json

# create a dynamodb client
dynamodb = boto3.client('dynamodb')

# create a table
dynamodb.create_table(
    TableName='Movies',
    KeySchema=[
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# insert a item in the table
response = dynamodb.put_item(
    TableName='Movies',
    Item={
        'year': {'N': '2015'},
        'title': {'S': 'The Big New Movie'},
        'info': {
            'M': {
                'plot': {'S': 'Nothing happens at all.'},
                'rating': {'N': '0'}
            }
        }
    }
)

# get the item from the table
response = dynamodb.get_item(
    TableName='Movies',
    Key={
        'year': {'N': '2015'},
        'title': {'S': 'The Big New Movie'}
    }
)

item = response
print(item)