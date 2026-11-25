# Tarefa 02 - Sistema de Cadastro de Alunos
# Disciplina: Introdução à Ciência da Computação
# Aluno(s): Matheus Ronei Sagás (26102325)
# Data: 24/11/2026

from datetime import datetime


alunos = []


def ler_data_nascimento(mensagem="Data de Nascimento (dd/mm/aaaa): "):
    while True:
        data = input(mensagem).strip()
        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            print("Data inválida. Informe uma data válida no formato dd/mm/aaaa.")


def localizar_aluno_por_matricula(matricula):
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            return aluno
    return None


def cadastrar_aluno():
    print("\n=== Cadastrar Aluno ===")

    while True:
        matricula = input("Matrícula: ").strip()
        if not matricula:
            print("Erro: a matrícula é obrigatória.")
        elif localizar_aluno_por_matricula(matricula):
            print("Erro: já existe um aluno com essa matrícula.")
        else:
            break

    nome = input("Nome: ").strip()
    while not nome:
        print("Erro: o nome é obrigatório.")
        nome = input("Nome: ").strip()

    endereco = input("Endereço: ").strip()
    while not endereco:
        print("Erro: o endereço é obrigatório.")
        endereco = input("Endereço: ").strip()

    data_nascimento = ler_data_nascimento()
    alunos.append({
        "matricula": matricula,
        "nome": nome,
        "endereco": endereco,
        "data_nasc": data_nascimento,
    })
    print("Aluno cadastrado com sucesso!")


def listar_alunos():
    print("\n=== Alunos Cadastrados ===")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        print(
            f"Matrícula: {aluno['matricula']} | "
            f"Nome: {aluno['nome']} | "
            f"Endereço: {aluno['endereco']} | "
            f"Data de Nascimento: {aluno['data_nasc']}"
        )


def buscar_aluno():
    print("\n=== Buscar Aluno ===")
    termo = input("Digite o nome ou a matrícula: ").strip()
    if not termo:
        print("Erro: informe um nome ou uma matrícula para buscar.")
        return

    resultados = [
        aluno for aluno in alunos
        if termo.casefold() in aluno["nome"].casefold()
        or termo.casefold() in aluno["matricula"].casefold()
    ]
    if not resultados:
        print("Nenhum aluno encontrado.")
        return

    for aluno in resultados:
        print(
            f"Matrícula: {aluno['matricula']} | "
            f"Nome: {aluno['nome']} | "
            f"Endereço: {aluno['endereco']} | "
            f"Data de Nascimento: {aluno['data_nasc']}"
        )


def alterar_aluno():
    print("\n=== Alterar Aluno ===")
    matricula_atual = input("Matrícula do aluno: ").strip()
    aluno = localizar_aluno_por_matricula(matricula_atual)
    if aluno is None:
        print("Aluno não encontrado.")
        return

    print("Pressione Enter para manter o valor atual.")
    nova_matricula = input(
        f"Matrícula [{aluno['matricula']}]: "
    ).strip()
    if nova_matricula:
        outro_aluno = localizar_aluno_por_matricula(nova_matricula)
        if outro_aluno is not None and outro_aluno is not aluno:
            print("Erro: já existe outro aluno com essa matrícula.")
            return

    novo_nome = input(f"Nome [{aluno['nome']}]: ").strip()
    novo_endereco = input(f"Endereço [{aluno['endereco']}]: ").strip()
    nova_data = input(
        f"Data de Nascimento [{aluno['data_nasc']}] (dd/mm/aaaa): "
    ).strip()

    if nova_data:
        try:
            datetime.strptime(nova_data, "%d/%m/%Y")
        except ValueError:
            print("Erro: data inválida. Use o formato dd/mm/aaaa.")
            return

    if nova_matricula:
        aluno["matricula"] = nova_matricula
    if novo_nome:
        aluno["nome"] = novo_nome
    if novo_endereco:
        aluno["endereco"] = novo_endereco
    if nova_data:
        aluno["data_nasc"] = nova_data

    print("Dados do aluno alterados com sucesso!")


def excluir_aluno():
    print("\n=== Excluir Aluno ===")
    matricula = input("Matrícula do aluno: ").strip()
    aluno = localizar_aluno_por_matricula(matricula)
    if aluno is None:
        print("Aluno não encontrado.")
        return

    print(f"Aluno: {aluno['nome']} (matrícula {aluno['matricula']})")
    confirmacao = input("Confirma a exclusão? (s/n): ").strip().casefold()
    if confirmacao == "s":
        alunos.remove(aluno)
        print("Aluno excluído com sucesso.")
    else:
        print("Exclusão cancelada.")


def exibir_menu():
    print("\n=== Sistema de Cadastro de Alunos ===")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Buscar")
    print("4 - Alterar")
    print("5 - Excluir")
    print("0 - Sair")


def exibir_cabecalho():
    print("Tarefa 02 - Sistema de Cadastro de Alunos")
    print("Disciplina: Introdução à Ciência da Computação")
    print("Aluno(s): Matheus Ronei Sagás (26102325)")
    print("Data: 24/11/2026")


def main():
    exibir_cabecalho()
    while True:
        exibir_menu()
        opcao = input("Digite a opção: ").strip()

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            buscar_aluno()
        elif opcao == "4":
            alterar_aluno()
        elif opcao == "5":
            excluir_aluno()
        elif opcao == "0":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Escolha uma opção de 0 a 5.")


if __name__ == "__main__":
    main()