import json
from shared.jwt_utils import generate_token

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        username = body.get("username", "guest")

        token = generate_token(username)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "token": token
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }
