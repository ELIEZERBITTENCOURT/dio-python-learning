# são tipo de iteradores, ao contrário das listas ou outros iteráveis,
# não armazenam todos os seus valores na memória
# são defindio utilizando funções regulares, mas, ao invés de retornar
# valores usando "return", utilizam "yield".

############### caracteristicas de geradores ######################
# uma vez consumido, ele é esquecido e não pode
# ser acessado novamente.
# exemplo de como consumir api utilizando um gerador:
import requests # type: ignore

def fecth_products(api_url, max_pages=100):
    page = 1
    while page <= max_pages:
        response = requests.get(f"{api_url}?pages{page}")
        data = response.json()
        for product in data['products']:
            yield product
        if 'next_pages' not in data:
            break
        page += 1

# Uso do gerador
for product in fecth_products("http://api.example.com/products"):
    print(product['name'])

#################################################################

def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2

for i in meu_gerador(numeros=[1, 2, 3]):
    print(i)

