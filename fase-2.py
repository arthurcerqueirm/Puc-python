import math
from datetime import datetime

arquivo = open("dados.csv", "r")
dados = arquivo.readlines()
arquivo.close()

def exibicaoTabela(dataInicial,dataFinal,exibicao):
    indexDataInicial = datas.index(dataInicial)
    indexDataFinal = datas.index(dataFinal)
    linha = dados[0][:-1].split(",")
    match exibicao:
        case 1:
            print(" " * 3 + ("| " + linha[0] + " | ") + " " * 3 + ("|" +  linha[1]  + " |") + ("|" +  linha[5]  + " |") + ("|" +  linha[6]  + " |") + ("|" +  linha[7]  + " |") )
            for i in range(indexDataInicial,indexDataFinal+1):
                print(("| " + datas[i] + " | ") + " " * 2 + ("|" +  str(precip[i])  + " |") + ("|" +  str(temp_media[i])  + " |") + ("|" +  str(um_relativa[i])  + " |") + ("|" +  str(vel_vento[i])  + " |"))
        case 2:
            
            print(("| " + linha[0] + " | ") + " " * 2 + ("|" +  linha[1]  + " |"))
            for i in range(indexDataInicial,indexDataFinal+1):
                print(("| " + datas[i] + " | ") + " " * 2 + ("|" +  str(precip[i])  + " |"))
        case 3:
            print(("| " + linha[0] + " | ") + " " * 2 + ("|" +  linha[5]  + " |"))
            for i in range(indexDataInicial,indexDataFinal+1):
                print(("| " + datas[i] + " | ") + " " * 2 + ("|" +  str(temp_media[i])  + " |"))
        case 4:
            print(("| " + linha[0] + " | ") + " " * 2 + ("|" +  linha[6]  + " |") + ("|" +  linha[7]  + " |"))
            for i in range(indexDataInicial,indexDataFinal+1):
                print(("| " + datas[i] + " | ") + " " * 2 + ("|" +  str(um_relativa[i])  + " |") + ("|" +  str(vel_vento[i])  + " |"))


#inicar variaveis
datas = []
precip = []    
temp_media = []
um_relativa = []
vel_vento = []
maxima = []
minima = []
horas_insol = []
tentativaDoWhile = True  
for linha in dados[1:]:
    linha = linha[:-1]
    meta = linha.split(",")

    datas.append(meta[0])
    precip.append(float(meta[1]))
    maxima.append(float(meta[2]))
    minima.append(float(meta[3]))
    horas_insol.append(float(meta[4]))
    temp_media.append(float(meta[5]))
    um_relativa.append(float(meta[6]))
    vel_vento.append((meta[7]))

mesInicio = int(datas[0][-7:5])
anoInicio = int(datas[0][-4:])
mesFinal = int(datas[-1][-7:5])
anoFinal = int(datas[-1][-4:])

print("data inicio",mesInicio,anoInicio,mesFinal,anoFinal)


def procuraAnoMes(anoInicio:int,anoFinal:int,mesFinal:int):
    tentativaDoWhileAno = True
    tentativaDoWhileMes = True
    while tentativaDoWhileAno:
        try:
            print("=" * 25)
            ano = int(input(f"Digite o ano ({anoInicio} - {anoFinal}): "))



            if ano < anoInicio or ano > anoFinal:
                print(f"Ano inválido! Digite um ano entre {anoInicio} e {anoFinal}.")
                continue  # Reinicia o loop

            while tentativaDoWhileMes:
                mes = int(input("Digite o mês (1 - 12): "))
                if mes < 1 or mes > 12:
                    print("Mês inválido! Digite um valor entre 1 e 12.")
                    continue  # Reinicia o loop

                if ano == anoFinal and mes > mesFinal:
                    print(f"{anoFinal} só tem dados até {mesFinal} (01 - {mesFinal:02d}).")
                    continue  # Reinicia o loop
                tentativaDoWhileMes = False
            tentativaDoWhileAno = False  # Sai do loop

        except ValueError:
            print(" ")
            print("*" * 25)
            print("⚠️  Somente numeros são válidos ⚠️")
            print("*" * 25)
            
            print(" ")

    data = datetime.strptime(f"01/{mes:02d}/{ano}", "%d/%m/%Y")
    dic_datas = {"data-formatada": f"01/{mes:02d}/{ano}", "data": data}
    return dic_datas


print("Selecione sua data inicial: ")
dataInicial = procuraAnoMes(anoInicio,anoFinal,mesFinal)
for _ in range(3):
    print(" ")

dataFinal = {"data": datetime.strptime(f"01/01/0001", "%d/%m/%Y")}
print("Selecione sua data Final: ")
while dataFinal["data"] < dataInicial["data"]:
    print("")
    print("Atenção! Data final não pode ser menor do que a data Inicial.")
    print("")
    dataFinal = procuraAnoMes(anoInicio,anoFinal,mesFinal)

for _ in range(3):
    print(" ")

print(f"Data de inicio escolhida: {dataInicial}")
print(f"Data de inicio escolhida: {dataFinal}")
for _ in range(3):
    print(" ")
    
print("Selecione os dados que deeja verificar: ")
print("(1) todos os dados. ")
print("(2) apenas os de precipitação. ")
print("(3) apenas os de temperatura ")
print("(4) apenas os de umidade e vento")

escolhaMenu = 0
while escolhaMenu > 4 or escolhaMenu < 1:
    try:
        escolhaMenu = int(input(""))
    except ValueError:
        print("Escolha uma das opções")

print(exibicaoTabela(dataInicial["data-formatada"],dataFinal["data-formatada"],escolhaMenu))

    


