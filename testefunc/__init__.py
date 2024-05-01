import azure.functions as func
import mysql.connector
import jwt
import os
from datetime import datetime, timedelta

def main(req: func.HttpRequest) -> func.HttpResponse:
    username = req.params.get('username')

    if not username:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            username = req_body.get('username')

    if username:
        user = get_user_from_db(username)
        if user:
            token = create_token(user)
            return func.HttpResponse(f"Token: {token}")
        else:
            return func.HttpResponse("Usuário não encontrado.", status_code=404)
    else:
        return func.HttpResponse("Por favor, passe um nome de usuário.", status_code=400)

def get_user_from_db(username):
    db_config = {
        'host': os.environ['DB_HOST'],
        'user': os.environ['DB_USER'],
        'password': os.environ['DB_PASSWORD'],
        'database': os.environ['DB_NAME']
    }
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def create_token(user):
    payload = {
        'user_id': user[0],
        'exp': datetime.utcnow() + timedelta(days=1)
    }
    secret = os.environ['JWT_SECRET']
    token = jwt.encode(payload, secret, algorithm='HS256')
    return token
