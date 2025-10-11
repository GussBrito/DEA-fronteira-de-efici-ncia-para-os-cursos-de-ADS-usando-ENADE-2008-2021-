import os
import csv

# Caminho da pasta com os arquivos .txt
pasta = r"C:\Users\brito\OneDrive\Área de Trabalho\Projeto DEA 2025.2\DEA-fronteira-de-efici-ncia-para-os-cursos-de-ADS-usando-ENADE-2008-2021-/"

# Cria a pasta de saída (opcional)
pasta_saida = os.path.join(pasta, "convertidos_csv")
os.makedirs(pasta_saida, exist_ok=True)

# Percorre todos os arquivos da pasta
for nome_arquivo in os.listdir(pasta):
    if nome_arquivo.endswith(".txt"):
        caminho_txt = os.path.join(pasta, nome_arquivo)
        caminho_csv = os.path.join(pasta_saida, nome_arquivo.replace(".txt", ".csv"))

        # Lê o conteúdo do arquivo .txt
        with open(caminho_txt, "r", encoding="utf-8") as txt_file:
            linhas = txt_file.readlines()

        # Divide as linhas por espaços (ajuste aqui se for vírgula, ponto e vírgula, etc.)
        dados = [linha.strip().split() for linha in linhas]

        # Escreve o conteúdo em formato CSV
        with open(caminho_csv, "w", newline="", encoding="utf-8") as csv_file:
            escritor = csv.writer(csv_file)
            escritor.writerows(dados)

        print(f"✅ Convertido: {nome_arquivo} → {os.path.basename(caminho_csv)}")

print("\nConversão concluída!")
