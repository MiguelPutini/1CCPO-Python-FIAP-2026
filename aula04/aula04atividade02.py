def funcao_de_validacao(nota):
    while nota < 0 or nota > 10:
        print("a nota deve estar entre 10 e 0")
        nota = float(input("digite a nota novamente: "))
    return nota

notaA = float(input("Digite a primeira nota: "))
notaA = funcao_de_validacao(notaA)

notaB = float(input("Digite a segunda nota: "))
notaB = funcao_de_validacao(notaB)

media = (notaA + notaB) / 2
print(media)