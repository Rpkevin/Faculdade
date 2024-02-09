def cadastrar_colaborador(id):
    global id_global, lista_colaboradores
    id_global += 1
    print("------------CADASTRO DE COLABORADOR-----------")
    nome = input("Digite o nome do colaborador: ")
    setor = input("Digite o setor do colaborador: ")
    salario = float(input("Digite o salário do colaborador: "))

    colaborador = {
        "id": id,
        "nome": nome,
        "setor": setor,
        "salario": salario
    }

    lista_colaboradores.append(colaborador)
    print("Colaborador cadastrado com sucesso!")
    print("---------------------------------------------")

def consultar_colaborador_por_id():
    print("-------CONSULTA POR COLABORADOR POR ID-------")
    id_consulta = int(input("Digite o ID do colaborador: "))
    encontrado = False
    for colaborador in lista_colaboradores:
        if colaborador["id"] == id_consulta:
            print(colaborador)
            encontrado = True
            break
    if not encontrado:
        print("Colaborador não encontrado.")
    print("--------------------------------------------")

def consultar_colaborador_por_setor():
    print("-----CONSULTA POR COLABORADOR(ES) POR SETOR-----")
    setor_consulta = input("Digite o setor desejado: ")
    encontrados = False
    for colaborador in lista_colaboradores:
        if colaborador["setor"] == setor_consulta:
            print(colaborador)
            encontrados = True
    if not encontrados:
        print("Nenhum colaborador encontrado neste setor.")
    print("----------------------------------------------")

def remover_colaborador():
    id_remover = int(input("Digite o ID do colaborador a ser removido: "))
    removido = False
    for colaborador in lista_colaboradores:
        if colaborador["id"] == id_remover:
            lista_colaboradores.remove(colaborador)
            print("Colaborador removido com sucesso!")
            removido = True
            break
    if not removido:
        print("Colaborador não encontrado.")

lista_colaboradores = []

id_global = 0

funcionarios_cadastrados = 0

print("Bem-vindo ao controle de colaborades do Kevin G. Porto")

while funcionarios_cadastrados < 3:
    cadastrar_colaborador(id_global)
    funcionarios_cadastrados += 1

funcionarios_cadastrados = 0

while True:
    print("------------MENU PRINCIPAL-----------")
    print('Bem-vindo ao controle de colaborades do Kevin G. Porto')
    print("Escolha a opção desejada")
    print("1 - Cadastrar Colaborador")
    print("2 - Consultar Colaborador por ID")
    print("3 - Consultar Colaborador(es) por Setor")
    print("4 - Remover Colaborador")
    print("5 - Consultar Todos os Colaboradores")
    print("6 - Encerrar")
    print("-------------------------------------")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        cadastrar_colaborador(id_global)
    elif opcao == 2:
        consultar_colaborador_por_id()
    elif opcao == 3:
        consultar_colaborador_por_setor()
    elif opcao == 4:
        remover_colaborador()
    elif opcao == 5:
        for colaborador in lista_colaboradores:
            print(colaborador)
    elif opcao == 6:
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida.")
