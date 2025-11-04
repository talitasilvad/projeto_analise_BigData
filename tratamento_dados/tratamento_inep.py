import pandas as pd
import numpy as np

arquivos_para_processar = [
    ("dados/TX_REND_BRASIL_REGIOES_UFS_2017.xlsx", 
     "arquivos_gerados/inep_2017_tratado.xlsx"),

    ("dados/TX_REND_BRASIL_REGIOES_UFS_2018.xlsx", 
     "arquivos_gerados/inep_2018_tratado.xlsx"),

    ("dados/tx_rend_brasil_regioes_ufs_2019.xlsx", 
     "arquivos_gerados/inep_2019_tratado.xlsx"),

    ("dados/tx_rend_brasil_regioes_ufs_2021.xlsx", 
     "arquivos_gerados/inep_2021_tratado.xlsx"),

    ("dados/tx_rend_brasil_regioes_ufs_2022.xlsx", 
     "arquivos_gerados/inep_2022_tratado.xlsx"),

    ("dados/tx_rend_brasil_regioes_ufs_2023.xlsx", 
     "arquivos_gerados/inep_2023_tratado.xlsx"),
     
    ("dados/tx_rend_brasil_regioes_ufs_2024.xlsx", 
     "arquivos_gerados/inep_2024_tratado.xlsx")
]

# Definindo as colunas pelos seus ÍNDICES (posição)
# Col 0 = Ano (na linha de dados)
# Col 1 = Unidade Geográfica (na linha de dados)
# Col 4 = Taxa Aprov. Fund. Total (código tap_FUN)
# Col 16 = Taxa Aprov. Médio Total (código tap_MED)
# Col 22 = Taxa Reprov. Fund. Total (código tre_FUN)
# Col 34 = Taxa Reprov. Médio Total (código tre_MED)
colunas_indices_para_manter = [0, 1, 4, 16, 22, 34]

renomeando_colunas = [
    'Ano',
    'Unidade_Geografica',
    'Aprovacao_Ensino_Fundamental',
    'Aprovacao_Ensino_Medio',
    'Reprovacao_Ensino_Fundamental',
    'Reprovacao_Ensino_Medio'
]

arquivos_tratados_inep = []

for arquivo_inep, arquivo_tratado in arquivos_para_processar:
    print(f"Processando: {arquivo_inep}...")
    df = pd.read_excel(arquivo_inep, header=None, skiprows=9)

    # Selecionando apenas as colunas pelos ÍNDICES
    # .iloc seleciona por posição: [todas as linhas, colunas da lista]
    df_filtrado = df.iloc[:, colunas_indices_para_manter]
    df_filtrado.columns = renomeando_colunas

    df_tratado = df_filtrado.dropna(how='all')
    df_tratado = df_tratado.replace('--', np.nan)

    df_tratado.to_excel(arquivo_tratado, index=False)
    print(f"Arquivo tratado salvo em: {arquivo_tratado}")
    
    arquivos_tratados_inep.append(arquivo_tratado)

