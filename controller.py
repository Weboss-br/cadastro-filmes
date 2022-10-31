import os
#from random import randrange
#import linecache
import ast

os.system('cls' if os.name == 'nt' else 'clear')

def buscaTitulo(nome): #recebe o nome do título da obra.

    with open('database.txt', 'r') as reader:

        for line in reader:
            aux = ast.literal_eval(line)
            if aux['titulo'] == nome:
                return line
            
    return False



def cadastraTitulo(titulo): #Recebe um titulo [Dicionário] e converte para string e salva no final do arquivo.
    with open('database.txt', 'a') as writer:
        writer.write(f'\n{titulo}')
        # o \n é usado criar uma nova linha, caso contrário ele irá salvar um do lado do outro.


#Encontra a pessoa no arquivo e atualiza os dados desta pessoa. 
#Se check for passado ele altera o status de checIn/Out da pessoa;
def editaPessoa(pessoa, check=False):
    
    with open('pessoas.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
        pessoa = eval(pessoa)
        if check:
            print(pessoa)
            pessoa['checkin'] = 1
        else:
            pessoa['checkin'] = 0
            
        for i in range (len(data)):
            aux = eval(data[i])

            #print(aux['ID'])
            #print(str(pessoa))
            
            if aux['ID'] == pessoa['ID']:
                data[i] = str(pessoa)+"\n"

    # and write everything back
    with open('pessoas.txt', 'w') as file:
        file.writelines( data )
    

def existePessoa(pessoa): #Recebe o [dicionario] pessoa e verifica se ela existe no arquivo e retorna apenas true or false
    with open('pessoas.txt', 'r') as reader:

        for line in reader:
            aux = ast.literal_eval(line)
            if aux['ID'] == pessoa['ID'] or aux['nome'] == pessoa['nome']:
                return True
    return False

def relatorioPessoas():
    pessoasAretornar = []
    
    with open('pessoas.txt', 'r') as reader:
        
        for line in reader:
            aux = ast.literal_eval(line)
            if aux['checkin'] == '1':
                pessoasAretornar.append(aux)
                #print(aux)
        return pessoasAretornar

def mostraPessoasBonito(listaPessoas):
    print("\n")
    for line in listaPessoas:
        tabID = " "*(5-len(str(line["ID"])))
        print("ID:" + str(line["ID"]) + tabID + " Nome: " + line["nome"])
    print("\n")



def menu():
    print("1- Fazer CheckIn:")
    print("2- Fazer CheckOut")
    print("3- Relatorio de hospedes")
    print("4- Procurar hospede")
    print("5- Sair do programa")
    
def pegaDadosCadastro():
    tipo = input("Tipo: ") #
    titulo = input("Titulo: ")
    genero = input("Genero: ")
    duracao = input("Duracao: ")
    assistido = input("Assitido S/N: ")
    if assistido.lower() == "s":
        assistido = '1'
    else:
        assistido = '0'
    titulo = ("{" + f"'tipo': {tipo}, 'titulo': '{titulo}', 'genero':'{genero}', 'duracao':'{duracao}'"+"}")
    return titulo


def listaTodosOsTitulos():
    pass

def listaTodosDeGenero(generos):
    pass

#asdasdas