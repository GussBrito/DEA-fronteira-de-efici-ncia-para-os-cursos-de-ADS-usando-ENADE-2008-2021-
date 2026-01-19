import pandas as pd
import numpy as np

# Carregar dados
df = pd.read_csv("pronto_para_dea.csv")
print(f"Carregou {len(df)} cursos")

# Preparar matrizes
X = df[['n_alunos', 'categoria_media', 'orgacad_media']].fillna(1).values  # Inputs
Y = df[['n_alunos']].fillna(1).values                                    # Outputs

print("Matrizes preparadas!")

# DEA manual simples (sem biblioteca externa)
def dea_simples(X, Y):
    n = X.shape[0]  # número de DMUs
    eficiencia = np.ones(n)  # inicia com 1.0
    
    for i in range(n):
        # Para cada DMU, verifica se outra é melhor
        for j in range(n):
            if j != i:
                # Se outra DMU usa menos input mas produz mais
                if np.all(X[j] <= X[i]) and np.any(X[j] < X[i]) and Y[j] >= Y[i]:
                    eficiencia[i] = 0.8  # ineficiente
                    break
    return eficiencia

# Rodar
eficiencias = dea_simples(X, Y)
df['eficiencia'] = eficiencias

# Resultados
print("\n🏆 RESULTADO DEA - EFICIÊNCIA:")
resultado = df[['NU_ANO', 'CO_IES', 'CO_CURSO', 'n_alunos', 'eficiencia']].sort_values('eficiencia', ascending=False)
print(resultado)
df.to_csv("resultados_dea_manual.csv", index=False)
print("\n✅ Salvo em resultados_dea_manual.csv")
