"""
Programa para ler até ao final do ficheiro
"""
import os

NOME_FICHEIRO = "nomes.txt"

if os.path.exists(NOME_FICHEIRO)==False:
    print("O ficheiro não existe")
else:

    with open(NOME_FICHEIRO,"r",encoding="utf-8") as ficheiro:
        linhas = ficheiro.readlines()

    for linha in linhas:
        print(linha,end="")

    #versão
    with open(NOME_FICHEIRO,"r",encoding="utf-8") as ficheiro:
        while True:
            linha = ficheiro.readline()
            #verificar se encontrou o fim do ficheiro (EOF)
            if not linha:
                break
            print(linha,end="")
