######### Módulo datetime() ##########

# import datetime                 <=== também pode ser usado como importação no python
# data = datetime.date(2024, 5, 19)
# print(data)

from datetime import date, datetime, timedelta, timezone

data = date(2024, 5, 19)
print(data)
print(date.today())

data_hora = datetime(2024, 5, 19)
print(data_hora)
print(datetime.today())

############ timedelta() #########################

tipo_de_carro = 'P'
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_de_carro == 'P':
    data_estimada = data_atual + timedelta(minutos=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficara pronto às {data_estimada}")
elif tipo_de_carro == 'M':
    data_estimada = data_atual + timedelta(minutos=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficara pronto às {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutos=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficara pronto às {data_estimada}")

print(date.today() - timedelta(days=1))

############## Formatando e convertendo datas com strtime e strptime ##############
data_hora_atual = datetime.now()
data_hora_str = "2024-10-20 10:20"
mascara_ptbr = "%d/%m/%Y %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))

############## Trabalhando com timezone()#########################
# Com biblioteca 'pytz'
# > criar ambiente venv
# > instalar o pacote 'pytz' (pip install pytz)
# > e depois deve ser importado o pytz 
# import pytz
#
# data_pytz = datetime.now(pytz.timezone("Europe/Oslo"))
# data_pytz1 = datetime.now(pytz.timezone("America/Sao_Paulo"))
#
# print(data_pytz)
# print(data_ptz1)

data_timezone_oslo = datetime.now(timezone(timedelta(hours=2)))
data_timezone_saopaulo = datetime.now(timezone(timedelta(hours=3)))

print(data_timezone_oslo)
print(data_timezone_saopaulo)
