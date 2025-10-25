import pandas as pd

pasta_arquivos = "arquivos_gerados/dados_tic_kids_geral.csv"

arquivos_tic_kids =[
    ("arquivos_gerados/tic_kids_2017_tratado.xlsx", 2017),
    ("arquivos_gerados/tic_kids_2018_tratado.xlsx", 2018),
    ("arquivos_gerados/tic_kids_2019_tratado.xlsx", 2019),
    ("arquivos_gerados/tic_kids_2021_tratado.xlsx", 2021),
    ("arquivos_gerados/tic_kids_2022_tratado.xlsx", 2022),
    ("arquivos_gerados/tic_kids_2023_tratado.xlsx", 2023),
    ("arquivos_gerados/tic_kids_2024_tratado.xlsx", 2024)
]

lista_dataframes = []

for arquivo, ano in arquivos_tic_kids:
    df_ano = pd.read_excel(arquivo)
    df_ano["Ano"] = ano
    lista_dataframes.append(df_ano)

df_final = pd.concat(lista_dataframes, ignore_index=True)

df_final.to_csv(pasta_arquivos, index=False, encoding="utf-8-sig")
print(f"Arquivo salvo: {pasta_arquivos}")