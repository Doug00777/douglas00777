class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade
    def apresentar(self): 
        return f'Olá, o meu nome é [self.nome] e tenho [self.idade] anos.' 
    
class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)  
        self.curso = curso 
    def apresentar(sef):
        return f'Olá, meu nome é [self.nome] tenho [self.idade] anos, e estou estudando [self.curso].'
    
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina): 
        super().__init__(nome, idade)
        self.disciplina = disciplina 
def apresentar(self):
    return f'Olá, eu sou professor de [self.disciplina].'

pessoa1 = Pessoa('João', 35)
print(pessoa1.apresentar())  
pessoa2 = Estudante('Guilherme', 25, 'Programação') 
print(pessoa2.apresentar()) 
pessoa3 = Professor('Manoel', 57, 'História') 






    