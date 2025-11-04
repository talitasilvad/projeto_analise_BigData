import pandas as pd

def unir_arquivos(lista_arquivos, pasta_arquivos, tipo_dados, salvar_como):
    lista_dataframes = []

    if tipo_dados == "tic_kids":
        for arquivo, ano in lista_arquivos:
            df = pd.read_excel(arquivo)
            df["Ano"] = ano
            lista_dataframes.append(df)
    else:
        for arquivo in lista_arquivos:
            df = pd.read_excel(arquivo)
            lista_dataframes.append(df)

    df_final = pd.concat(lista_dataframes, ignore_index=True)
    if salvar_como == "csv":
        df_final.to_csv(pasta_arquivos, index=False, encoding="utf-8-sig")
    else:
        df_final.to_excel(pasta_arquivos, index=False)        


    print(f"Arquivo salvo: {pasta_arquivos}")

arquivos_tic_kids =[
    ("arquivos_gerados/tic_kids_2017_tratado.xlsx", 2017),
    ("arquivos_gerados/tic_kids_2018_tratado.xlsx", 2018),
    ("arquivos_gerados/tic_kids_2019_tratado.xlsx", 2019),
    ("arquivos_gerados/tic_kids_2021_tratado.xlsx", 2021),
    ("arquivos_gerados/tic_kids_2022_tratado.xlsx", 2022),
    ("arquivos_gerados/tic_kids_2023_tratado.xlsx", 2023),
    ("arquivos_gerados/tic_kids_2024_tratado.xlsx", 2024)
]

arquivos_inep = [
    "arquivos_gerados/inep_2017_tratado.xlsx",
    "arquivos_gerados/inep_2018_tratado.xlsx",
    "arquivos_gerados/inep_2019_tratado.xlsx",
    "arquivos_gerados/inep_2021_tratado.xlsx",
    "arquivos_gerados/inep_2022_tratado.xlsx",
    "arquivos_gerados/inep_2023_tratado.xlsx",
    "arquivos_gerados/inep_2024_tratado.xlsx"

]

unir_arquivos(arquivos_tic_kids, "arquivos_gerados/dados_tic_kids_geral_csv.csv", tipo_dados="tic_kids", salvar_como="csv" )

unir_arquivos(arquivos_inep, "arquivos_gerados/dados_inep_geral_csv.csv", tipo_dados="inep", salvar_como="csv" )