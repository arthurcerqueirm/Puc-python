from datetime import datetime
arquivo = open("dados.csv", "r")
dados = arquivo.readlines()
arquivo.close()


#inicar variaveis
datas = []
precip = 0    
tentativaDoWhile = True  
for linha in dados[1:]:
    linha = linha[:-1]
    meta = linha.split(",")

    datas.append(meta[0])
    precip = float(meta[1])
    maxima = float(meta[2])
    minima = float(meta[3])
    horas_insol = float(meta[4])
    temp_media = float(meta[5])
    um_relativa = float(meta[6])
    vel_vento = float(meta[7])


while tentativaDoWhile:
    ano = int(input("Digite o ano: (1961 - 2016) "))
    mes = int(input("Digite o mes: (1961 - 2016) "))
    for data in datas:
        if int(data[-4:]) == ano:
            print("2016 só tem dados até o mes de junho (01 - 06)" if ano == 2016 else "")
            if int(data[-7:-5]) == mes:
                tentativaDoWhile = False
                index = datas.index(data)
                break   
    else:
        print("data não encontrada")
        print("Digite novamente")

print(mes,ano)


def procuraAnoMes(ano,mes):
    for data in datas:
        if int(data[-4:]) == ano:
            if int(data[-7:-5]) == mes:
                index = datas.index(data)
                return index
    return -1
