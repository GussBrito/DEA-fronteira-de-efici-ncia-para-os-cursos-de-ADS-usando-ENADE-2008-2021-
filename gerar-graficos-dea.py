import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("resultados_dea_manual.csv")

# Mapa com nomes reais (ajuste se souber os nomes exatos)
nome_ies = {
    124: "UNIARA (SP)",
    757: "IFPB (PB)", 
    1732: "UNIPAC (MG)",
    206: "Fac. Ciências Médicas",
    13663: "UniRV",
    83: "CESMAC",
    2632: "UniFCV"
}

df['nome'] = df['CO_IES'].map(nome_ies).fillna('IES ' + df['CO_IES'].astype(str))

plt.figure(figsize=(14, 8))
colors = ['green' if x==1.0 else 'orange' for x in df['eficiencia']]
bars = plt.bar(df['nome'], df['eficiencia'], color=colors)

plt.title('Eficiência dos Cursos de ADS - Análise DEA (ENADE)', fontweight='bold', fontsize=16)
plt.ylabel('Eficiência\n(1.0 = 100% eficiente)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.ylim(0, 1.1)
plt.grid(True, alpha=0.3)

for bar, eff in zip(bars, df['eficiencia']):
    plt.text(bar.get_x() + bar.get_width()/2, eff + 0.01, 
             f'{eff:.1f}', ha='center', fontweight='bold', fontsize=11)

plt.tight_layout()
plt.savefig('grafico_final_com_nomes.png', dpi=300, bbox_inches='tight')
plt.show()
