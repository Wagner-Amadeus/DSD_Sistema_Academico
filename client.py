import Pyro4
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def menu():
    os.system('cls')
    print("Escolha uma opção:")
    print("[1] Cadastrar um novo aluno")
    print("[2] Listar os alunos cadastrados")
    print("[3] Excluir aluno cadastrado")
    print("[4] Exportar para um arquivo .csv")
    print("[5] Gerar ralatório")
    print("[6] Sair\n")


def cadastrar_aluno(sistema_academico):
    nome = input("Nome do aluno: ")
    nota1 = float(input("\nNota 1: "))
    nota2 = float(input("Nota 2: "))
    sistema_academico.cadastrar_aluno(nome, nota1, nota2)
    os.system('cls')
    print("Aluno cadastrado com sucesso!\n")
    input("\nPressione qualquer tecla para continuar...")


def excluir_aluno(sistema_academico):
    nome = input("Nome do aluno a ser excluído: ")
    if sistema_academico.excluir_aluno(nome):
        os.system('cls')
        print(f"Aluno {nome} excluído com sucesso.")
    else:
        os.system('cls')
        print(f"Aluno {nome} não encontrado.")
    input("\nPressione qualquer tecla para continuar...")


def listar_alunos(sistema_academico):
    alunos = sistema_academico.listar_alunos()
    if not alunos:
        os.system('cls')
        print("Nenhum aluno cadastrado.")
        input("\nPressione qualquer tecla para continuar...")
    else:
        os.system('cls')
        print("LISTA DE ALUNOS".center(80))
        print("\nNOME".ljust(20) + "NOTA 1".ljust(10) + "NOTA 2".ljust(10) + "MÉDIA".ljust(20) + "SITUAÇÃO".ljust(20))
        for aluno in alunos:
            print(f"{aluno['nome']}".ljust(20) + f"{aluno['nota1']}".ljust(10) + f"{aluno['nota2']}".ljust(10) + f"{aluno['media']}".ljust(20) + f"{aluno['situacao']}".ljust(20))
        input("\nPressione qualquer tecla para continuar...")
        os.system('cls')


def exportar(sistema_academico):
    arquivo = input("Digite o nome do arquivo CSV para exportar os alunos (ex: alunos.csv): ")
    resultado = sistema_academico.exportar(arquivo)
    if resultado is True:
        print(f"\tAlunos exportados com sucesso para o arquivo: {arquivo}.")
    else:
        print(f"Erro ao exportar alunos: {resultado}")
    input("\nPressione qualquer tecla para continuar...")


def exportar_pdf(sistema_academico):
    arquivo = input("Digite o nome do arquivo PDF para exportar os alunos (ex: alunos.pdf): ")
    resultado = sistema_academico.exportar_pdf(arquivo)
    if resultado is True:
        print(f"Alunos exportados para o arquivo PDF {arquivo}.")
    else:
        print(f"Erro ao exportar alunos para PDF: {resultado}")
    input("\nPressione qualquer tecla para continuar...")


def sair(sistema_academico):
    return False


def main():
    sistema_academico = Pyro4.Proxy("PYRO:obj_a685f1cb5676488ba43f15bcc9904c7b@localhost:50871")

    opcoes = {
        '1': cadastrar_aluno,
        '2': listar_alunos,
        '3': excluir_aluno,
        '4': exportar,
        '5': exportar_pdf,
        '6': sair,
    }

    while True:
        menu()
        opcao = input("Opção: ")

        if opcao in opcoes:
            if opcoes[opcao](sistema_academico) is False:
                break
        else:
            print("Opção inválida. Tente novamente.")


########## FIM DOS MÉTODOS ##########

if __name__ == '__main__':
    main()
