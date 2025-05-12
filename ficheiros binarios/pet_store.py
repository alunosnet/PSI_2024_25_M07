"""
Programa para gerir uma pet store.
O programa deve gerir um ficheiro de animais com os dados:
raça   - string (30 bytes)
peso   - float (4 bytes)
genero - string (1 byte)
preço  - float (4 bytes)

Funcionalidades: 1.Adicionar 2.Listar 3.Apagar 4.Editar 5.Sair
"""
import struct,os

FICHEIRO = "pets.bin"
TAMANHO_REGISTO = 39

def Adicionar():
    """Lê os dados do utilizar e adiciona ao ficheiro"""
    raca = input("Raça: ")
    peso = float(input("Peso: "))
    genero = input("Género: ")
    preco = float(input("Preço: "))
    with open(FICHEIRO,"ab") as ficheiro:
        #gravar um campo de cada vez
        ficheiro.write(struct.pack("30s",raca.encode("utf-8")))
        ficheiro.write(struct.pack("f",peso))
        ficheiro.write(struct.pack("1s",genero.encode("utf-8")))
        ficheiro.write(struct.pack("f",preco))
        #gravar o registo de uma vez
        #dados_binario = struct.pack("30sf1sf",raca.encode("utf-8"),peso,genero.encode("utf-8"),preco)
        #ficheiro.write(dados_binario)
    print("Dados registados com sucesso")

def Listar():
    """Lista todos os pets do ficheiro - opcionalmente perguntar a raça e só listar os pets da raça indicada"""
    #testar se ficheiro existe
    if os.path.exists(FICHEIRO)==False:
        print("Ainda não tem dados")
        return
    with open(FICHEIRO,"rb") as ficheiro:
        while True:
            #raça
            dados_binario = ficheiro.read(30)
            if not dados_binario:
                break
            dados = struct.unpack("30s",dados_binario)
            print("Raça ",dados[0].decode("utf-8").rstrip("\x00"))
            #peso
            dados_binario = ficheiro.read(4)
            dados = struct.unpack("f",dados_binario)
            print("Peso ",dados[0])
            #genero
            dados_binario = ficheiro.read(1)
            dados = struct.unpack("1s",dados_binario)
            print("Género: ",dados[0].decode("utf-8").rstrip("\x00"))
            #preço
            dados_binario = ficheiro.read(4)
            dados = struct.unpack("f",dados_binario)
            print("Preço ",dados[0])

def Apagar():
    """Lista os pets e pergunta se é o pet a apagar"""
    with open(FICHEIRO,"rb") as f_ler:
        #criar um ficheiro temporário
        with open("temp.bin","wb") as f_escrever:
            while True:
                raca_binario = f_ler.read(30)
                if not raca_binario:
                    break
                #ler um registo
                peso_binario = f_ler.read(4)
                genero_binario = f_ler.read(1)
                preco_binario = f_ler.read(4)
                raca = struct.unpack("30s",raca_binario)
                #mostrar ao utilizar
                print("Raça: ",raca)
                #se NÃO é para apagar gravar no ficheiro temp
                op = input("Pretende apagar este animal? ")
                if op not in "sS":
                    f_escrever.write(raca_binario)
                    f_escrever.write(peso_binario)
                    f_escrever.write(genero_binario)
                    f_escrever.write(preco_binario)
    #apagar o ficheiro de dados
    
    #mudar o nome do ficheiro temporário


def Editar():
    """Lista os pets e pergunta se pretende editar"""
    pass

def Menu():
    """Menu principal da aplicação"""
    op = 0
    while op != 5:
        op = int(input("1.Adicionar\n2.Listar\n3.Apagar\n4.Editar\n5.Sair"))
        if op == 1:
            Adicionar()
        if op == 2:
            Listar()
        if op == 3:
            Apagar()
        if op == 4:
            Editar()

if __name__ == "__main__":
    Menu()