class Pessoa:
    def __init__(self, *filhos, nome=None,idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {id(self)}'



if __name__ == '__main__':
    pai = Pessoa(nome="Luciano",idade=40)
    pai.filhos.append('Jameica')
    print(Pessoa.cumprimentar(pai))
    print(id(pai))
    print(pai.cumprimentar())
    print(pai.nome , 'idade:' ,pai.idade)
    for filhos in pai.filhos:
        print("Nome do Filho:",pai.filhos)
    pai.sobrenome = 'Ramalho'
    #del pai.filhos
    print(pai.__dict__)
    print(filhos.__dict__)


