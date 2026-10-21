def exibir_menu():
    print("\n======== ESTOQUE DA LOJA =======")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Atualizar quantidade")
    print("4 - Exibir estoque")
    print("0 - Sair")


def ler_quantidade(mensagem):
    while True:
        entrada = input(mensagem).strip()
        try:
            quantidade = int(entrada)
            if quantidade < 0:
                print("Erro: a quantidade não pode ser negativa.")
                continue
            return quantidade
        except ValueError:
            print("Erro: digite um número inteiro válido.")


def adicionar_produto(estoque, nome, quantidade):
    if nome in estoque:
        print(f'Produto "{nome}" já está cadastrado. Use a opção 3 para atualizar.')
        return False
    estoque[nome] = quantidade
    print(f'Produto "{nome}" adicionado com sucesso (quantidade: {quantidade}).')
    return True


def remover_produto(estoque, nome):
    if nome not in estoque:
        print(f'Produto "{nome}" não encontrado.')
        return False
    del estoque[nome]
    print(f'Produto "{nome}" removido com sucesso.')
    return True


def atualizar_quantidade(estoque, nome, quantidade):
    if nome not in estoque:
        print(f'Produto "{nome}" não encontrado.')
        return False
    estoque[nome] = quantidade
    print(f'Quantidade do produto "{nome}" atualizada para {quantidade}.')
    return True


def exibir_estoque(estoque):
    print("\n--- ESTOQUE ---")
    if not estoque:
        print("Estoque vazio")
        return
    for nome, quantidade in estoque.items():
        print(f"{nome}: {quantidade} unidade(s)")
    print(f"Total de produtos: {len(estoque)}")


def main():
    estoque = {}
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Nome do produto: ").strip().title()
            if not nome:
                print("Erro: o nome não pode ficar em branco.")
                continue
            quantidade = ler_quantidade("Quantidade: ")
            adicionar_produto(estoque, nome, quantidade)

        elif opcao == "2":
            nome = input("Nome do produto a remover: ").strip().title()
            if not nome:
                print("Erro: o nome não pode ficar em branco.")
                continue
            remover_produto(estoque, nome)

        elif opcao == "3":
            nome = input("Nome do produto a atualizar: ").strip().title()
            if not nome:
                print("Erro: o nome não pode ficar em branco.")
                continue
            quantidade = ler_quantidade("Nova quantidade: ")
            atualizar_quantidade(estoque, nome, quantidade)

        elif opcao == "4":
            exibir_estoque(estoque)

        elif opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break

        else:
            print("Opção inválida! Digite uma opção do menu.")


if __name__ == "__main__":
    main()
