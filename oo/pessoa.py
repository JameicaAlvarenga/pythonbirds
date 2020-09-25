class Pessoa:
    def __init__(self, nome=None,idade=35):
        self.idade = idade
        self.nome = nome
        #self.nome = atributo nome
        #nome = parametro passado

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa("Luciano")
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Renzo'
    print(p.nome)
