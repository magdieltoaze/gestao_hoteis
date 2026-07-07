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
