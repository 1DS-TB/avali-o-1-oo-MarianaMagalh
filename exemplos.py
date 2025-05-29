# exemplo de Herança e Polimorfismo
# Herança
class Itens_Jogo:
    def __init__(self, magia, forca, protecao):
        self.magia = magia
        self.forca = forca
        self.protecao = protecao

    def atingir(self):
        print("Você atingiu o seu inimigo!")

    def defender(self):
        print("Você conseguiu se denfender do seu inimigo!")

class Tijolo(Itens_Jogo):
    def fazer_barrulho(self):
        print("Você fez barrulho, conseguiu atrair o inimigo!")

class Garrafa(Itens_Jogo):
    def fazer_moloto(self):
        print("Você fez um molotov, jogue-o nos inimigos!")

# Polimorfismo
class Animal:
    def emitir_som(self):
        print("O animal faz um som.")

class Cachorro(Animal):
    def emitir_som(self):
        print(" Au au!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")


animais = [Cachorro(), Gato(), Animal()]

for animal in animais:
    animal.emitir_som()
