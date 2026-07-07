from datetime import datetime
from utilidades import limpar_tela_cabecalho, validar_cpf, validar_email, ler_int, ler_float

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