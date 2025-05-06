"""
Programa para ler e guardar dados em ficheiros csv para carros e pilotos de corridas.
carros.csv : marca, modelo, matricula
pilotos.csv: nome,idade,pais

Funcionalidades:
    Adicionar: carros, pilotos
    Listar   : carros, pilotos
    Pesquisar: Pilotos de um carro, carro de um piloto
"""
import csv
import os

FICHEIRO_PILOTOS = "pilotos.csv"
FICHEIRO_CARROS = "carros.csv"

lista_pilotos = []
lista_carros  = []

def LerFicheiro(nome_ficheiro):
    """Função para ler ficheiro csv e devolver uma lista com os dados"""
    #lista vazia para guardar os dados do ficheiro
    dados = []
    #verificar se o ficheiro existe
    if os.path.exists(nome_ficheiro) == False:
        return dados
    
    #abrir ficheiro para leitura
    with open(nome_ficheiro,"r",encoding="utf-8") as ficheiro:
        #criar o objeto para ler o csv
        ler = csv.DictReader(ficheiro)

        #ler cada linha do ficheiro e adicionar à lista
        for linha in ler:
            dados.append(linha)
    #devolver a lista com os dados do ficheiro
    return dados

def Escrever(lista,nome):
    """Função para escrever os dados de uma lista num ficheiro csv"""
    chaves = lista[0].keys()

    with open(nome,"w",encoding='utf-8',newline='') as ficheiro:
        #variável para gravar no ficheiro (ficheiro, campos do dicionário)
        escrever = csv.DictWriter(ficheiro,fieldnames=chaves)
        #gravar o cabeçalho
        escrever.writeheader()
        for i in range(len(lista)):
            escrever.writerow(lista[i]) #grava os dados correspondentes às chaves

def Adicionar():
    op = input("Adicionar [P]iloto ou [C]arro? ")
    if op in "cC":
        #ler os dados do carro
        marca     = input("Qual a marca do carro: ")
        modelo    = input("Qual o modelo do carro: ")
        matricula = input("Qual a matrícula do carro: ")
        #criar um dicionário
        carro ={
            'marcar'    : marca,
            'modelo'    : modelo,
            'matricula' : matricula
        }
        #adicionar à lista
        lista_carros.append(carro)
        #escrever no ficheiro dos carros
        Escrever(lista_carros,FICHEIRO_CARROS)
    if op in "pP":
        #ler os dados do piloto
            #verificar se a matrícula do carro existe
        #criar um dicionário
        #adicionar à lista
        #escrever no ficheiro dos pilotos
        pass

def Listar():
    pass

def Pesquisar():
    pass

def Menu():
    global lista_carros
    lista_carros = LerFicheiro(FICHEIRO_CARROS)
    op=0
    while op!=4:
        op = int(input("1.Adicionar\n2.Listar\n3.Pesquisar\n4.Sair"))
        if op == 1:
            Adicionar()
        if op == 2:
            Listar()
        if op == 3:
            Pesquisar()

if __name__=='__main__':
    Menu()