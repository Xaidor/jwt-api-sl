import json
import jwt
import datetime

# In production, store this in AWS Secrets Manager or environment variables
SECRET_KEY = "my_super_secret_key"

def lambda_handler(event, context):
    
    # Create payload (data stored in the token)
    payload = {
        "user": "authorized_user",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }

    # Generate token
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "token": token
        })
    }
