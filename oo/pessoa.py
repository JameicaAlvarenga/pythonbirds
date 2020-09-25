class Pessoa:
    def __init__(self, *filhos, nome=None,idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
        #self.nome = atributo nome
        #nome = parametro passado

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    filho = Pessoa(nome='Renzo')
    pai = Pessoa(filho, nome="Luciano",idade=40)
    print(Pessoa.cumprimentar(pai))
    print(id(pai))
    print(pai.cumprimentar())
    print(pai.nome , 'idade:' ,pai.idade)
    for filhos in pai.filhos:
        print("Nome do Filho:",filhos.nome)


