import os
from datetime import datetime

# CPF como registro principal: [Nome, Email, Telefone]
hospedes = {
    '11111111111': ['Maria do Socorro', 'maria@email.com', '(84) 99999-9999'],
    '22222222222': ['Sansão Toscano', 'sansao@email.com', '(84) 88888-8888']
}

# Numero do quarto como registro principal: [Tipo, Preço, Status]
quartos = {
    '101': ['Solteiro', '150.00', 'Disponivel'],
    '102': ['Casal', '250.00', 'Ocupado'],
    '103': ['Luxo', '400.00', 'Manutenção'],
    '104': ['Solteiro', '150.00', 'Ocupado']
}

# Atribuir uma chave de cliente para gerar o dicionario de regristro. Não tem nada haver com o numero do quarto
chave = 1003

# Numero de chave como registro principal: [CPF, Num_Quarto, Data_Entrada, Data_Saida(vazio), Consumo(R$), Valor_Total(vazio)]
registro = {
    1001: ['22222222222', '102', datetime(2026, 6, 5, 14, 30), '', 45.50, ''],
    1002: ['11111111111', '104', datetime(2026, 6, 7, 9, 15), '', 0.0, '']
}

resp = ''
while resp != '0': 
    os.system('cls' if os.name == 'nt' else 'clear') 
    
    print("============================================")
    print("======       GESTÃO DE HOTEIS         ======")
    print("============================================")
    print("----- 1 - Módulo Hóspedes              -----")
    print("----- 2 - Módulo Quartos               -----")
    print("----- 3 - Módulo Hospedagem            -----")
    print("----- 4 - Módulo Relatórios            -----")
    print("----- 5 - Módulo Informações           -----")
    print("----- 0 - Sair                         -----")
    print("============================================")
    resp = input("===== Escolha sua opção: ")
    
    # MODULO HOSPEDES
    if resp == '1':
        resp2 = ''
        while resp2 != '0': 
            os.system('cls' if os.name == 'nt' else 'clear')
            print("============================================")
            print("======       Módulo Hóspedes          ======")
            print("============================================")
            print("----- 1 - Cadastrar Hóspede            -----")
            print("----- 2 - Exibir Dados do Hóspede      -----")
            print("----- 3 - Alterar Dados do Hóspede     -----")
            print("----- 4 - Excluir Hóspede              -----")
            print("----- 0 - Retornar ao Menu Principal   -----")
            print("============================================")
            resp2 = input("===== Escolha sua opção: ")
            
            if resp2 == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("============================================")
                print("======        Cadastrar Hóspede       ======")
                print("============================================")
                cpf = input("# CPF (Apenas números): ")
                
                if cpf in hospedes:
                    print("\n Erro: Este CPF já está cadastrado no sistema!")
                else:
                    nome = input("# Nome do hóspede: ")
                    email = input("# Email: ")
                    numero = input("# Telefone: ")
                    hospedes[cpf] = [nome, email, numero]
                    print("\n Hóspede cadastrado com sucesso!")
                input("\n Tecle <ENTER> para continuar...")
                
            elif resp2 == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("============================================")
                print("======      Exibir Dados do Hóspede   ======")
                print("============================================")
                cpf = input("# Digite o CPF do hóspede para busca: ")
                
                if cpf in hospedes:
                    print(f"\n # CPF: {cpf}")
                    print(f"# Nome: {hospedes[cpf][0]}")
                    print(f"# Email: {hospedes[cpf][1]}")
                    print(f"# Telefone: {hospedes[cpf][2]}")
                else:
                    print("\n Hóspede não encontrado!")
                input("\n Tecle <ENTER> para continuar...")
                
            elif resp2 == '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("============================================")
                print("======   Alterar Dados do Hóspede     ======")
                print("============================================")
                cpf = input("##### Digite o CPF do hóspede: ")
                
                if cpf in hospedes:
                    print(f"\n Alterando os dados de: {hospedes[cpf][0]}")
                    nome = input("# Digite o Nome: ")
                    email = input("# Digite o Email: ")
                    numero = input("# Digite o Telefone: ")
                    hospedes[cpf] = [nome, email, numero]
                    print("\n Dados atualizados com sucesso!")
                else:
                    print("\n Hóspede não encontrado!")
                input("\n Tecle <ENTER> para continuar...")
                
            elif resp2 == '4':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("============================================")
                print("======        Excluir Hóspede         ======")
                print("============================================")
                cpf = input("# Digite o CPF do hóspede para excluir: ")
                
                if cpf in hospedes:
                    del hospedes[cpf] 
                    print("\n Hóspede removido do sistema!")
                else:
                    print("\n Hóspede não encontrado!")
                input("\n Tecle <ENTER> para continuar...")

    # MÓDULO QUARTOS
    elif resp == '2':
        resp2 = ''
        while resp2 != '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("============================================")
            print("======           Módulo Quartos       ======")
            print("============================================")
            print("----- 1 - Cadastrar Novo Quarto        -----")
            print("----- 2 - Acompanhar Disponibilidade   -----")
            print("----- 3 - Alterar Preço da Diária      -----")
            print("----- 0 - Retornar ao Menu Principal   -----")
            print("============================================")
            resp2 = input("===== Escolha sua opção: ")
    
            if resp2 == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("============================================")
                print("======     Cadastrar Novo Quarto      ======")
                print("============================================")
                num_quarto = input("# Numero do Quarto: ")
                
                if num_quarto in quartos:
                    print("\n Erro: Este quarto já está cadastrado no sistema!")
                else:
                    tipo = input("# Tipo do quarto (Solteiro, casal, luxo): ")
                    preco = input("# Preço diário do quarto: R$ ")
                    status = input("# Disponibilidade (Disponivel/Indisponivel/Manutencao): ")
                    quartos[num_quarto] = [tipo, preco, status]
                    print("\n Quarto cadastrado com sucesso!")
                input("\n Tecle <ENTER> para continuar...")
                        
            elif resp2 == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("============================================")
                print("======     Checkando Disponibilidade  ======")
                print("============================================")
                num_quarto = input("# Digite o número do quarto para busca: ")
                
                if num_quarto in quartos:
                    print(f"\n # Quarto: {num_quarto}")
                    print(f"# Tipo: {quartos[num_quarto][0]}")
                    print(f"# Preço: R$ {quartos[num_quarto][1]}")
                    print(f"# Disponibilidade: {quartos[num_quarto][2]}")
                else:
                    print("\n Quarto não encontrado!")
                input("\n Tecle <ENTER> para continuar...")

            elif resp2 == '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("============================================")
                print("======     Alterar Preço da Diária    ======")
                print("============================================")
                num_quarto = input("# Digite o número do quarto: ")
                
                if num_quarto in quartos:
                    print(f"\n Quarto {num_quarto} localizado.")
                    print(f" Preço atual da diária: R$ {quartos[num_quarto][1]}")
                    novo_preco = input("\n# Digite o NOVO preço da diária: R$ ")
                    quartos[num_quarto][1] = novo_preco
                    print("\n Preço da diária atualizado com sucesso!")
                else:
                    print("\n Quarto não encontrado!")
                input("\n Tecle <ENTER> para continuar...")

    # MÓDULO HOSPEDAGEM
    elif resp == '3':
        resp2 = ''
        while resp2 != '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("============================================")
            print("======         Módulo Hospedagem      ======")
            print("============================================")
            print("----- 1 - Realizar Check-in            -----")
            print("----- 2 - Realizar Check-out           -----")
            print("----- 3 - Registrar Consumo/Serviços   -----")
            print("----- 0 - Retornar ao Menu Principal   -----")
            print("============================================")
            resp2 = input("===== Escolha sua opção: ")
            
            if resp2 == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("============================================")
                print("======        Realizar Check-in       ======")
                print("============================================")
                cpf = input("# CPF do Hóspede: ")
                num_quarto = input("# Número do Quarto: ")
                
                if cpf in hospedes and num_quarto in quartos:
                    if quartos[num_quarto][2] == 'Disponivel':
                        quartos[num_quarto][2] = 'Ocupado' 
                        
                        data_entrada = datetime.now()
                        registro[chave] = [cpf, num_quarto, data_entrada, '', 0.0, '']
                        
                        print(f"\n Check-in de {hospedes[cpf][0]} realizado com sucesso no quarto {num_quarto}!")
                        print(f" >>> O CÓDIGO DA RESERVA É: {chave} <<<")
                        print(f" Entrada registrada às: {data_entrada.strftime('%d/%m/%Y %H:%M')}")
                        
                        chave += 1 
                    else:
                        print("\n Erro: Esse quarto já está ocupado ou em manutenção.")
                else:
                    print("\n Hóspede ou Quarto não encontrado no sistema!")
                input("\n Tecle <ENTER> para continuar...")
                
            elif resp2 == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("============================================")
                print("======       Realizar Check-out       ======")
                print("============================================")
                num_quarto = input("# Número do Quarto para fechar conta: ")
                
                encontrou = False
                for chave_antiga, dados in registro.items():
                    
                    if dados[1] == num_quarto and dados[3] == '':
                        encontrou = True 
                        
                        cpf = dados[0]
                        data_entrada = dados[2]
                        consumo = dados[4]
                        preco_diaria = float(quartos[num_quarto][1])
                        
                        data_saida = datetime.now()
                        dias = (data_saida - data_entrada).days
                        if dias <= 0:
                            dias = 1
                            
                        total_diarias = dias * preco_diaria
                        total_geral = total_diarias + consumo
                        
                        print(f"\n===== EXTRATO #{chave_antiga} =====")
                        print(f" Quarto: {num_quarto}")
                        print(f" Hóspede: {hospedes[cpf][0]}")
                        print(f" Permanência: {dias} dia(s)")
                        print(f" Total Diárias: R$ {total_diarias:.2f}")
                        print(f" Total Consumo: R$ {consumo:.2f}")
                        print("--------------------------------------------")
                        print(f" TOTAL A PAGAR: R$ {total_geral:.2f}")
                        print("============================================")
                        
                        quartos[num_quarto][2] = 'Disponivel'
                        dados[3] = data_saida
                        dados[5] = total_geral
                        
                        print("\n Conta fechada, quarto liberado e histórico salvo com sucesso!")
                        break
                if encontrou == False:
                    print("\n Erro: Quarto não encontrado ou não possui hospedagem ativa!")
                    
                input("\n Tecle <ENTER> para continuar...") 
                
            elif resp2 == '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("============================================")
                print("======  Registrar Consumo/Serviços    ======")
                print("============================================")
                num_quarto = input("# Número do Quarto: ")
                
                encontrou = False
                for codigo_reserva, dados in registro.items():
                    if dados[1] == num_quarto and dados[3] == '':
                        encontrou = True
                        
                        cpf_hospede = dados[0]
                        consumo_atual = dados[4]
                        
                        print(f"\n Hóspede atual: {hospedes[cpf_hospede][0]}")
                        print(f" Consumo atual da conta: R$ {consumo_atual:.2f}")
                        
                        valor_consumo = float(input("\n# Digite o valor do novo consumo (Ex: 15.50): R$ "))
                        dados[4] += valor_consumo
                        
                        print(f"\n Consumo registrado! Novo saldo: R$ {dados[4]:.2f}")
                        break
                
                if encontrou == False:
                    print("\n Erro: Este quarto não possui uma hospedagem ativa.")
                    
                input("\n Tecle <ENTER> para continuar...")

    # MÓDULO RELATÓRIOS 
    elif resp == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("============================================")
        print("======        Módulo Relatórios       ======")
        print("============================================")
        print("----- 1 - Lista Geral de Hóspedes      -----")
        print("----- 2 - Relatório Financeiro         -----")
        print("----- 0 - Retornar ao Menu Principal   -----")
        print("============================================")
        resp2 = input("===== Escolha sua opção: ")
        
        if resp2 == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("============================================")
            print("======      Lista Geral de Hóspedes   ======")
            print("============================================")
            print("##### 1. Maria do Socorro   - CPF: 111.111.111-11")
            print("##### 2. Sansão Toscano  - CPF: 222.222.222-22")
            input("\n Tecle <ENTER> para continuar...")
            
        elif resp2 == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("============================================")
            print("======      Relatório Financeiro      ======")
            print("============================================")
            print("# Taxa de Ocupação Atual: 65%")
            print("# Faturamento Estimado do Mês: R$ 12.450,00")
            input("\n Tecle <ENTER> para continuar...")

    # MÓDULO INFORMAÇÕES
    elif resp == '5':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("============================================")
        print("======            Informações         ======")
        print("============================================")
        print("# Sistema de Gestão para Hotéis e Pousadas")
        print("# Desenvolvido para a Disciplina de Algorítmos e Lógica de Programação, sob orientação do Professor Flavius Gorgônio")
        print("# UFRN 2026")
        print("# Autor: Magdiel Toscano")
        print("============================================")
        input("\n Tecle <ENTER> para continuar...")

    elif resp == '0':
        print("\n Você encerrou o programa. Até logo!")
    else:
        print("\n Opção inválida! Tente novamente.")
        input("\n Tecle <ENTER> para continuar...")
