import azure.functions as func
import jwt
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Obter o token JWT do cabeçalho de autorização
    token = req.headers.get('Authorization')
    if not token or not token.startswith('Bearer '):
        return func.HttpResponse("Token não fornecido ou formato inválido", status_code=401)

    try:
        # Extrair o token sem o prefixo 'Bearer '
        token = token.split(' ')[1]
        # Decodificar o token usando a chave secreta e verificar a validade
        decoded_token = jwt.decode(token, os.environ['JWT_SECRET'], algorithms=['HS256'])
        # Se o token for válido, continue com a lógica da função
        return func.HttpResponse(f"Acesso autorizado para o usuário {decoded_token['user_id']}")
    except jwt.ExpiredSignatureError:
        return func.HttpResponse("Token expirado", status_code=401)
    except jwt.InvalidTokenError:
        return func.HttpResponse("Token inválido", status_code=401)


