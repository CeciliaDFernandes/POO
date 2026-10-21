def exibir_menu():
    print("\n======== CADASTRO DE ALUNOS =======")
    print("1 - Adicionar aluno")
    print("2 - Atualizar notas")
    print("3 - Remover aluno")
    print("4 - Exibir alunos e notas")
    print("5 - Exibir médias")
    print("0 - Sair")


def ler_nota(mensagem):
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                return nota
            print("Erro: a nota deve estar entre 0 e 10.")
        except ValueError:
            print("Erro: digite um número válido.")


def ler_quatro_notas():
    notas = []
    for i in range(1, 5):
        notas.append(ler_nota(f"N{i}: "))
    return notas


def adicionar_aluno(alunos, nome, notas):
    if nome in alunos:
        print(f'Aluno "{nome}" já está cadastrado. Use a opção 2 para atualizar.')
        return False
    alunos[nome] = notas
    print(f'Aluno "{nome}" cadastrado com sucesso.')
    return True


def atualizar_notas(alunos, nome, notas):
    if nome not in alunos:
        print(f'Aluno "{nome}" não encontrado.')
        return False
    alunos[nome] = notas
    print(f'Notas do aluno "{nome}" atualizadas com sucesso.')
    return True


def remover_aluno(alunos, nome):
    if nome not in alunos:
        print(f'Aluno "{nome}" não encontrado.')
        return False
    del alunos[nome]
    print(f'Aluno "{nome}" removido com sucesso.')
    return True


def calcular_media(notas):
    return sum(notas) / len(notas)


def exibir_alunos(alunos):
    print("\n--- ALUNOS E NOTAS ---")
    if not alunos:
        print("Nenhum aluno cadastrado")
        return
    for nome, notas in alunos.items():
        notas_str = ", ".join(f"{n:.1f}" for n in notas)
        print(f"{nome}: [{notas_str}]")


def exibir_medias(alunos):
    print("\n--- MÉDIAS ---")
    if not alunos:
        print("Nenhum aluno cadastrado")
        return
    for nome, notas in alunos.items():
        media = calcular_media(notas)
        print(f"{nome}: média = {media:.2f}")


def main():
    alunos = {
        "Ana": [8.5, 7.0, 9.2, 6.8],
        "Carlos": [5.5, 6.0, 7.5, 8.0],
        "Mariana": [9.0, 8.5, 10.0, 9.8],
        "Lucas": [6.5, 7.2, 5.8, 6.9],
        "Fernanda": [7.8, 8.2, 7.0, 8.5],
    }

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Nome do aluno: ").strip().title()
            if not nome:
                print("Erro: o nome não pode ficar em branco.")
                continue
            notas = ler_quatro_notas()
            adicionar_aluno(alunos, nome, notas)

        elif opcao == "2":
            nome = input("Nome do aluno a atualizar: ").strip().title()
            if not nome:
                print("Erro: o nome não pode ficar em branco.")
                continue
            if nome not in alunos:
                print(f'Aluno "{nome}" não encontrado.')
                continue
            notas = ler_quatro_notas()
            atualizar_notas(alunos, nome, notas)

        elif opcao == "3":
            nome = input("Nome do aluno a remover: ").strip().title()
            if not nome:
                print("Erro: o nome não pode ficar em branco.")
                continue
            remover_aluno(alunos, nome)

        elif opcao == "4":
            exibir_alunos(alunos)

        elif opcao == "5":
            exibir_medias(alunos)

        elif opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break

        else:
            print("Opção inválida! Digite uma opção do menu.")


if __name__ == "__main__":
    main()
