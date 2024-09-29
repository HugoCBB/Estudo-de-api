from api import api

class User:
    def usuario(self, nome, idade, cep):
        self.nome = nome
        self.idade = idade
        self.cep = api(cep)

        for key, value in self.cep.items():
            print(f'{key}: {value}')


p1 = User()
p1.usuario('Hugo', 15, 41342812)
