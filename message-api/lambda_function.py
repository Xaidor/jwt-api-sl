import json
from shared.jwt_utils import verify_token

def lambda_handler(event, context):
    headers = event.get("headers", {})
    auth_header = headers.get("Authorization")

    if not auth_header:
        return response(401, "Missing Authorization header")

    try:
        token = auth_header.split(" ")[1]
        decoded = verify_token(token)

        message = "You've been granted February 2026 access! Happy Black History Month 🖤"

        return response(200, {
            "message": message,
            "user": decoded["user"]
        })

    except Exception:
        return response(401, "Invalid or expired token")


def response(status, body):
    return {
        "statusCode": status,
        "body": json.dumps(body)
    }
