import jwt
import datetime

SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"

def generate_token(username):
    payload = {
        "user": username,
        "role": "authorized_user",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


def verify_token(token):
    decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return decoded
