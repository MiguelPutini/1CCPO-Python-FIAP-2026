nota_final = 3

if nota_final < 6:
    print("reprovado")

nota_final1 = 4

if nota_final1 < 4:
    print("Reprovado")
elif nota_final < 6:
    print("Recuperação")
else:
    print("Aprovado")

print("fim")

nota1 = float(input("digite a primeira nota do aluno: "))
nota2 = float(input("digite a primeira nota do aluno: "))
nota3 = float(input("digite a primeira nota do aluno: "))

notafinal = (nota1 + nota2 + nota3) / 3

print(notafinal)

if notafinal <= 7:
    print("reprovado")
else:
    print("aprovado")
