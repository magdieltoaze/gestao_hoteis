import os
import pickle
from datetime import datetime

def recupera_hospedes():
    try:
        arq_hospedes = open("hospedes.dat", "rb")
        hospedes = pickle.load(arq_hospedes)
        arq_hospedes.close()
    except:
        hospedes = {
            '11111111111': ['Mortícia Addams', 'morto@email.com', '84999999991', True],
            '22222222222': ['Gomez Addams', 'gomez@email.com', '84999999992', True],
            '33333333333': ['Vandinha Addams', 'vandinha@email.com', '84999999993', True]
        }
        arq_hospedes = open("hospedes.dat", "wb")
        pickle.dump(hospedes, arq_hospedes)
        arq_hospedes.close()
    return hospedes


def recupera_quartos():
    try:
        arq_quartos = open("quartos.dat", "rb")
        quartos = pickle.load(arq_quartos)
        arq_quartos.close()
    except:
        quartos = {
            '101': ['Solteiro', 150.00, 'Disponivel'],
            '102': ['Casal', 250.00, 'Ocupado'],
            '103': ['Luxo', 400.00, 'Manutencao'],
            '104': ['Solteiro', 150.00, 'Ocupado']
        }
        arq_quartos = open("quartos.dat", "wb")
        pickle.dump(quartos, arq_quartos)
        arq_quartos.close()
    return quartos


def recupera_registro():
    try:
        arq_registro = open("registro.dat", "rb")
        registro = pickle.load(arq_registro)
        arq_registro.close()
    except:
        registro = {
            1001: ['22222222222', '102', datetime(2026, 6, 5, 14, 30), '', 45.50, 0.0]
        }
        arq_registro = open("registro.dat", "wb")
        pickle.dump(registro, arq_registro)
        arq_registro.close()
    return registro


def recupera_proxima_chave():
    try:
        arq_config = open("config.dat", "rb")
        chave = pickle.load(arq_config)
        arq_config.close()
    except:
        chave = 1002
        arq_config = open("config.dat", "wb")
        pickle.dump(chave, arq_config)
        arq_config.close()
    return chave


def grava_dados_finais(hospedes, quartos, registro, chave):
    with open("hospedes.dat", "wb") as f:
        pickle.dump(hospedes, f)
    with open("quartos.dat", "wb") as f:
        pickle.dump(quartos, f)
    with open("registro.dat", "wb") as f:
        pickle.dump(registro, f)
    with open("config.dat", "wb") as f:
        pickle.dump(chave, f)


# ==========================================================
# FUNÇÕES DE VALIDAÇÃO
# ==========================================================

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


# ==========================================================
# MÓDULOS
# ==========================================================

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
                elif cpf in hospedes and hospedes[cpf][3]:
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
            if cpf in hospedes and hospedes[cpf][3]:
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
            if cpf in hospedes and hospedes[cpf][3]:
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
            if cpf in hospedes and hospedes[cpf][3]:
                hospedes[cpf][3] = False
                print(f"\n Hóspede {hospedes[cpf][0]} foi desativado do sistema!")
            else:
                print("\n Hóspede não encontrado ou já está inativo!")
            input("\n Tecle <ENTER> para continuar...")
            
    return proxima_chave


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
            if cpf in hospedes and hospedes[cpf][3]:
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


def modulo_relatorios(registro, hospedes, quartos, produtos_servicos):
    op = ''
    while op != '0':
        limpar_tela_cabecalho("Módulo Relatórios")
        print("----- 1 - Lista Geral de Hóspedes Ativos-----")
        print("----- 2 - Ocupação e Mapa de Quartos    -----")
        print("----- 3 - Tabela de Produtos/Serviços   -----")
        print("----- 4 - Painel Financeiro Comparativo -----")
        print("----- 0 - Retornar ao Menu Principal    -----")
        print("============================================")
        op = input("===== Escolha sua opção: ")
        
        if op == '1':
            limpar_tela_cabecalho("Hóspedes Ativos")
            existe = False
            print(f"{'NOME':<22} | {'CPF':<15} | {'QUARTO ATUAL':<15}")
            print("-" * 58)
            
            for c, d in hospedes.items():
                if d[3] == True:
                    nome = d[0]
                    quarto_hospedado = "Não Hospedado"
                    for cod, dados in registro.items():
                        if dados[0] == c and dados[3] == '':
                            quarto_hospedado = f"Quarto {dados[1]}"
                            break
                    print(f" -> {nome:<20} | CPF: {c} | {quarto_hospedado}")
                    existe = True
                    
            if not existe: 
                print("Nenhum hóspede ativo cadastrado.")
            input("\n Tecle <ENTER> para continuar...")
            
        elif op == '2':
            limpar_tela_cabecalho("Mapa de Quartos")
            disponiveis, ocupados, manutencao, reservados = [], [], [], []
            for num, dados in quartos.items():
                texto = f"Quarto {num} ({dados[0]}) - R$ {dados[1]:.2f}"
                if dados[2] == 'Disponivel': disponiveis.append(texto)
                elif dados[2] == 'Ocupado': ocupados.append(texto)
                elif dados[2] == 'Reservado': reservados.append(texto)
                else: manutencao.append(texto)
            
            print("--- DISPONÍVEIS ---")
            for q in disponiveis: print(f" [🟢] {q}")
            print("\n--- OCUPADOS ---")
            for q in ocupados: print(f" [🔴] {q}")
            print("\n--- RESERVADOS ---")
            for q in reservados: print(f" [🔵] {q}")
            print("\n--- EM MANUTENÇÃO ---")
            for q in manutencao: print(f" [🟡] {q}")
            input("\n Tecle <ENTER> para continuar...")
            
        elif op == '3':
            limpar_tela_cabecalho("Produtos do Hotel")
            for k, v in produtos_servicos.items():
                print(f" Cód {k}: {v[0]:18} -> R$ {v[1]:.2f}")
            input("\n Tecle <ENTER> para continuar...")
            
        elif op == '4':
            limpar_tela_cabecalho("Painel Financeiro")
            agora = datetime.now()
            fat_semana, fat_mes, fat_trimestre, fat_semestre, fat_ano = 0.0, 0.0, 0.0, 0.0, 0.0
            
            for cod, dados in registro.items():
                if dados[3] != '' and dados[3] != 'RESERVA':
                    dt_saida = dados[3]
                    valor = dados[5]
                    diferenca = agora - dt_saida
                    
                    if diferenca.days <= 7: fat_semana += valor
                    if diferenca.days <= 30: fat_mes += valor
                    if diferenca.days <= 90: fat_trimestre += valor
                    if diferenca.days <= 180: fat_semestre += valor
                    if diferenca.days <= 365: fat_ano += valor
            
            print(f"💰 Faturamento da Semana (7 dias):   R$ {fat_semana:.2f}")
            print(f"💰 Faturamento do Mês (30 dias):     R$ {fat_mes:.2f}")
            print(f"💰 Faturamento do Trimestre (90d):   R$ {fat_trimestre:.2f}")
            print(f"💰 Faturamento do Semestre (180d):  R$ {fat_semestre:.2f}")
            print(f"💰 Faturamento do Ano (365 dias):    R$ {fat_ano:.2f}")
            print("--------------------------------------------")
            print("📊 COMPARATIVO DE PERFORMANCE:")
            if fat_ano > 0:
                print(f" Mês representa {(fat_mes/fat_ano)*100:.1f}% do faturamento anual.")
            else:
                print(" Sem dados suficientes para percentuais comparativos ainda.")
            input("\n Tecle <ENTER> para continuar...")


def modulo_informacoes():
    limpar_tela_cabecalho("Informações")
    print("# Sistema de Gestão para Hotéis e Pousadas")
    print("# Desenvolvido para a Disciplina de Algorítmos e Lógica de Programação")
    print("# UFRN 2026 - Padrão de Armazenamento por Listas.")
    print("# Autor: Magdiel Toscano")
    print("============================================")
    input("\n Tecle <ENTER> para continuar...")

hospedes = recupera_hospedes()
quartos = recupera_quartos()
registro = recupera_registro()
proxima_chave_reserva = recupera_proxima_chave()

produtos_servicos = {
    '1': ['Água Mineral', 5.00],
    '2': ['Refrigerante', 8.00],
    '3': ['Cerveja', 10.00],
    '4': ['Petisco/Porção', 35.00],
    '5': ['Lavanderia (Peça)', 15.00]
}

resp = ''
while resp != '0': 
    limpar_tela_cabecalho("GESTÃO DE HOTEIS")
    print("----- 1 - Módulo Hóspedes              -----")
    print("----- 2 - Módulo Quartos               -----")
    print("----- 3 - Módulo Hospedagem            -----")
    print("----- 4 - Módulo Relatórios            -----")
    print("----- 5 - Módulo Informações           -----")
    print("----- 0 - Sair                         -----")
    print("============================================")
    resp = input("===== Escolha sua opção: ")
    
    if resp == '1':
        proxima_chave_reserva = modulo_hospedes(hospedes, quartos, registro, proxima_chave_reserva)
    elif resp == '2':
        modulo_quartos(quartos)
    elif resp == '3':
        proxima_chave_reserva = modulo_hospedagem(registro, hospedes, quartos, produtos_servicos, proxima_chave_reserva)
    elif resp == '4':
        modulo_relatorios(registro, hospedes, quartos, produtos_servicos)
    elif resp == '5':
        modulo_informacoes()

limpar_tela_cabecalho("Sair")
print("\n Salvando os Dados...")
grava_dados_finais(hospedes, quartos, registro, proxima_chave_reserva)
print(" Sincronização concluída com sucesso. Até breve!")
print()
input("Tecle <ENTER> para fechar a aplicação...")
