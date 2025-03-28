import pandas as pd  # Manipulação de dados
import numpy as np  # Operações matemáticas
import matplotlib.pyplot as plt  # Gráficos

#Estatísticas básicas
print("Dados do Campeonato Inglês 2025:")
df = pd.read_csv("classificacao.csv")  # Criando DataFrame

print("Zona de classificação para a Liga dos Campeões UEFA:")
print(df.head(5))  # Exibindo as primeiras linhas

print("Zona de rebaixamento para a segunda divisão:")
print(df.tail(3)) # Exibindo as últimas linhas

column_name='Time'
num_times = len(df.get(column_name, pd.Series()))

print(f"Número de times no Campeonato: {num_times}")

# Gráfico de barras com a pontuação de cada time
plt.figure(figsize=(12, 6))
plt.barh(df['Time'], df['Pontos'], color='lightblue', edgecolor='black')
plt.title("Pontuação por Time - Campeonato Inglês 2025")
plt.xlabel("Pontos")
plt.ylabel("Times")
plt.show()

# Gráfico de barras dos times com maior aproveitamento
plt.figure(figsize=(12, 6))
plt.bar(df['Time'], df['Aproveitamento'], color='grey', edgecolor='black')
plt.title("Aproveitamento por Time - Campeonato Inglês 2025")
plt.xlabel("Aproveitamento (%)")
plt.ylabel("Times")
plt.xticks(fontsize=10, rotation='vertical', va='center', ha='right')
plt.tight_layout()
plt.show()

# Gráfico de barras agrupadas com gols pó e gols contra de cada time
plt.figure(figsize=(10, 6))
bar_height = 0.35  # Largura das barras
index = range(len(df['Time']))  # Posições no eixo X
plt.barh(index, df['Gols pró'], height=bar_height, label='Gols pró', color='skyblue', edgecolor='black') # Barras para gols pró
plt.barh([i + bar_height for i in index], df['Gols contra'], height=bar_height, label='Gols contra', color='salmon', edgecolor='black')# Barras para gols contra
plt.xlabel('Gols')
plt.ylabel('Times')
plt.title('Comparação de Gols: pró vs contra')
plt.yticks([i + bar_height /2 for i in index], df['Time'])  # Centraliza os rótulos
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Gráfico de pizza para representar o quanto cada time representa no total de pontos do campeonato
total_pontos = df['Pontos'].sum()
df['Percentual'] = (df['Pontos'] / total_pontos) * 100

plt.figure(figsize=(10, 10))
sizes = {
    'labels': 7,      # Tamanho dos nomes dos times
    'percent': 10,     # Tamanho dos percentuais
    'title': 12        # Tamanho do título
}
plt.pie(df['Percentual'],
        labels=df['Time'],
        autopct='%1.1f%%',
        startangle=90,
        pctdistance=0.85,
        textprops={
            'rotation': 30,  # Rotação de 45 graus
            'ha': 'center',  # Alinhamento horizontal central
            'va': 'center',  # Alinhamento vertical central
            'fontsize': 10  # Tamanho da fonte
        },
        wedgeprops={'edgecolor': 'white', 'linewidth': 1})

# Círculo central para deixar o gráfico com aspecto de donut e melhorar o aspecto visual
centre_circle = plt.Circle((0,0), 0.50, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title(f'\nDistribuição Percentual dos Pontos - Total do Campeonato: {total_pontos} pontos\n', pad=20)
plt.axis('equal')  # Assegura que o gráfico é desenhado como um círculo
plt.tight_layout()
plt.show()