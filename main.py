from controller import buscaTitulo, cadastraTitulo, pegaDadosCadastro, menu, relatorioTitulos
from controller import *


#print(buscaTitulo(input("digite o nome da obra")))

while True:
    menu()
    opcao = input("Digite uma opção: ")
    
    match opcao:
        case "1":
            cadastraTitulo(pegaDadosCadastro())
        case "2":
            teste1 = "string"
            teste2 = []
            print(type(teste1))
            print(type(teste2))
        case "4":
            mostraBonito(buscaTitulo(str(input("Digite o titulo"))))
        case "5":
            break
        case _:
            print("NÂO!!!!")
