#MATEUS 07/10/2026
#sets iniciais de variaveis
menuConfig = 1
Usuario = "juquinha"
SnhUsuario = 999
poder = 0
materiais = []
proximo_id = 1

#PROC configs
def Configs() :
    global menuConfig
    menuConfig = int(input("Qual tipo de Menu deseja?: (1/2)"))

#PROCS LOGIN

def UserAuth ():
    global Usuario
    global SnhUsuario
    global poder
    Usertip1 = "Operador de Almoxarifado"
    UserAtlh1 = "Op. Almox"
    UsertipAll = "Administrador do Sistema"
    UserAtlhAll = "Adm"

    snhUsertip1 = 12345
    snhUserAtlh1 = 12345
    snhUsertipAll = 123
    snhUserAtlhAll = 123

    if (Usuario == Usertip1) and (SnhUsuario == snhUsertip1):
        poder = 1
        if menuConfig == 1:
            menu1()
        else :
            menu2()
    elif (Usuario == UsertipAll) and (SnhUsuario == snhUsertipAll) :
        poder = 2
        if menuConfig == 1:
            menu1()
        else :
            menu2()
    else:
        print("brilhante")
        
       

def loginEntrar():
    global Usuario
    global SnhUsuario

    print("\n=================================")
    Usuario = input("Nome do Usuario: ")
    SnhUsuario = int(input("Senha do Usuario: "))

    UserAuth()



#PROCS MENU
#Cadastrar material
def cadastrar_material():
    global proximo_id
    nome = input("Nome do material: ").strip()
    quantidade = int(input("Quantidade inicial: "))
    materiais.append({"id": proximo_id, "nome": nome, "quantidade": quantidade})
    print(f"Material cadastrado com sucesso! ID: {proximo_id}")
    proximo_id += 1

#Listar Material
def listar_materiais():
    if not materiais:
        print("Nenhum material cadastrado.")
        return
    print("\n--- LISTA DE MATERIAIS ---")
    for mat in materiais:
        print(f"ID: {mat['id']} | Nome: {mat['nome']} | Quantidade: {mat['quantidade']}")

#Atualizar Material
def atualizar_material():
    id_mat = int(input("Informe o ID do material a atualizar: "))
    for mat in materiais:
        if mat["id"] == id_mat:
            novo_nome = input(f"Novo nome ({mat['nome']}): ").strip()
            nova_qtd = input(f"Nova quantidade ({mat['quantidade']}): ").strip()
            if novo_nome:
                mat["nome"] = novo_nome
            if nova_qtd:
                mat["quantidade"] = int(nova_qtd)
            print("Material atualizado com sucesso!")
            return
    print("Material não encontrado.")

#Excluir
def excluir_material():
    id_mat = int(input("Informe o ID do material a excluir: "))
    for mat in materiais:
        if mat["id"] == id_mat:
            materiais.remove(mat)
            print("Material excluído com sucesso!")
            return
    print("Material não encontrado.")

#Registrar retirada
def registrar_retirada():
    id_mat = int(input("Informe o ID do material para retirada: "))
    for mat in materiais:
        if mat["id"] == id_mat:
            qtd_retirada = int(input("Quantidade a retirar: "))
            if qtd_retirada <  mat["quantidade"] :
                mat["quantidade"] -= qtd_retirada
                print(f"Retirada de {qtd_retirada} unidades realizada. Saldo atual: {mat['quantidade']}")
            else :
                print("Quantidade INVALIDA OU SUPERIOR A DISPONIVEL")
                return

#Splash screen
def main():
    while True:
        print("=================================")
        print("=== SISTEMA EMPRESA BRILHANTE ===")
        print("=== Desde = O FOSCO COM VOCE ====")
        print("=================================")
        break
    login()

#Tela de Login
def login():
    while True:
        print("\n=== SISTEMA EMPRESA BRILHANTE ===")
        print("1- Entrar")
        print("2- Configurar")
        print("3- Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            loginEntrar()
        if opcao == "2":
            Configs()
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

#MENU do sistema
def menu1():
    if poder > 1 :
        while True:
            print("\n=== SISTEMA DE ALMOXARIFADO ===")
            print(f"=== BEM VINDO {Usuario} ===")
            print("1. Cadastrar Material")
            print("2. Listar Materiais  ")
            print("3. Atualizar Material")
            print("4. Excluir Material ")
            print("5. Registrar Retirada")
            print("6. Sair")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                cadastrar_material()
            elif opcao == "2":
                listar_materiais()
            elif opcao == "3":
                atualizar_material()
            elif opcao == "4":
                excluir_material()
            elif opcao == "5":
                registrar_retirada()
            elif opcao == "6":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida!")
    else :
        while True:
        
                print("\n=== SISTEMA DE ALMOXARIFADO ===")
                print(f"=== BEM VINDO {Usuario} ===")
                print("1. Listar Materiais  ")
                print("2. Atualizar Material")
                print("3. Registrar Retirada")
                print("4. Sair")
                opcao = input("Escolha uma opção: ").strip()
        
                if opcao == "1":
                    listar_materiais()
                elif opcao == "2":
                    atualizar_material()
                elif opcao == "3":
                    registrar_retirada()
                elif opcao == "4":
                    print("Saindo do sistema...")
                    break
                else:
                    print("Opção inválida!")

def menu2():
    while True:
        
        print("\n=== SISTEMA DE ALMOXARIFADO ===")
        print(f"=== BEM VINDO {Usuario} ===")
        if poder > 1 :
            print("1. Cadastrar Material")

        if poder > 0 :
            print("2. Listar Materiais  ")
            print("3. Atualizar Material")
        if poder > 1 :
            print("4. Excluir Material ")
        if poder > 0 :
            print("5. Registrar Retirada")
            print("6. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_material()
        elif opcao == "2":
            listar_materiais()
        elif opcao == "3":
            atualizar_material()
        elif opcao == "4":
            excluir_material()
        elif opcao == "5":
            registrar_retirada()
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()