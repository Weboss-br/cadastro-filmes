from controller import *




while True:
    menu()
    opcao = input("Digite uma opção: ")
    
    match opcao:
        case "1":
            cadastraTitulo(pegaDadosCadastro())
        case "2":
            opcao2 = buscaTitulo(input("Informe o nome do titulo a ser alterado: "))
            if opcao2:
                print("Informe os novos dados do tilulo: ")
                editaTitulo(pegaDadosCadastro(opcao2))
            else:
                print("Titulo não encontrado ")
        case "3":
            mostraBonito(listaTodosOsTitulos())
        case "4":
            mostraBonito(buscaTitulo(str(input("Digite o titulo: "))))
        case "5":
            break
        case _:
            print("NÃO!!!!")
