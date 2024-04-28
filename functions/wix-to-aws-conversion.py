#lambda to turn off ec2 instance
import boto3
import json
import os
import logging

logging.basicConfig(level=logging.INFO)
# Set up AWS Cognito client
client = boto3.client('cognito-idp', region_name=os.getenv('REGION'))  



def signup_zapier_user(username, password, name, surname, email):
    """
    Sign up a new user in AWS Cognito.
    Uses event data from Zapier to create a new user.
    Returns the user's UserSub.
    """
    try:
        response = client.sign_up(
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

def signup_user(username, password, name, surname, email):
    """
    Sign up a new user in AWS Cognito.
    Uses event data from Wix webook to create a new user.
    Returns the user's UserSub.
    """
    try:
        response = client.sign_up(
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

def lambda_handler(event, context):

    print(event)
    
    # Example usage
    # username = event.username #FIXME: add to zap
    # password = event.password #FIXME: add to zap
    # email = event.email
    # name =event.name
    # surname = event.surname
    # user_sub = signup_user(username, password, name, surname, email)

    # print(f"User successfully signed up. UserSub: {user_sub}")
        
    return {
        'statusCode': 200,
        'body': json.dumps('EC2 instance stopped!')
    }
