import os

def limpar_tela_cabecalho(titulo):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("============================================")
    print(f"======    {titulo.upper().center(22)}    ======")
    print("============================================")


def apenas_numeros(texto):
    if texto == '': return False
    return all(c in '0123456789' for c in texto)


def validar_cpf(cpf):
    return len(cpf) == 11 and apenas_numeros(cpf)


def validar_email(email):
    return '@' in email and '.com' in email


def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print(" Erro: Introduza um valor numérico válido (use ponto para decimais).")

def ler_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print(" Erro: Introduza um número inteiro válido.")