import pandas as pd

arquivos_tic_kids = [
    ("dados/tic_kids_online_brasil_2017_criancas_base_de_microdados_v1.0.csv",
     "dados/tic_kids_online_brasil_2017_criancas_dicionario_de_variaveis_v1.0.xlsx",
     "arquivos_gerados/tic_kids_2017_tratado.xlsx"),

    ("dados/tic_kids_online_brasil_2018_criancas_base_de_microdados_v1.0.csv",
     "dados/tic_kids_online_brasil_2018_criancas_dicionario_de_variaveis_v1.0.xlsx",
     "arquivos_gerados/tic_kids_2018_tratado.xlsx"),

    ("dados/tic_kids_online_brasil_2019_criancas_base_de_microdados_v1.1.csv",
     "dados/tic_kids_online_brasil_2019_criancas_dicionario_de_variaveis_v1.0.xlsx",
     "arquivos_gerados/tic_kids_2019_tratado.xlsx"),

    ("dados/tic_kids_online_brasil_2021_base_de_microdados_v1.0.csv",
     "dados/tic_kids_online_brasil_2021_dicionario_de_variaveis_v1.0.xlsx",
     "arquivos_gerados/tic_kids_2021_tratado.xlsx"),

    ("dados/tic_kids_online_brasil_2022_base_de_microdados_v1.0.csv",
     "dados/tic_kids_online_brasil_2022_dicionario_de_variaveis_v1.0.xlsx",
     "arquivos_gerados/tic_kids_2022_tratado.xlsx"),

    ("dados/tic_kids_online_brasil_2023_base_de_microdados_v1.0.csv",
     "dados/tic_kids_online_brasil_2023_dicionario_de_variaveis_v1.0.xlsx",
     "arquivos_gerados/tic_kids_2023_tratado.xlsx"),

    ("dados/tic_kids_online_brasil_2024_base_de_microdados_v1.2.csv",
     "dados/tic_kids_online_brasil_2024_dicionario_de_variaveis_v1.1.xlsx",
     "arquivos_gerados/tic_kids_2024_tratado.xlsx")
]

# ID_variável no dicionário
variaveis_importantes = [
    "ESC1", "FAIXA_ETARIA", "COD_REGIAO_2", "M7A_B", "N1_C", "N2_C", "N1_H", "N2_H", "T12_D", "N1_G1","N2_G", "N2_G1"   
]

for arquivo_microdados, arquivo_dicionario, arquivo_final_gerado in arquivos_tic_kids:

    print("Lendo os arquivos...")
    df_dicionario = pd.read_excel(arquivo_dicionario, header=1)
    df_dados = pd.read_csv(arquivo_microdados, sep=";", encoding="latin-1", low_memory=False)

    df_dicionario.columns = df_dicionario.columns.str.strip()
    mapeamento = df_dicionario.set_index("ID_variável")["Descrição da variável"].to_dict()

    colunas_existentes = [id_variavel for id_variavel in variaveis_importantes if id_variavel in df_dados.columns]
    df_dados_filtrados = df_dados[colunas_existentes].copy()    

    print("Iniciando a tradução das respostas...")
    for coluna in df_dados_filtrados.columns:
        info_var = df_dicionario[df_dicionario["ID_variável"] == coluna]

        if not info_var.empty:
            conj_legenda = info_var["Código e rótulo da variável"].iloc[0]
            tradutor = {}
            if pd.notna(conj_legenda):
                for cond_legenda in conj_legenda.split("\n"):
                    if "=" in cond_legenda:
                        valor_numerico, texto = cond_legenda.split("=",1)
                        tradutor[int(valor_numerico.strip())] = texto.strip().strip('“”"')
            if tradutor:
                df_dados_filtrados[coluna] = df_dados_filtrados[coluna].replace(tradutor)

    df_dados_renomeados = df_dados_filtrados.rename(columns=mapeamento)
    df_dados_renomeados.to_excel(arquivo_final_gerado, index=False)
    print(f"Arquivo salvo: {arquivo_final_gerado}")