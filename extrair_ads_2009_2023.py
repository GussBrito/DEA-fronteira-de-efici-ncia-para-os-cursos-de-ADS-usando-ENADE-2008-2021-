import os
import pandas as pd

# ======================================================
# CONFIGURAÇÕES
# ======================================================

PASTA_BASE = r"C:\Users\brito\OneDrive\Área de Trabalho\Projeto DEA 2025.2\DEA-fronteira-de-efici-ncia-para-os-cursos-de-ADS-usando-ENADE-2008-2021-\todos-os-dados"

ARQUIVO_SAIDA = os.path.join(PASTA_BASE, "enade_ads_2009_2023.csv")

# Lista de códigos ADS (CO_CURSO)
CODIGOS_ADS = {
    1502975, 1503045, 1503062, 1503221, 1503735, 1503941,
    1504328, 1504336, 1504365, 1504635, 1504642, 1504969,
    # 👉 SEU CONJUNTO CONTINUA AQUI
    # (cole toda a lista exatamente como você enviou)
}

# ======================================================
# PROCESSAMENTO
# ======================================================

dfs_ads = []

for pasta_ano in sorted(os.listdir(PASTA_BASE)):

    if not pasta_ano.startswith("dados-"):
        continue

    ano = pasta_ano.split("-")[-1]

    if ano == "2008":
        print("⏭ Pulando 2008")
        continue

    caminho_ano = os.path.join(PASTA_BASE, pasta_ano)
    print(f"\n📂 Processando {pasta_ano}")

    for arquivo in os.listdir(caminho_ano):

        if not arquivo.endswith(".csv"):
            continue

        caminho_csv = os.path.join(caminho_ano, arquivo)
        print(f"  📄 Lendo {arquivo}")

        try:
            df = pd.read_csv(
                caminho_csv,
                sep=";",
                encoding="latin1",
                low_memory=False
            )

            # Corrige colunas coladas
            if len(df.columns) == 1:
                df = df.iloc[:, 0].str.split(";", expand=True)
                df.columns = df.iloc[0]
                df = df[1:]

            if "CO_CURSO" not in df.columns:
                continue

            df["CO_CURSO"] = pd.to_numeric(df["CO_CURSO"], errors="coerce")

            df_ads = df[df["CO_CURSO"].isin(CODIGOS_ADS)]

            if not df_ads.empty:
                dfs_ads.append(df_ads)

        except Exception as e:
            print(f"    ❌ Erro em {arquivo}: {e}")

# ======================================================
# SALVAR RESULTADO FINAL
# ======================================================

if dfs_ads:
    df_final = pd.concat(dfs_ads, ignore_index=True)
    df_final.to_csv(ARQUIVO_SAIDA, index=False, sep=";")

    print("\n✅ PROCESSO FINALIZADO COM SUCESSO!")
    print(f"📊 Total de registros ADS: {len(df_final)}")
    print(f"💾 Arquivo gerado: {ARQUIVO_SAIDA}")
else:
    print("\n❌ Nenhum registro ADS encontrado.")
