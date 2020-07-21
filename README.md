# AWS Cognito User Migration Lambda trigger

AWS Cognito User Pool migrate user from OAuth 2 provider. The example follow [Migrate User Lambda Trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-migrate-user.html) docs.

## Required

- OAuth 2.0 provider with `client_credentials` grant type.
- Resource Server with OAuth 2.0.

Maybe you can try run [shazi7804/example-oauth2-server](https://github.com/shazi7804/example-oauth2-server) for example of OAuth 2.0 server in [Authlib](https://authlib.org/), the repo reference of [authlib/example-oauth2-server](https://github.com/authlib/example-oauth2-server)

## Feature

1. Cognito migrate user trigger lambda
    - UserMigration_Authentication
    - UserMigration_ForgotPassword
1. Backend Idp of OAuth 2.0 `client_credentials` grant.

## How to migrate users

### Before deploy tasks

1. Get OAuth 2.0 parameters
    - client id and secret key for `client_credentials` grant.
    - OAuth2 token endpoint
    - grant scopes
1. Get Resources user profile endpoint.

### Deploy Migration User Lambda

- Deploy Lambda to AWS

```
sam build && sam deploy
```

- Set Cognito `User Migration` trigger of Lambda arn.

### Users mrigation

When users login or forgot password then trigger migration flow.

> user migrate flow require reset password.

## Local invoke

```
sam build && sam local invoke \
    --parameter-overrides \
        ParameterKey=clientId, ParameterValue=... \
        ParameterKey=clientSecret, ParameterValue=... \
        ParameterKey=scope, ParameterValue=profile \
        ParameterKey=tokenEndpoint, ParameterValue=http://.../oauth/token \
        ParameterKey=profileEndpoint, ParameterValue=http://.../api/user \
    -e events/authentication.json
```

## Author

@shazi7804