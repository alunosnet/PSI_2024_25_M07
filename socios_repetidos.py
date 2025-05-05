"""
Programa para encontrar nomes de sócios repetidos entre dois clubes: Académico e Tondela
"""
import os

NOME1 = "academico.txt"
NOME2 = "tondela.txt"

def socios_repetidos():
    #verificar se existem
    if os.path.exists(NOME1) == False or os.path.exists(NOME2) == False:
        print("Os ficheiros dos sócios não existem.")
        return
    with open(NOME1,"r",encoding="utf-8") as ficheiro:
        socios1 = ficheiro.readlines()
    with open(NOME2 ,"r",encoding="utf-8") as ficheiro:
        socios2 = ficheiro.readlines()
    
    #remover \n
    for i in range(len(socios1)):
        socios1[i] = socios1[i].replace("\n","")
    for i in range(len(socios2)):
        socios2[i] = socios2[i].replace("\n","")

    encontra=False    
    for socio in socios1:
        if socio in socios2:
            print(f"{socio} é sócio dos dois clubes")
            encontra=True
    if encontra==False:
        print("Não existem sócios repetidos nos dois clubes.")

socios_repetidos()