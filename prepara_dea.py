import pandas as pd
import os

pasta_dados = r"C:\Users\brito\OneDrive\Área de Trabalho\Projeto DEA 2025.2\DEA-fronteira-de-efici-ncia-para-os-cursos-de-ADS-usando-ENADE-2008-2021-\todos-os-dados"
arquivo_original = os.path.join(pasta_dados, "enade_ads_2009_2023.csv")

df = pd.read_csv(arquivo_original, sep=";", decimal=".", low_memory=False)

# Ver quais colunas numéricas têm dados
colunas_numericas = ['CO_CATEGAD', 'CO_ORGACAD', 'CO_TURNO_GRADUACAO', 'NT_GER', 'NT_FG', 'NT_CE']
for col in colunas_numericas:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        print(f"{col}: {df[col].notna().sum()} valores")

# Filtrar só linhas com pelo menos CO_CATEGAD (que deve ter dados)
df_com_dados = df.dropna(subset=['CO_CATEGAD'])

print(f"\nLinhas com CO_CATEGAD: {len(df_com_dados)}")

# Agrupar por curso-ano usando só o que tem dados
group_cols = ["NU_ANO", "CO_IES", "CO_CURSO"]
dea_df = df_com_dados.groupby(group_cols).agg(
    n_alunos=("CO_CATEGAD", "count"),        # número de alunos
    categoria_media=("CO_CATEGAD", "mean"),   # categoria da IES
    orgacad_media=("CO_ORGACAD", "mean"),     # organização
    turno_media=("CO_TURNO_GRADUACAO", "mean") # turno
).reset_index()

dea_df.to_csv("enade_ads_dea_final.csv", index=False)
print("\n✅ enade_ads_dea_final.csv criado!")
print(dea_df.head(10))
print(f"Total de DMUs (cursos-ano): {len(dea_df)}")
