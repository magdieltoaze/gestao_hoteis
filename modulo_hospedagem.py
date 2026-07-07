from datetime import datetime
from utilidades import limpar_tela_cabecalho, validar_cpf, validar_email, ler_int, ler_float

def modulo_hospedagem(registro, hospedes, quartos, produtos_servicos, proxima_chave):
    op = ''
    while op != '0':
        limpar_tela_cabecalho("Módulo Hospedagem")
        print("----- 1 - Realizar Check-in            -----")
        print("----- 2 - Realizar Check-out           -----")
        print("----- 3 - Registrar Consumo            -----")
        print("----- 4 - Cancelar Reserva             -----")
        print("----- 0 - Retornar ao Menu Principal   -----")
        print("============================================")
        op = input("===== Escolha sua opção: ")
        
        if op == '1':
            limpar_tela_cabecalho("Realizar Check-in")
            cpf = input("# CPF do Hóspede: ")
            
            if cpf in hospedes and hospedes[cpf][3] == True:
                nome_hospede = hospedes[cpf][0]
            
                reserva_encontrada = None
                cod_reserva = None
                for cod, dados in registro.items():
                    if dados[0] == cpf and dados[3] == 'RESERVA':
                        reserva_encontrada = dados
                        cod_reserva = cod
                        break
                
                if reserva_encontrada:
                    quarto_reserva = reserva_encontrada[1]
                    confirma = input(f"\n {nome_hospede} tem uma reserva para o quarto {quarto_reserva}. Confirmar check-in? (S/N): ").strip().upper()
                    
                    if confirma == 'S':
                        quartos[quarto_reserva][2] = 'Ocupado'
                        reserva_encontrada[2] = datetime.now()
                        reserva_encontrada[3] = ''             
                        print(f"\n Check-in da reserva #{cod_reserva} ativado com sucesso no quarto {quarto_reserva}!")
                        input("\n Tecle <ENTER> para continuar...")
                        continue
                    else:
                        print("\n Prosseguindo para um check-in avulso tradicional...")
                
                num_quarto = input("# Número do Quarto: ")
                if num_quarto in quartos:
                    if quartos[num_quarto][2] == 'Disponivel':
                        quartos[num_quarto][2] = 'Ocupado'
                        data_entrada = datetime.now()
                        
                        registro[proxima_chave] = [cpf, num_quarto, data_entrada, '', 0.0, 0.0]
                        
                        print(f"\n Check-in de {nome_hospede} feito com sucesso no quarto {num_quarto}!")
                        print(f" >>> CÓDIGO DO REGISTRO: {proxima_chave} <<<")
                        proxima_chave += 1
                    else:
                        print("\n Erro: Quarto não está disponível!")
                else:
                    print("\n Erro: Quarto não localizado!")
            else:
                print("\n Hóspede não localizado ou inativo!")
            input("\n Tecle <ENTER> para continuar...")
            
        elif op == '2':
            limpar_tela_cabecalho("Realizar Check-out")
            num_quarto = input("# Número do Quarto para fechar conta: ")
            encontrou = False
            for cod, dados in registro.items():
                if dados[1] == num_quarto and dados[3] == '':
                    encontrou = True
                    cpf = dados[0]
                    data_entrada = dados[2]
                    consumo = dados[4]
                    preco_diaria = quartos[num_quarto][1]
                    
                    data_saida = datetime.now()
                    diferenca = data_saida - data_entrada
                    dias = diferenca.days
                    horas_restantes = diferenca.seconds // 3600
                    if horas_restantes > 1 or dias == 0:
                        dias += 1
                    
                    total_diarias = dias * preco_diaria
                    total_geral = total_diarias + consumo
                    
                    print(f"\n===== EXTRATO #{cod} =====")
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

                    hospedes[cpf][3] = False
                    print("\n Check-out finalizado com sucesso! O cliente foi desativado.")
                    break
            if not encontrou:
                print("\n Erro: Nenhuma hospedagem ativa neste quarto.")
            input("\n Tecle <ENTER> para continuar...")
            
        elif op == '3':
            limpar_tela_cabecalho("Registrar Consumo")
            num_quarto = input("# Número do Quarto: ")
            encontrou = False
            for cod, dados in registro.items():
                if dados[1] == num_quarto and dados[3] == '':
                    encontrou = True
                    print(f"\n Hóspede: {hospedes[dados[0]][0]}")
                    print("--- CARDÁPIO DE PRODUTOS/SERVIÇOS ---")
                    for k, v in produtos_servicos.items():
                        print(f" {k} - {v[0]:18} -> R$ {v[1]:.2f}")                    
                    opcao_p = input("\n# Escolha o produto (0 para cancelar): ")
                    if opcao_p in produtos_servicos:
                        qtd = ler_int(f" Quantidade de [{produtos_servicos[opcao_p][0]}]: ")
                        custo_total = produtos_servicos[opcao_p][1] * qtd
                        dados[4] += custo_total  
                        print(f"\n Adicionado! Custo extra de R$ {custo_total:.2f}")
                        print(f" Consumo updated da reserva: R$ {dados[4]:.2f}")
                    break
            if not encontrou:
                print("\n Erro: Quarto sem hospedagem ativa.")
            input("\n Tecle <ENTER> para continuar...")

        elif op == '4':
            limpar_tela_cabecalho("Cancelar Reserva")
            num_quarto = input("# Número do Quarto reservado: ")
            encontrou = False
            for cod, dados in list(registro.items()): 
                if dados[1] == num_quarto and dados[3] == 'RESERVA':
                    encontrou = True
                    cpf = dados[0]
                    confirma = input(f"\n Confirmar cancelamento da reserva de {hospedes[cpf][0]} no quarto {num_quarto}? (S/N): ").strip().upper()
                    if confirma == 'S':
                        quartos[num_quarto][2] = 'Disponivel'
                        del registro[cod]
                        print("\n Reserva cancelada com sucesso! O quarto está disponível novamente.")
                    else:
                        print("\n Operação abortada. A reserva foi mantida.")
                    break
            if not encontrou:
                print("\n Erro: Nenhuma reserva ativa encontrada para este quarto.")
            input("\n Tecle <ENTER> para continuar...")

    return proxima_chave