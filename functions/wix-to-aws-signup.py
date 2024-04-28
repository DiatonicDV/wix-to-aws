#lambda to turn off ec2 instance
import boto3
import json
import os
import logging

logging.basicConfig(level=logging.INFO)
# Set up AWS Cognito client
cognito = boto3.client('cognito-idp', region_name=os.getenv('REGION'))  
dynamodb = boto3.resource('dynamodb', region_name=os.getenv('REGION'))
table = dynamodb.Table(os.getenv('DYNAMODB_TABLE'))


def signup_zapier_user(username, password, name, surname, email):
    """
    Sign up a new user in AWS Cognito.
    Uses event data from Zapier to create a new user.
    Returns the user's UserSub.
    """
    try:
        #check if user already exists
        #TODO

        #add user to Cognito
        response = cognito.sign_up(
            ClientId=os.getenv('COGNITO_APP_CLIENT_ID'),
            Username=username,
            Password=password,
            UserAttributes=[
                {'Name': 'email', 'Value': email},
                {'Name': 'given_name', 'Value': name},
                {'Name': 'family_name', 'Value': surname}
            ]
        )
        # User signup successful
        return response['UserSub']

    except Exception as e:
        print(f"User signup failed: {e}")

def signup_wix_user(username, password, name, surname, email):
    """
    Sign up a new user in AWS Cognito.
    Uses event data from Wix webook to create a new user.
    Returns the user's UserSub.
    """
    try:

         #check if user already exists
        #TODO

        #add to Cognito
        # response = cognito.sign_up(
        #     ClientId=os.getenv('COGNITO_APP_CLIENT_ID'),
        #     Username=username,
        #     Password=password,
        #     UserAttributes=[
        #         {'Name': 'email', 'Value': email},
        #         {'Name': 'given_name', 'Value': name},
        #         {'Name': 'family_name', 'Value': surname}
        #     ]
        # )
        
        #add to DynamoDB table
        key = {
                'email': email,
                # 'given_name': name,
                # 'family_name': surname
              }
        if table.get_item(Key=key):
            print("user exists")
            #user exists
            table.update_item(
                Key=key,
                UpdateExpression="set tier = :u",
                ExpressionAttributeValues={
                    ':u': "free"
                }
            )
        else:
            #add user
            print("adding user")
            table.put_item(Item=key)
        
        # User signup successful
        # return response['UserSub']
        return "success"

    except Exception as e:
        print(f"User signup failed: {e}")

def lambda_handler(event, context):

    print(event)
    data = json.loads(event.replace("\\"," "))['data']
    
    # Example usage
    # username = event.username #FIXME: add to zap
    # password = event.password #FIXME: add to zap
    # email = event.email
    # name =event.name
    # surname = event.surname
    username = "test"
    password = "XXXX"
    name = "test"
    surname = "test"
    email = json.loads(data['body'].replace("\\"," "))['data']['contact']['email'] 
    user_sub = signup_wix_user(username, password, name, surname, email)

    print(f"User successfully signed up. UserSub: {user_sub}")
        
    return {
        'statusCode': 200,
        'body': json.dumps('EC2 instance stopped!')
    }
