# como criar conjuntos
# não confiar na ordem que será criado o set
numeros = set([1, 2, 3, 1, 2, 3])
print(numeros)
# {1, 2, 3}

letras = set('abacaxi')
print(letras)
#{'b', 'a', 'c', 'x', 'i'} ou outra ordem

linguagens = set(['python', 'java', 'javascript', 'c++'])
print(linguagens)

# como acessar um conjunto
# primeiro transformar em lista
numeros1 = {1, 2, 3, 4, 5}
numeros2 = list(numeros1)
print(numeros2[0])

# iterar conjunto
carros = {'gol', 'celta', 'palio'}
for carro in carros:
    print(carro)

# função enumerate() nos conjuntos
carros2 = {'renegate', 'ka', 'prisma'}
for indice, carro1 in enumerate(carros2):
    print(f"{indice}: {carro1}")

# Metodos da classe set
# {}.union
conjunto_a = {1,2}
conjunto_b = {3,4}

conjunto_c = conjunto_a.union(conjunto_b)

print(conjunto_c)

# {}.intersection
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_c = conjunto_a.intersection(conjunto_b)

print(conjunto_c)

#{}.difference
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_c = conjunto_a.difference(conjunto_b)
conjunto_d = conjunto_b.difference(conjunto_a)

print(conjunto_c, conjunto_d)

#{}.symmetric_difference
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_c = conjunto_a.symmetric_difference(conjunto_b)

print(conjunto_c)

#{}.issubset
conjunto_a = {1,2,3}
conjunto_b = {4,5,6, 2, 1, 9}

conjunto_c = conjunto_a.issubset(conjunto_b)
conjunto_d = conjunto_b.issubset(conjunto_a)

print(conjunto_c, conjunto_d)

#{}.issuperset
conjunto_a = {1,2,3}
conjunto_b = {4,5,6, 2, 1, 9}

conjunto_c = conjunto_a.issuperset(conjunto_b)
conjunto_d = conjunto_b.issuperset(conjunto_a)

print(conjunto_c, conjunto_d)

#{}.isdisjoin
conjunto_a = {1,2,3}
conjunto_b = {4,5,6, 2, 1, 9}
conjunto_c = {1,0}

conjunto_d = conjunto_a.isdisjoin(conjunto_b)
conjunto_f = conjunto_a.isdisjoin(conjunto_c)

print(conjunto_d, conjunto_f)

