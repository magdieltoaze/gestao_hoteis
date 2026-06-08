import os

# CPF como registro principal: [Nome, Email, Telefone]
hospedes = {
    '11111111111': ['Maria do Socorro', 'maria@email.com', '(84) 99999-9999'],
    '22222222222': ['Sansão Toscano', 'sansao@email.com', '(84) 88888-8888']
}

# Numero do quato como registro principal: [Tipo, Preço, Status]
quartos = {
    '101': ['Solteiro', '150.00', 'Disponivel'],
    '102': ['Casal', '250.00', 'Ocupado'],
    '103': ['Luxo', '400.00', 'Manutenção']
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
                    print("\n Dados updated com sucesso!")
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
                        print(f"\n Check-in de {hospedes[cpf][0]} realizado com sucesso no quarto {num_quarto}!")
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
                num_quarto = input("##### Número do Quarto para fechar conta: ")
                
                if num_quarto in quartos:
                    if quartos[num_quarto][2] == 'Ocupado':
                        quartos[num_quarto][2] = 'Disponivel'
                        print(f"\n Quarto {num_quarto} liberado com sucesso! Conta fechada.")
                    else:
                        print("\n Esse quarto já está desocupado.")
                else:
                    print("\n Quarto não encontrado!")
                input("\n Tecle <ENTER> para continuar...")  
            elif resp2 == '3':
                print("\n Módulo de consumo programado para a próxima etapa...")
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
            
        elif resp2 == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("============================================")
            print("======      Relatório Financeiro      ======")
            print("============================================")
            print("# Taxa de Ocupação Atual: 65%")
            print("# Faturamento Estimado do Mês: R$ 12.450,00")
            

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
