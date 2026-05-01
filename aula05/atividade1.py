import itertools

nomes = ["joão", "Lucas", "Jair", "Duda"]

duplas = list(itertools.combinations(nomes, 2))

for dupla in duplas:
    print(dupla)

