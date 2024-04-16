# Dicionarios
################ Criação ##############################

pessoa = { "nome": "Rafael", "idade": 28 }

pessoa = dict(nome="Rafael", idade=28)

pessoa["telefone"] = "3333-1234"

print(pessoa)
print("####################################################################")
################## acesso ao dados #####################
dados =  { "nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

print(dados["nome"])
print(dados["idade"])
print(dados["telefone"])

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1234"

print(dados)
print("####################################################################")
################## Dicionarios aninhados #####################
contatos = {
    "guilherme@email.com": { "nome": "Guilherme", "idade": 28, "telefone": "3333-1234"},
    "rafael@email.com": { "nome": "Rafael", "idade": 38, "telefone": "9999-1234"},
    "gabriel@email.com": { "nome": "Gabriel", "idade": 18, "telefone": "9877-1234"},
    "rafaela@email.com": { "nome": "Rafaela", "idade": 19, "telefone": "9956-1234"},
}

print(contatos["gabriel@email.com"]["telefone"])
print("####################################################################")
################## Iterar dicionários #####################
for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)

################## Metodos da classe dict #####################
################## {}.clear #####################
contatos = {
    "guilherme@email.com": { "nome": "Guilherme", "idade": 28, "telefone": "3333-1234"},
    "rafael@email.com": { "nome": "Rafael", "idade": 38, "telefone": "9999-1234"},
    "gabriel@email.com": { "nome": "Gabriel", "idade": 18, "telefone": "9877-1234"},
    "rafaela@email.com": { "nome": "Rafaela", "idade": 19, "telefone": "9956-1234"},
}

contatos.clear()
print(contatos)

################## {}.copy #####################
contatos = {
    "guilherme@email.com": { "nome": "Guilherme", "telefone": "3333-1234"}
}

copia = contatos.copy()
copia["guilherme@email.com"] = {"nome": "Gui"}

print(contatos["guilherme@email.com"])
print(copia["guilherme@email.com"])

################## {}.fromkeys #####################
dict.fromkeys(["nome", "telefone"]) # {"nome": None, "telefone": None}

dict.fromkeys(["nome", "telefone"], "vazio") # {"nome": vazio, "telefone": vazio}

################## {}.get #####################
contatos = {
    "rafael@email.com": { "nome": "Rafael", "telefone": "3333-2234"}
}

contatos["chave"] # KeyError
contatos.get("chave") # None
contatos.get("chave", {}) # {}
contatos.get("rafael@email.com", {}) # "rafael@email.com": { "nome": "Rafael", "telefone": "3333-2234"}

################## {}.items #####################

contatos.items() # dict_items([('rafael@email.com': { 'nome': 'Rafael', 'telefone': '3333-2234'})])

################## {}.keys #####################

contatos.keys() # dict_keys([('rafael@email.com')])

################## {}.pop #####################

contatos.pop("rafael@email.com") # { "nome": "Rafael", "telefone": "3333-2234"}
contatos.pop("rafael@email.com", {}) # {}

################## {}.popitem #####################

contatos.popitem() # ("rafael@email.com", { "nome": "Rafael", "telefone": "3333-2234"})
contatos.popitem() # KeyError

################## {}.setdefault #####################
contato = {'nome': 'Gui', 'telefone': '1234-5678'}

contato.setdefault("nome", "Giovana") # Giovana
print(contato)

contato.setdefault("idade", 36) # 36
print(contato)

################## {}.update #####################
contatos = {
    "rafael@email.com": { "nome": "Rafael", "telefone": "3333-2234"}
}
contatos.update({"rafael@email.com": { "nome": "Rafa"}})
print(contatos)

################## {}.values #####################

contatos.values()

################## in #####################

"rafael@email.com" in contatos # True
"rafaela@email.com" in contatos # False
"idade" in contatos["rafael@email.com"] # False
"telefone" in contatos["rafael@email.com"] # True

################## del #####################

del contatos["rafael@email.com"]["telefone"]

print(contatos)