from datetime import datetime
from utilidades import limpar_tela_cabecalho, validar_cpf, validar_email, apenas_numeros

def modulo_hospedes(hospedes, quartos, registro, proxima_chave):
    op = ''
    while op != '0':
        limpar_tela_cabecalho("Módulo Hóspedes")
        print("----- 1 - Cadastrar Hóspede            -----")
        print("----- 2 - Exibir Dados do Hóspede      -----")
        print("----- 3 - Alterar Dados do Hóspede     -----")
        print("----- 4 - Inativar Hóspede             -----")
        print("----- 0 - Retornar ao Menu Principal   -----")
        print("============================================")
        op = input("===== Escolha sua opção: ")
        
        if op == '1':
            limpar_tela_cabecalho("Cadastrar Hóspede")
            while True:
                cpf = input("# CPF (Apenas 11 números): ").strip()
                if not validar_cpf(cpf):
                    print("\n Erro: CPF inválido!")
                elif cpf in hospedes and hospedes[cpf][3] == True:
                    print("\n Erro: Este CPF já está ativo no sistema!")
                else:
                    break
                if input(" Deseja tentar novamente? (S/N): ").strip().upper() != 'S':
                    cpf = None
                    break
            
            if cpf is not None:
                atualizar_dados = True
                nome = None
                
                if cpf in hospedes:
                    nome_salvo = hospedes[cpf][0]
                    print(f"\n Um cliente com esse CPF foi encontrado: {nome_salvo}")
                    resposta = input(f" Deseja continuar como {nome_salvo}? (S/N): ").strip().upper()
                    if resposta == 'S':
                        hospedes[cpf][3] = True
                        print(f"\n Cliente {nome_salvo} bem-vindo(a) de volta!")
                        nome = nome_salvo
                        atualizar_dados = False
                    else:
                        print("\n Insira os novos dados para atualizar o cadastro deste CPF:")
                
                if atualizar_dados:
                    nome_input = input("# Nome do hóspede: ")
                    while True:
                        email = input("# Email: ")
                        if validar_email(email):
                            break
                        print("\n Erro: Email inválido!")
                        if input(" Deseja tentar novamente? (S/N): ").strip().upper() != 'S':
                            email = None
                            break
                            
                    if email is not None:
                        while True:
                            numero = input("# Telefone (Apenas números): ")
                            if apenas_numeros(numero):
                                break
                            print("\n Erro: Telefone deve conter apenas números!")
                            if input(" Deseja tentar novamente? (S/N): ").strip().upper() != 'S':
                                numero = None
                                break
                                
                        if numero is not None:
                            hospedes[cpf] = [nome_input, email, numero, True]
                            nome = nome_input
                            print(f"\n Hóspede {nome} cadastrado com sucesso!")
                
                # --- Prosseguir do registro direto para o checkin ou reserva ---
                if nome is not None:
                    print(f"\n O que deseja fazer a seguir para {nome}?")
                    print(" 1 - Ir direto para o Check-in")
                    print(" 2 - Fazer reserva")
                    print(" 0 - Voltar ao menu")
                    acao = input(" Escolha: ").strip()
                    
                    if acao == '1':
                        num_quarto = input(" # Número do Quarto: ")
                        if num_quarto in quartos:
                            if quartos[num_quarto][2] == 'Disponivel':
                                quartos[num_quarto][2] = 'Ocupado'
                                data_entrada = datetime.now()
                                registro[proxima_chave] = [cpf, num_quarto, data_entrada, '', 0.0, 0.0]
                                
                                print(f"\n Check-in de {nome} feito no quarto {num_quarto}!")
                                print(f" >>> CÓDIGO DO REGISTRO: {proxima_chave} <<<")
                                proxima_chave += 1
                            else:
                                print("\n Erro: Quarto não está disponível!")
                        else:
                            print("\n Erro: Quarto não localizado!")
                            
                    elif acao == '2':
                        num_quarto = input(" # Número do Quarto para Reserva: ")
                        if num_quarto in quartos:
                            if quartos[num_quarto][2] == 'Disponivel':
                                data_str = input(" # Data da Reserva (DD/MM/AAAA): ")
                                try:
                                    dia, mes, ano = map(int, data_str.split('/'))
                                    data_reserva = datetime(ano, mes, dia, 14, 0)
                                    
                                    quartos[num_quarto][2] = 'Reservado'
                                    registro[proxima_chave] = [cpf, num_quarto, data_reserva, 'RESERVA', 0.0, 0.0]
                                    
                                    print(f"\n Reserva de {nome} realizada para o quarto {num_quarto} em {data_str}!")
                                    print(f" >>> CÓDIGO DA RESERVA: {proxima_chave} <<<")
                                    proxima_chave += 1
                                except ValueError:
                                    print("\n Erro: Data em formato inválido! Use DD/MM/AAAA.")
                            else:
                                print("\n Erro: Quarto não está disponível para reserva!")
                        else:
                            print("\n Erro: Quarto não localizado!")
                            
            input("\n Tecle <ENTER> para continuar...")
            
        elif op == '2':
            limpar_tela_cabecalho("Exibir Dados")
            cpf = input("# Digite o CPF do hóspede: ")
            if cpf in hospedes and hospedes[cpf][3] == True:
                print(f"\n # CPF: {cpf}")
                print(f"# Nome: {hospedes[cpf][0]}")
                print(f"# Email: {hospedes[cpf][1]}")
                print(f"# Telefone: {hospedes[cpf][2]}")
                print(f"# Status no Sistema: ATIVO")
            else:
                print("\n Hóspede não encontrado ou inativo!")
            input("\n Tecle <ENTER> para continuar...")
            
        elif op == '3':
            limpar_tela_cabecalho("Alterar Dados")
            cpf = input("# Digite o CPF do hóspede: ")
            if cpf in hospedes and hospedes[cpf][3] == True:
                print(f"\n Alterando os dados de: {hospedes[cpf][0]}")
                nome = input("# Novo Nome: ")
                email = input("# Novo Email: ")
                if not validar_email(email):
                    print("\n Erro: Email inválido!")
                else:
                    numero = input("# Novo Telefone: ")
                    if not apenas_numeros(numero):
                        print("\n Erro: Telefone inválido!")
                    else:
                        hospedes[cpf] = [nome, email, numero, True]
                        print("\n Dados updated com sucesso!")
            else:
                print("\n Hóspede não encontrado!")
            input("\n Tecle <ENTER> para continuar...")
            
        elif op == '4':
            limpar_tela_cabecalho("Inativar Hóspede")
            cpf = input("# Digite o CPF para INATIVAR: ")
            if cpf in hospedes and hospedes[cpf][3] == True:
                hospedes[cpf][3] = False
                print(f"\n Hóspede {hospedes[cpf][0]} foi desativado do sistema!")
            else:
                print("\n Hóspede não encontrado ou já está inativo!")
            input("\n Tecle <ENTER> para continuar...")
            
    return proxima_chave