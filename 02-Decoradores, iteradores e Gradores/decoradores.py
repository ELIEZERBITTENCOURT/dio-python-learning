import functools

##########################Decorador simples##########################

def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar a função.")
        funcao()
        print("Faz algo depois de executar a função.")
    
    return envelope

def ola_mundo():
    print("Olá mundo!")

ola_mundo = meu_decorador(ola_mundo)
ola_mundo()

############### decorador com açúcar sintático '@' ################

def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar a função.")
        funcao()
        print("Faz algo depois de executar a função.")
    
    return envelope

@meu_decorador # <==== açúcar sintático
def ola_mundo():
    print("Olá mundo!")

ola_mundo()

############## decorador com parametros ######################
# Podemos usar o *args e o *kwargs na funçaõ interna
# com isso ela aceitará um numero arbitrário de argumentos posicionais
# e de palavras-chaves.

def duplicar(funcao):
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs)
        funcao(*args, **kwargs)
    
    return envelope

@duplicar 
def aprender(tecnologia):
    print(f"Olá mundo, estou aprendendo {tecnologia}!")

aprender("Python")

##############################################################
def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar a função.")
        funcao(*args, **kwargs)
        print("Faz algo depois de executar a função.")
    
    return envelope

@meu_decorador # <==== açúcar sintático
def ola_mundo(nome, argumento):
    print(f"Olá mundo, {nome}, {argumento}!")

ola_mundo("João", "Estudando python")

##########################################################
def duplicar(funcao):
    def envelope(*args, **kwargs):
        resultado = funcao(*args, **kwargs)
        return resultado
    
    return envelope

@duplicar 
def aprender(tecnologia, outro_argumento):
    print(f"Olá mundo, estou aprendendo {tecnologia}!")
    return tecnologia.upper()

resultado = aprender("Python", 1000)
print(resultado)
########################################################
# 'import functools' está sendo importado lá em cima

def duplicar(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs)
        funcao(*args, **kwargs)
    
    return envelope

@duplicar 
def aprender(tecnologia):
    print(f"Olá mundo, estou aprendendo {tecnologia}!")

aprender("Python")