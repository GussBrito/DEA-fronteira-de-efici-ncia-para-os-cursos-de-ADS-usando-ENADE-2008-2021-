import os
import pandas as pd

BASE = r"C:\Users\brito\OneDrive\Área de Trabalho\Projeto DEA 2025.2\DEA-fronteira-de-efici-ncia-para-os-cursos-de-ADS-usando-ENADE-2008-2021-\todos-os-dados"

cursos_encontrados = set()

for pasta in sorted(os.listdir(BASE)):
    if not pasta.startswith("dados-"):
        continue

    ano = pasta.replace("dados-", "")
    if ano == "2008":
        continue

    caminho_pasta = os.path.join(BASE, pasta)
    print(f"\n📂 Ano {ano}")

    for arquivo in os.listdir(caminho_pasta):
        if not arquivo.endswith(".csv"):
            continue

        caminho_csv = os.path.join(caminho_pasta, arquivo)

        try:
            df = pd.read_csv(
                caminho_csv,
                sep=";",
                encoding="latin1",
                low_memory=False
            )
        except Exception as e:
            print(f"❌ Erro ao ler {arquivo}: {e}")
            continue

        if "CO_CURSO" in df.columns:
            cursos_encontrados.update(df["CO_CURSO"].dropna().unique())

print("\n✅ CURSOS ENCONTRADOS:")
for c in sorted(cursos_encontrados):
    print(c)

print(f"\nTotal de cursos distintos: {len(cursos_encontrados)}")
