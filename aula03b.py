
# função sem retorno e sem parametro
def print_lyrics():
    print("I ain't gonna live forever")
    print("i just want to live while i'm alive")

print_lyrics()


def boas_vindas(nome):
    print(f"olá, {nome}!!! Seja bem vindo")

nome_digitado = input("digite seu nome")
boas_vindas(nome_digitado)

# função com retorno e com parametro
def soma(numa, numb):
    soma = numa + numb
    return soma

print(soma(13, 30))