#lambda provide information about new user that subscribe a payment plan on Wix to DynamoDB or Cognito

import boto3
import json
import os
import logging

logging.basicConfig(level=logging.INFO)
cognito_client = boto3.client('cognito-idp', region_name=os.getenv('REGION'))
dynamodb_client = boto3.client('dynamodb', region_name=os.getenv('REGION'))
table = dynamodb_client.Table(os.getenv('DYNAMODB_TABLE'))

def signup_cognito_user(poolId, group, email, password, first_name, last_name, phone, prefix, birthdate, address):
    """
    Sign up a new user in AWS Cognito.
    Uses event data from Wix webook to create a new user.
    Returns the user's UserSub.
    """
    try:
        response = cognito_client.admin_create_user(
                UserPoolId=poolId,
                Username=email,
                TemporaryPassword= password,
                UserAttributes=[{"Name": "email","Value": email},  #see them here: https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html
                                {"Name": "email_verified", "Value": "true"},
                                {"Name": "family_name", "Value": first_name},
                                {"Name": "name", "Value": last_name},
                                {"Name": "phone_number", "Value": prefix+phone},
                                {"Name": "birthdate", "Value": birthdate},
                                {"Name": "address", "Value": address}
                ]
            )
        reply = client.admin_add_user_to_group( UserPoolId=poolId, Username=email, GroupName=group )

    except Exception as e:
        print(f"User signup failed: {e}")

def add_to_dynamodb(email, tier):
    '''
    Update the tier of the recently added user.
    ''' 
    key = {"email": email}
    update_expression = "SET tier = :new_value"
    expression_values = {":new_value": tier}
    
    try:
        response = table.update_item(
            Key=key,
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_values,
        )
        print("Item updated successfully:", response)
    except Exception as e:
        print("Error updating item:", e)
    
def lambda_handler(event, context):

    first_name = json.loads(event['body'].replace("\\"," "))['data']['contact']['name']['first']
    last_name = json.loads(event['body'].replace("\\"," "))['data']['contact']['name']['last']
    phone = json.loads(event['body'].replace("\\"," "))['data']['contact']['phones'][0]['phone']
    address = json.loads(event['body'].replace("\\"," "))['data']['contact']['address']['addressLine']
    email = json.loads(event['body'].replace("\\"," "))['data']['contact']['email']
    tier = json.loads(event['body'].replace("\\"," "))['data']['plan_title']

    add_to_dynamodb(email, tier)
    signup_cognito_user(os.getenv('COGNITO_POOL_ID'), os.getenv('COGNITO_GROUP'), email, os.getenv('COGNITO_PASSWORD'), first_name, last_name, phone, os.getenv('PHONE_PREFIX'), "01/01/1999", address)
        
    return {
        'statusCode': 200,
        'body': json.dumps('User added!')
    }
