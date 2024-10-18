# Crie uma classe que modele uma pessoa:

# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
      self.nome = nome 
      self.idade = idade
      self.peso = peso 
      self.altura = altura 

    def envelhecer(self, anos): 
      for _ in range(anos):
        self.idade += 1 
        if self.idade < 21:
          self.crescer(0.5) 

    def engordar(self, quilos):
      self.peso = quilos 

    def emagrecer(self, quilos):
      self.peso = quilos 

    def crescer(self, cm): 
      self.altura = cm 

      # exemplo de uso 
pessoa = Pessoa('João', 20, 70, 1.75)
pessoa.envelhecer(2)
pessoa.engordar(5)
pessoa.emagrecer(2) 
pessoa.crescer(3) 

      # exibindo resultadso 

print(f'\nNome: {pessoa.nome}')
print(f'\nIdade: {pessoa.idade}')
print(f'\nPeso: {pessoa.peso}')
print(f'\nAltura: {pessoa.altura}')  




                     



 
      

