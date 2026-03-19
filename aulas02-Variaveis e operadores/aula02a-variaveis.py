print("hello world")

print(7 + 4)
print("7 + 4")
print("7" + "4") #concatenação de strings

'''

Autor: Miguel
'''
# Variaveis
nome = "Miguel" #str
idade = 18 #int
peso = 68.0 #float

print(nome, idade, peso)
print(f"oiiii {nome}")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))

print(nome, idade, peso)
print(idade + 1)

ano_de_nascimento = 1999
ano_atual = 2026
idade = ano_atual - ano_de_nascimento
print("Sua idade é", idade)