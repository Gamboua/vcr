import sys
sys.path.insert(0, "~/projects/unittest-pytest/http_client.py")

import pytest
import requests
import vcr

from http_client import get_client

'''
    Depois rodar a primeira vez, vc pode remover esse decorador.
    Ele vai criar o arquivo com o nome da função. Eu deixei as duas funções
    só pra deixar como exemplo.
    Só um detalhe. Se vc trocar o método, vai precisar gerar de novo.
    Se vc mudar algum parâmetro, vai precisar gerar de novo.
'''
# @pytest.mark.vcr()
# def test_get_client_should_return_json_response():
#     url = 'https://jsonplaceholder.typicode.com/todos/1'

#     r = requests.get(
#         url=url
#     )

'''
    Esse é o decorador para usar o yaml criado.
    Ele pode vir com o caminho do arquivo yaml ou,
    caso ele tenha o mesmo nome do arquivo, pode chamar
    o método vazio:
    @vcr.use_cassette()
    def test_get_client_should_return_json_response()
'''
@vcr.use_cassette()
def test_get_client_should_return_json_response():
    r = get_client()

    assert isinstance(r, dict)
