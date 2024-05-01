import secrets

def generate_jwt_secret():
    return secrets.token_hex(32)  # Gera um token hexadecimal de 64 caracteres

jwt_secret = generate_jwt_secret()
print(jwt_secret)