import os
import ast

os.system('cls' if os.name == 'nt' else 'clear')

def buscaTitulo(nome): #recebe o nome do título da obra.

    with open('database.txt', 'r') as reader:

        for line in reader:
            aux = eval(line)
            if aux['titulo'] == str(nome):
                return line
            
    return False



def cadastraTitulo(titulo): #Recebe um titulo [Dicionário] e converte para string e salva no final do arquivo.
    with open('database.txt', 'a') as writer:
        writer.write(f'\n{titulo}')
        # o \n é usado criar uma nova linha, caso contrário ele irá salvar um do lado do outro.

def mostraBonito(listaDeTilulos):
    
    if type(listaDeTilulos) == str:
            aux = eval(listaDeTilulos)
            print(aux)
    else:
        for linha in listaDeTilulos:
            aux = eval(linha)
            print("Tipo: " + str(aux["tipo"]) + " "*(10-len(str(aux["tipo"]))) + " Titulo: " + str(aux["titulo"]))


def menu():
    print("1- Cadastrar Títulos:")
    print("2- Editar Títulos")
    print("3- Mostrar todos os Títulos") #Dieter
    print("4- Procurar Título") #Luiza
    print("5- Sair do programa")
    
def pegaDadosCadastro(tituloReferencia=False):
    tipo = input("Tipo: ")
    if tituloReferencia:
        tituloReferencia = eval(tituloReferencia)
        titulo = tituloReferencia["titulo"]
    else:
        titulo = input("Titulo: ")
    genero = input("Genero: ")
    duracao = input("Duracao: ")
    assistido = input("Assitido S/N: ")
    if assistido.lower() == "s":
        assistido = '1'
    else:
        assistido = '0'
    titulo = ("{" + f"'tipo': '{tipo}', 'titulo': '{titulo}', 'genero':'{genero}', 'duracao':'{duracao}', 'assistido':'{assistido}'"+ "}")
    print(titulo)
    return titulo


def listaTodosOsTitulos():
    with open('database.txt', 'r') as file:
        # Le a lista de linhas do documento completo e joga em um array
        data = file.readlines()
        return data

def listaTodosDeGenero(generos):
    pass

def relatorioTitulos():
    titulosAretornar = []
    
    with open('database.txt', 'r') as arquivo:
        
        for line in arquivo:
            #aux = ast.literal_eval(line)
            titulosAretornar.append(line)
        return titulosAretornar


#Encontra a pessoa no arquivo e atualiza os dados desta pessoa. 
#Se check for passado ele altera o status de checIn/Out da pessoa;

def editaTitulo(titulo, assistido=False):
    
    with open('database.txt', 'r') as file:
        # Le a lista de linhas do documento completo e joga em um array
        data = file.readlines()
        titulo = eval(titulo)
        if assistido:
            print(titulo)
            titulo['assistido'] = 1
        
        #Percorre todo o "arquivo" data que possui o conteúdo do txt e verifica linha a linha até encontrar o titulo e sobrescreve a linha inteira    
        for i in range (len(data)):
            aux = eval(data[i])

            if aux['titulo'] == titulo['titulo']:
                data[i] = str(titulo)+"\n"

    # Escreve todo o conteúdo da variavel data novamente no arquivo.
    with open('database.txt', 'w') as file:
        file.writelines( data )