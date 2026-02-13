# Serverless JWT API (AWS Lambda + API Gateway)
This project is part of my cloud engineering portfolio and demonstrates how to build a secure, serverless API using AWS Lambda and JSON Web Tokens (JWT) for authorization.

## Architecture Overview
This system is designed using two separate APIs:
- Auth API – generates JWT tokens for authenticated users
- Message API – returns a protected message only when a valid JWT is provided

## Tech Stack
- AWS Lambda
- Amazon API Gateway
- Python
- PyJWT

### How It Works
1. A client sends a request to the Auth API
2. The Auth API generates and returns a JWT
3. The client sends that JWT in the Authorization header
4. The Message API verifies the token
5. If valid → access granted
6. If invalid → access denied