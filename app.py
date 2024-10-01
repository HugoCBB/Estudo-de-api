from api import api
from banco import criar_tabela, adicionar_dados
import sqlite3

conn = sqlite3.connect('meu_banco.db')
criar_tabela()

def head():
    return print('''
=======================
    MATRICULA 2000
=======================
                 ''')
class User:
    def __init__(self, nome, idade, cep):
    
        self.nome = nome
        self.idade = idade
        self.cep = api(cep)

        
    def matricula(self):
        adicionar_dados(
            self.nome, 
            self.idade, 
            self.cep['cep'], 
            self.cep['bairro'], 
            self.cep['localidade'], 
            self.cep['estado'], 
            self.cep['regiao']
            )
        
    def matriculados(self):
        matricula = {
            # 'id':id ,
            'Nome':self.nome,
            'Idade':self.idade,
            'Cep':self.cep['cep'],
            'Bairro':self.cep['bairro'],
            'Localidade':self.cep['localidade'],
            'Estado':self.cep['estado'],
            'Região':self.cep['regiao'],
        }

        for key, value in matricula.items():
            print(f'{key}: {value}')


head()
p1 = User('Sofia', 12,  41347565 )
p1.matricula()
p1.matriculados()
# print('========================')
# p2 = User('Maicon', 12, 41342754)
# p2.matricula()



