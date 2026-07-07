from datetime import datetime
from utilidades import limpar_tela_cabecalho, validar_cpf, validar_email, ler_int, ler_float

def modulo_quartos(quartos):
    op = ''
    while op != '0':
        limpar_tela_cabecalho("Módulo Quartos")
        print("----- 1 - Cadastrar Novo Quarto        -----")
        print("----- 2 - Alterar Preço da Diária      -----")
        print("----- 3 - Alterar Status do Quarto     -----")
        print("----- 0 - Retornar ao Menu Principal   -----")
        print("============================================")
        op = input("===== Escolha sua opção: ")
        
        if op == '1':
            limpar_tela_cabecalho("Novo Quarto")
            num_quarto = input("# Numero do Quarto: ")
            if num_quarto in quartos:
                print("\n Erro: Este quarto já existe!")
            else:
                tipo = input("# Tipo (Solteiro/Casal/Luxo): ")
                preco = ler_float("# Preço diário: R$ ")
                status = input("# Status (Disponivel/Reservado/Ocupado/Manutencao): ")
                quartos[num_quarto] = [tipo, preco, status]
                print("\n Quarto cadastrado com sucesso!")
            input("\n Tecle <ENTER> para continuar...")
            
        elif op == '2':
            limpar_tela_cabecalho("Preço da Diária")
            num_quarto = input("# Número do quarto: ")
            if num_quarto in quartos:
                print(f"\n Preço atual: R$ {quartos[num_quarto][1]:.2f}")
                novo_preco = ler_float("# Novo preço: R$ ")
                quartos[num_quarto][1] = novo_preco
                print("\n Diária atualizada!")
            else:
                print("\n Quarto não encontrado!")
            input("\n Tecle <ENTER> para continuar...")

        elif op == '3':
            limpar_tela_cabecalho("Alterar Status")
            num_quarto = input("# Número do quarto: ")
            if num_quarto in quartos:
                status_atual = quartos[num_quarto][2]
                print(f"\n Status atual: {status_atual}")
                if status_atual == 'Ocupado':
                    print("\n Erro: Este quarto está OCUPADO por um hóspede!")
                    print(" Para desocupá-lo, realize o Check-out no Módulo Hospedagem.")
                else:
                    while True:
                        novo_status = input("# Novo Status (Disponivel/Manutencao/Reservado): ").strip()
                        
                        if novo_status.lower() == 'disponivel':
                            novo_status = 'Disponivel'
                            break
                        elif novo_status.lower() == 'manutencao':
                            novo_status = 'Manutencao'
                            break
                        elif novo_status.lower() == 'reservado':
                            novo_status = 'Reservado'
                            break
                        elif novo_status.lower() == 'ocupado':
                            print("\n Erro: Não é permitido mudar para 'Ocupado' manualmente.")
                            print(" Use a opção de Check-in no Módulo Hospedagem.")
                        else:
                            print("\n Erro: Status inválido! Opções: Disponivel, Manutencao ou Reservado.")
                    
                    quartos[num_quarto][2] = novo_status
                    print("\n Status atualizado com sucesso!")
            else:
                print("\n Quarto não encontrado!")
            input("\n Tecle <ENTER> para continuar...")