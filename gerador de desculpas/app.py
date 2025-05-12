"""
Programa que utiliza os ficheiros intro.txt desculpa.txt e culpado.txt para gerar uma frase
"""
import random
import os

FICHEIRO1 = "intro.txt"
FICHEIRO2 = "culpado.txt"
FICHEIRO3 = "desculpa.txt"

def LinhaAleatoria(ficheiro):
    """Função que devolve uma linha aleatória de um ficheiro de texto"""
    if os.path.exists(ficheiro) == False:
        print(f"Falta o ficheiro {ficheiro}")
        return ""
    with open(ficheiro,"r",encoding="utf-8") as ficheiro:
        linhas = ficheiro.readlines()
    linha = random.choice(linhas)
    linha = linha.replace("\n","")
    return linha

print(LinhaAleatoria(FICHEIRO1)+" ",end="")
print(LinhaAleatoria(FICHEIRO2)+ " ",end="")
print(LinhaAleatoria(FICHEIRO3)+".")

