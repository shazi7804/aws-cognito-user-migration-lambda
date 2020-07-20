# AWS Cognito User Migration Lambda trigger

## Feature

1. Cognito migrate user trigger lambda
    - UserMigration_Authentication
    - UserMigration_ForgotPassword
1. Backend Idp of OAuth 2.0 `client_credentials` grant.

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

## Deploy

```
sam build && sam deploy
```