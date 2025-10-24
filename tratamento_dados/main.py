import pandas as pd

arquivo_microdados = "dados/tic_kids_online_brasil_2017_criancas_base_de_microdados_v1.0.csv"
arquivo_dicionario = "dados/tic_kids_online_brasil_2017_criancas_dicionario_de_variaveis_v1.0.xlsx"

ANO = 2017
arquivo_final_gerado = f"arquivos_gerados/tic_kids_{ANO}_tratado.xlsx"

print("Lendo os arquivos...")
df_dicionario = pd.read_excel(arquivo_dicionario, header=1)
df_dados = pd.read_csv(arquivo_microdados, sep=";", encoding="latin-1", low_memory=False)

# ID_variável no dicionário
variaveis_importantes = [
    "ESC1", "M7A_B", "N1_C", "N2_C", "N1_H", "N2_H", "T12_D", "N1_G1","N2_G", "N2_G1"
    # "M1B_D","M2","M5", 
    # "O1_D", "O1_A", "O1_B", "O1_E" 
    # "O6_A","O6_B","O6_C","O6_D","O6_E","O6_F","O6_G",
    # "P5_H", 
    # "T12_E","T12_A"
]

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
                    tradutor[int(valor_numerico.strip())] = texto.strip().strip('""')
        if tradutor:
            df_dados_filtrados[coluna] = df_dados_filtrados[coluna].replace(tradutor)

df_dados_renomeados = df_dados_filtrados.rename(columns=mapeamento)
df_dados_renomeados.to_excel(arquivo_final_gerado, index=False)
print(f"Arquivo salvo: {arquivo_final_gerado}")