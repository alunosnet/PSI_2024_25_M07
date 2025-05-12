"""
Programa para ler os dados de um ficheiro binário com o formato:
nome 20s - 20
idade i  -  4
saldo f  -  4
        ------
           28
"""
import struct

with open("dados.bin","rb") as ficheiro:
    #ler os dados todos de uma vez só
    dados_binarios = ficheiro.read(28)
    #esta linha só funciona se os dados forem empacotados da mesma forma
    dados = struct.unpack("20sif",dados_binarios)

#converter a string binária numa string
nome = dados[0].decode('utf-8').rstrip("\x00")
print("Nome: ",nome)
print("Idade: ",dados[1])
print("Saldo: ",dados[2])