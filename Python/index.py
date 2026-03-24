# Sistema de Controle de Estoque com Entrada e Saída

estoque = {}
movimentacoes = []

def cadastrar_produto():
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade inicial: "))
    
    estoque[nome] = quantidade
    print("Produto cadastrado!\n")

def entrada_produto():
    nome = input("Produto: ")
    
    if nome in estoque:
        quantidade = int(input("Quantidade recebida: "))
        data = input("Data da entrada: ")
        
        estoque[nome] += quantidade
        
        movimentacoes.append(f"Entrada - Produto: {nome}, Qtd: {quantidade}, Data: {data}")
        
        print("Entrada registrada!\n")
    else:
        print("Produto não encontrado.\n")

def saida_produto():
    nome = input("Produto: ")
    
    if nome in estoque:
        quantidade = int(input("Quantidade retirada: "))
        
        if quantidade <= estoque[nome]:
            data = input("Data da saída: ")
            responsavel = input("Responsável: ")
            
            estoque[nome] -= quantidade
            
            movimentacoes.append(f"Saída - Produto: {nome}, Qtd: {quantidade}, Data: {data}, Resp: {responsavel}")
            
            print("Saída registrada!\n")
        else:
            print("Estoque insuficiente!\n")
    else:
        print("Produto não encontrado.\n")

def listar_estoque():
    for nome, quantidade in estoque.items():
        print(f"{nome} - Quantidade: {quantidade}")
    print()

def listar_movimentacoes():
    print("Histórico:")
    for mov in movimentacoes:
        print(mov)
    print()

def menu():
    while True:
        print("1 - Cadastrar produto")
        print("2 - Entrada de produto")
        print("3 - Saída de produto")
        print("4 - Listar estoque")
        print("5 - Ver movimentações")
        print("0 - Sair")
        
        opcao = input("Escolha: ")
        
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            entrada_produto()
        elif opcao == "3":
            saida_produto()
        elif opcao == "4":
            listar_estoque()
        elif opcao == "5":
            listar_movimentacoes()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!\n")

menu()
