import os
import shutil
import csv
from pathlib import Path
# OS TIPOS DE ARQUIVOS UTILIZADOS SÃO O .txt E O .csv
# POIS SÃO OS PADRÕES UTILIZADOS EM TRATAMENTO DE DADOS
############# Abrir e fechar arquivo #########################
# open() 
# close()
# modo de abrir arquivos "r"(ler), "w"(escrever) e "a"(anexar)
# file = open("example.txt", "r")
# print(file.read())
# file.close()

############## Lendo arquivo #################################

file = open("example.txt", "r")
print(file.read())# => retorna o texto do arquivo
print(file.readline())# => retorna linha a linha
print(file.readlines())# => retorna texto numa lista

#tip
#while len(linha := file.readline()):
#    print(linha)
file.close()

############## Escrendo em arquivo ############################
arquivo = open("teste.txt", "w")
arquivo.write("Escrevendo em um novo arquivo")
arquivo.writelines(["\n", "escrevendo", "\n","um", "\n","novo","\n","texto"])
arquivo.close()

############## Gerenciando arquivos e diretórios ##############
# podemos criar, renomear, mover e remover um arquivo.
#
# as importações ficam no cabeçalho:
# import os
# import shutil
# from pathlib import Path

ROOT_PATH = Path(__file__).parent
# criar diretorio
os.mkdir(ROOT_PATH / 'novo-diretorio')
# abrir arquivo
newfile = open(ROOT_PATH / "novo.txt", "w")
# fechar arquivo
newfile.close()

# renomear
os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

# mover
shutil.move(ROOT_PATH / "teste.txt", ROOT_PATH / "novo-diretorio" / "teste.txt")

# remover
os.remove(ROOT_PATH / "alterado.txt")

############ Tratamento de exceções mais comuns ########################
# FileNotFoundError
# PermisssionError
# OSError ===> alterado na versão 3.3 de IOError para OSError
# UnicodeDecodeError
# UnicodeEncodeError
# IsADirectoryError

try:
    arquivo = open(ROOT_PATH / "novo-diretorio" / "novo.txt", "r")
except FileNotFoundError as exc:
    print("Arquivo não encontrado!")
    print(exc)
except IsADirectoryError as exc:
    print(f"Não foi possível abrir o arquivo: {exc}")
except OSError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")
except Exception as exc:
    print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")


# try:
#     arquivo = open(ROOT_PATH / "novo-diretorio")
# except IsADirectoryError as exc:
#     print(f"Não foi possível abrir o arquivo: {exc}")

############# BOAS PRÁTICAS NA MANIPULAÇÃO DE ARQUIVOS ##############]
# 1ª  BLoco 'with':
# with open('arquivo.txt', 'r') as arquivo:
#       print('trabalhando com o arquvivo')
# Faça operações de leitura/ gravação no arquivo
# 
# 2ª Verifique se o arquivo foi aberto com sucesso:
# try
#   with open('arquivo.txt', 'r') as arquivo:
# exception OSError as exc:
#   print("Error ao abrir ao arquivo {exc}")
#
# 3ª Use a decodificação correta:
# try:
#  with open(ROOT_PATH/'arquivo.txt', 'r', enconding='utf-8', ) as arquivo:
#       print(arquivo.read())
#  exception OSError as exc:
#       print(f"Error ao abrir ao arquivo {exc}")
# try:
#  with open(ROOT_PATH/'arquivo.txt', 'w', enconding='utf-8', ) as arquivo:
#       arquvio.write('trabalhando com o arquvivo')
#  exception OSError as exc:
#       print(f"Error ao abrir ao arquivo {exc}")
#  exception UnicodeDecodeError as exc:
#       print(f"Error ao abrir ao arquivo {exc}")
#
################# TRABALHANDO COM ARQUIVO .csv ############################
# import csv
ROOT_PATH = Path(__file__).parent

COLUNA_ID = 0
COLUNA_NOME = 1


try:
    with open(ROOT_PATH / "usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["id", "nome"])
        escritor.writerow(["1", "Maria"])
        escritor.writerow(["2", "João"])
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")


try:
    with open(ROOT_PATH / "usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for idx, row in enumerate(leitor):
            if idx == 0:
                continue
            print(f"ID: {row[COLUNA_ID]}")
            print(f"Nome: {row[COLUNA_NOME]}")
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")


try:
    with open(ROOT_PATH / "usuarios.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"ID: {row['id']}")
            print(f"Nome: {row['nome']}")
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")