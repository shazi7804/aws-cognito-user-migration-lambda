from authlib.integrations.requests_client import OAuth2Session
from os import getenv

# # OAuth
# client_id = 'adSzJDQbu3WSZiV1ZpCisoZw'
client_id = getenv('clientId')
client_secret = getenv('clientSecret')
scope = getenv('scope')
token_endpoint = getenv('tokenEndpoint')
profile_endpoint = getenv('profileEndpoint')
# client_secret = 'ILfC0utk2SGU6fZ6ygFiKT2Io7NNAGrQnMInu0dPecPJy0jq'
# scope = 'profile'

# token_endpoint = 'http://ec2-34-217-20-189.us-west-2.compute.amazonaws.com/oauth/token'

# # Resource
# profile_endpoint = 'http://ec2-34-217-20-189.us-west-2.compute.amazonaws.com/api/user'

def authenticateUser(username):

    # OAuth2 client_credentials grant type
    client = OAuth2Session(client_id, client_secret, scope=scope, token_endpoint_auth_method='client_secret_basic')
    token = client.fetch_token(token_endpoint, grant_type='client_credentials')

    # Get user_profile from resource server
    profile = client.get(profile_endpoint).json()

    status = ''
    if username in profile['email']:
        status = 'true'

    print(status)

    return status

def lambda_handler(event, context):

    if ( event['triggerSource'] == 'UserMigration_Authentication' ):

        # authenticate the user with your existing user directory service
        user_status = authenticateUser(event['userName'])

        if ( user_status == 'true' ):
            event['response']['userAttributes'] = {
                "email": event['userName'],
                "email_verified": "true"
            }
        
            event['response']['finalUserStatus'] = "CONFIRMED"
            event['response']['messageAction'] = "SUPPRESS"
        else:
            raise Exception('Bad username or password')

    elif ( event['triggerSource'] == 'UserMigration_ForgotPassword' ):

        # lookup the user in your existing user directory service
        user_status = authenticateUser(event['userName'])
        if ( user_status == 'true' ):
            event['response']['userAttributes'] = {
                "email": event['userName'],
                "email_verified": "true"
            }

            event['response']['messageAction'] = "SUPPRESS"
        else:
            raise Exception('Bad username or password')

    else:
        raise Exception('Bad triggerSource' + event['triggerSource'])

    return event
