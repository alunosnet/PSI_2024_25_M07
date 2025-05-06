    main()
    #print(sys.argv)
if __name__=="__main__":

        print("Essa opção não existe")
    else:
        Ler()
    elif opcao.lower()=="-l":
        Adicionar()
    if opcao.lower() == "-a":
    opcao = sys.argv[1]
    #opção
        NOME_FICHEIRO = sys.argv[2]
    if len(sys.argv)==3:
    #nome do ficheiro
        return
        print("Utilização: py linha_comandos.py -l | -a [NOME FICHEIRO]")
    if len(sys.argv)<=1:
    #ler os argumentos da linha de comandos
    global NOME_FICHEIRO
def main():

            ficheiro.write(frase+"\n")
            #se frase não está em branco escrever no ficheiro
                break
            if not frase:
            #se frase está em branco terminar programa
            frase = input(">")
            #ler uma frase
        while True:
    with open(NOME_FICHEIRO,"a",encoding="utf-8") as ficheiro:
    #abrir para adicionar
def Adicionar():

        print(linha,end="")
    for linha in linhas:
    
        linhas = ficheiro.readlines()
    with open(NOME_FICHEIRO,"r",encoding="utf-8") as ficheiro:
    #abrir para leitura
        return
        print(f"Ficheiro {NOME_FICHEIRO} não encontrado.")
    if os.path.exists(NOME_FICHEIRO) == False:
def Ler():

NOME_FICHEIRO = "frases.txt"

import os
import sys #para fornecer acesso aos parâmetros da linha de comandos
"""
    py linha_comandos.py -a [NOME_FICHEIRO] - o programa deve adicionar ao ficheiro indicado ou ao ficheiro prédefinido todas as linhas que o utilizador escreve até introduzir uma linha em branco

    py linha_comandos.py -l [NOME_FICHEIRO] - o programa deve a abrir o ficheiro indicado ou o ficheiro prédefinido e listar todo o seu conteúdo
Utilização:
Programa para gravar e ler ficheiros de texto.
"""
