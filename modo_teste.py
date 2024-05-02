import pytest
from . import main  # Importe sua função aqui
from azure.functions import HttpRequest

def test_jwt_validation():
    # Simule um HttpRequest
    req = HttpRequest(
        method='GET',
        url='/api/sua_function',
        headers={'Authorization': 'Bearer <seu_token_jwt>'}
    )
    
    # Chame a função com o request simulado
    response = main(req)
    
    # Verifique se a resposta é o que você espera
    assert response.status_code == 200  # ou outro código conforme esperado
