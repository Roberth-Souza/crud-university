
import random

produtos = {
    1: {
        "nome": "controle ps5",
        "preco": 350.00,
        "estoque": random.choice([True, False]),
    },
    2: {
        "nome": "headset gamer",
        "preco": 180.00,
        "estoque": random.choice([True, False]),
    },
    3: {
        "nome": "mouse gamer",
        "preco": 220.00,
        "estoque": random.choice([True, False]),
    },
}

id_Produto = 3

### * Buscar e adicionar


def buscarProduto():
    '''Busca um produto pelo id e retorna o produto encontrado ou False caso não encontre'''
    busca = input("Digite o id do produto que deseja buscar/alterar: ")
    try:
        busca = int(busca)
    except ValueError:
        print("Digite somente numeros")
        return
    if busca in produtos:
        print("Produto encontrado")
        return produtos[busca]
    print("Produto não encontrado")
    return False


def listarProdutos(produtos):
    '''Lista os produtos disponiveis'''
    if len(produtos) == 0:
        print("Não temos produtos na lista")
    for k, v in produtos.items():
        print(k, v)


def adicionarProduto():
    '''Adiciona um produto a fornecido pelo usuario na lista de produtos
    , caso o produto já exista ele atualiza o estoque para True'''
    global id_Produto
    nome = input("Digite o nome do produto: ")
    for e in produtos.values():
        if e["nome"] == nome:
            e["estoque"] = True
            print("Estoque atualizado com sucesso")
            return
    preco = float(input("Digite o preco do produto: "))
    produto = {"nome": nome, "preco": preco, "estoque": True}
    id_Produto += 1
    produtos[id_Produto] = produto


#### * Verificar estoque:


def verificar_Estoque():
    '''Busca um produto pelo id e verifica se ele está em estoque ou não'''
    for id, v in produtos.items():
        print(f"{id} | {v['nome']} ... R$ {v['preco']:.2f}")
    produto = buscarProduto()
    if produto:
        print(
            f"{produto['nome']} | R$ {produto['preco']:.2f} | {'Em estoque' if produto['estoque'] else 'Fora de estoque'}"
        )


###### * Atualizando


def atualizar_Produto():
    '''Busca um produto pelo id e permite atualizar o nome, preço ou estoque do produto'''
    produto = buscarProduto()
    if produto:
        print("Digite o que deseja alterar: (numero)")
        print("1 - Nome")
        print("2 - Preco")
        print("3 - Estoque")
        escolha = input("Digite a opção desejada: ")
        try:
            escolha = int(escolha)
        except ValueError:
            print("Digite somente numeros")
            return

        if escolha not in range(1, 4):
            print("Opcao nao encontrada")
            return

        elif escolha == 1:
            atualizar_Nome_Produto(produto)
        elif escolha == 2:
            atualizar_Preco_Produto(produto)
        elif escolha == 3:
            atualizar_Estoque_Produto(produto)


def atualizar_Nome_Produto(produto):
    '''Atualiza o nome do produto'''
    print(f"Nome atual: {produto['nome']}")
    produto["nome"] = input("Digite o novo nome do produto: ")
    print("Lista atualizada: ")
    listarProdutos(produtos)
    return


def atualizar_Preco_Produto(produto):
    '''Atualiza o preço do produto'''
    print(f"Preço atual: {produto['preco']}")
    preco = input("Digite o novo preço do produto: ")
    try:
        preco = float(preco)
    except ValueError:
        print('Digite o valor em reais "n.xx" ')
        return
    produto["preco"] = preco
    listarProdutos(produtos)


def atualizar_Estoque_Produto(produto):
    '''Altera o estoque do produto para o valor oposto do atual'''
    produto["estoque"] = not produto["estoque"]
    print("Produto atualizado com sucesso")
    listarProdutos(produtos)
    print("Produto atualizado com sucesso")


#### * Remover produtos:


def removerProduto():
    '''Busca um produto pelo id e remove o produto encontrado da lista de produtos'''
    busca = input("Digite o id do produto que deseja remover: ")
    try:
        busca = int(busca)
    except ValueError:
        print("Digite somente numeros")
        return
    if busca in produtos:
        del produtos[busca]
        print("Produto removido com sucesso")
        listarProdutos(produtos)
    else:
        print("Produto não encontrado")


#### * MENU ---------

opcao = None
while opcao != "0":
    print()
    print("========================================")
    print("               MENU")
    print("========================================")
    print("1 - Listar Produtos")
    print("2 - Adicionar Produto")
    print("3 - Verificar Estoque")
    print("4 - Atualizar Produto")
    print("5 - Remover Produto")
    print("0 - Sair")
    print("========================================")

    if opcao == "1":
        print()
        print("LISTA DE PRODUTOS ======================")
        listarProdutos(produtos)

    elif opcao == "2":
        print()
        print("ADICIONAR DE PRODUTOS ==================")
        adicionarProduto()

        print("LISTA DE PRODUTOS ======================")
        listarProdutos(produtos)

    elif opcao == "3":
        print("VERIFICAR ESTOQUE =========================")
        verificar_Estoque()

    elif opcao == "4":
        print("ATUALIZAR PRODUTO ======================")
        listarProdutos(produtos)
        atualizar_Produto()

    elif opcao == "5":
        print("REMOVER PRODUTO ========================")
        listarProdutos(produtos)
        removerProduto()
        
    elif opcao is not None:
        print("Opção não existe")

    print()
    opcao = input("Opção desejada: ")
