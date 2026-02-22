import json
import jwt

SECRET_KEY = "my_super_secret_key"

def lambda_handler(event, context):

    headers = event.get("headers", {})
    auth_header = headers.get("authorization") or headers.get("Authorization")

    # No token provided
    if not auth_header:
        return {
            "statusCode": 401,
            "body": json.dumps({"message": "Missing Authorization header"})
        }

    try:
        # Expected format: "Bearer <token>"
        token = auth_header.split(" ")[1]

        # Verify token
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        # Authorized response
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "You've been granted February 2026 access! Happy Black History Month ✊🏾"
            })
        }

    except jwt.ExpiredSignatureError:
        return {
            "statusCode": 401,
            "body": json.dumps({"message": "Token has expired"})
        }

    except jwt.InvalidTokenError:
        return {
            "statusCode": 401,
            "body": json.dumps({"message": "Invalid token"})
        }