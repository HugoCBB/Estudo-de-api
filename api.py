import requests

def api(cep):
    
    cep = cep
    url = f'https://viacep.com.br/ws/{cep}/json/'
    
    response = requests.get(url)
    dados = response.json()
    
    dicionario = {
        'cep':dados['cep'],
        'logradouto':dados['logradouro'],
        'bairro':dados['bairro'],
        'localidade':dados['localidade'],
        'uf':dados['uf'],
        'estado':dados['estado'],
        'regiao':dados['regiao'],
        'ddd':dados['ddd']
    }

    return dicionario


# print(dicionario['ddd'])
