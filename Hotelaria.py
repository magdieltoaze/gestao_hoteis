import os

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
    
    if resp == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("============================================")
        print("======          Módulo Hóspedes       ======")
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
            nome = input("##### Nome do hóspede: ")
            cpf = input("##### CPF: ")
            numero = input("##### Telefone: ")
            email = input("##### Email: ")
            print("\n Hóspede cadastrado com sucesso!")
            
        elif resp2 == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("============================================")
            print("======      Exibir Dados do Hóspede   ======")
            print("============================================")
            cpf = input("##### Digite o CPF do hóspede para busca: ")
            print(f"\n ##### CPF: {cpf}")
            print("##### Nome: Maria do Socorro")
            print("##### Telefone: (84) 99999-9999")
            
        elif resp2 == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("============================================")
            print("======      Alterar Dados do Hóspede  ======")
            print("============================================")
            cpf = input("##### Digite o CPF do hóspede: ")
            print("\n Dados atualizados com sucesso!")
            
        elif resp2 == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("============================================")
            print("======        Excluir Hóspede         ======")
            print("============================================")
            cpf = input("##### Digite o CPF do hóspede para excluir: ")
            print("\n Hóspede removido do sistema!")
            
        input("\n Tecle <ENTER> para continuar...")

    elif resp == '2':
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
            print("======       Cadastrar Novo Quarto    ======")
            print("============================================")
            num = input("##### Número do Quarto: ")
            tipo = input("##### Tipo (Solteiro/Casal/Luxo): ")
            print("\n Quarto cadastrado!")
            
        elif resp2 == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("============================================")
            print("======    Disponibilidade de Quartos  ======")
            print("============================================")
            print("##### Quarto 101 - [Disponível] - R$ 150,00")
            print("##### Quarto 102 - [Ocupado]    - R$ 250,00")
            print("##### Quarto 103 - [Manutenção] - R$ 150,00")
            
        elif resp2 == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("============================================")
            print("======     Alterar Preço da Diária    ======")
            print("============================================")
            num = input("##### Número do Quarto: ")
            preco = input("##### Novo valor da diária: R$ ")
            print("\n Preço atualizado!")
            
        input("\n Tecle <ENTER> para continuar...")

    elif resp == '3':
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
            print("======          Realizar Check-in      ======")
            print("============================================")
            cpf = input("##### CPF do Hóspede: ")
            quarto = input("##### Número do Quarto Escolhido: ")
            dias = input("##### Quantidade de diárias planejadas: ")
            print("\n Check-in realizado! Quarto Ocupado.")
            
        elif resp2 == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("============================================")
            print("======        Realizar Check-out      ======")
            print("============================================")
            quarto = input("##### Número do Quarto fechando conta: ")
            print("\n ##### Consumo extra lançado: R$ 45,00")
            print("##### Total da estadia: R$ 345,00")
            print("\n Pagamento efetuado e quarto liberado!")
            
        elif resp2 == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("============================================")
            print("======   Registrar Consumo/Serviços   ======")
            print("============================================")
            quarto = input("##### Número do Quarto: ")
            item = input("##### Item consumido (Serviço): ")
            print("\n Valor adicionado à conta do quarto!")
            
        input("\n Tecle <ENTER> para continuar...")

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
            print("##### Taxa de Ocupação Atual: 65%")
            print("##### Faturamento Estimado do Mês: R$ 12.450,00")
            
        input("\n Tecle <ENTER> para continuar...")

    elif resp == '5':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("============================================")
        print("======            Informações         ======")
        print("============================================")
        print("##### Sistema de Gestão para Hotéis e Pousadas")
        print("##### Desenvolvido para a Disciplina de Algorítmos e Lógica de Programação, sob orientação do Professor Flavius Gorgônio)
        print("#####")
        print("##### Autor: Magdiel Toscano")
        print("============================================")
        input("\n Tecle <ENTER> para continuar...")

    elif resp == '0':
        print("\n Você encerrou o programa. Até logo!")
    else:
        print("\n Opção inválida! Tente novamente.")
        input("\n Tecle <ENTER> para continuar...")
