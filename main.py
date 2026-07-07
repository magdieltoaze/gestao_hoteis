import os
import pickle
from datetime import datetime

from utilidades import limpar_tela_cabecalho
from dados import recupera_hospedes, recupera_quartos, recupera_registro, recupera_proxima_chave, grava_dados_finais
from modulo_quartos import modulo_quartos
from modulo_hospedes import modulo_hospedes 
from modulo_hospedagem import modulo_hospedagem
from modulo_relatorios import modulo_relatorios
from modulo_informacoes import modulo_informacoes

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