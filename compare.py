import pandas as pd
import numpy as np


# Função para criar um DataFrame de exemplo com 100.000 linhas e 20 cidades únicas
def criar_medidas(num_linhas=100000, num_cidades=20, semente=None):
    estado = np.random.RandomState(semente)
    cidades = [f"Cidade_{i}" for i in range(num_cidades)]
    dados = {
        "estacao": estado.choice(cidades, size=num_linhas),
        "medida": estado.uniform(-20, 50, size=num_linhas).round(4)  # Medições de temperatura entre -20 e 50 com 4 casas decimais
    }
    df = pd.DataFrame(dados)
    return df

# Criar um DataFrame de exemplo
df = criar_medidas(semente=0)

# Exibir tipos de dados e uso de memória antes da conversão
print("Tipos de dados e uso de memória antes da conversão:")
print(df.dtypes)
print(df.memory_usage(deep=True))

# Salvar o uso de memória inicial
uso_memoria_inicial = df.memory_usage(deep=True).sum()

# Detalhes do uso de memória antes da conversão
detalhes_memoria_antes = df.memory_usage(deep=True)

# Converter tipos de dados para tipos mais eficientes
df["estacao"] = df["estacao"].astype("category")
df["medida"] = pd.to_numeric(df["medida"], downcast="float")

# Exibir tipos de dados e uso de memória após a conversão
print("\nTipos de dados e uso de memória após a conversão:")
print(df.dtypes)
print(df.memory_usage(deep=True))

# Salvar o uso de memória final
uso_memoria_final = df.memory_usage(deep=True).sum()

# Calcular a redução no uso de memória
reducao_total = 1 - (uso_memoria_final / uso_memoria_inicial)
reducao_estacao = 1 - (df.memory_usage(deep=True)['estacao'] / detalhes_memoria_antes['estacao'])
reducao_medida = 1 - (df.memory_usage(deep=True)['medida'] / detalhes_memoria_antes['medida'])

print(f"\nRedução total no uso de memória: {reducao_total:.2f}")
print(f"Redução no uso de memória para a coluna 'estacao': {reducao_estacao:.2f}")
print(f"Redução no uso de memória para a coluna 'medida': {reducao_medida:.2f}")

# Detalhes do uso de memória antes e depois da conversão
print("\nDetalhes do uso de memória antes da conversão:")
print(detalhes_memoria_antes)

print("\nDetalhes do uso de memória após a conversão:")
print(df.memory_usage(deep=True))
