from processor import load_dataset
from sklearn.cluster import KMeans
import os
import shutil

# --- CONFIGURAÇÃO ---
PASTA_DATASET = "Dataset/images/"
PASTA_OUTPUT = "Output/"
NUM_CLUSTERS = 2  # Ajuste para a quantidade de tipos de objetos que você fotografou

# 1. Carregar os dados (Aqui ele descobre o caminho!)
print("Lendo imagens do dataset...")
features, nomes_arquivos = load_dataset(PASTA_DATASET)

if len(features) == 0:
    print("Erro: Nenhuma imagem encontrada na pasta dataset!")
else:
    # 2. Aplicar o K-Means
    print(f"Agrupando em {NUM_CLUSTERS} clusters...")
    kmeans = KMeans(n_clusters=NUM_CLUSTERS, random_state=42)
    labels = kmeans.fit_predict(features)

    # 3. Organizar os resultados (Mover para pastas de clusters)
    print("Organizando arquivos por grupo...")
    for i in range(NUM_CLUSTERS):
        caminho_cluster = os.path.join(PASTA_OUTPUT, f"Cluster_{i}")
        if not os.path.exists(caminho_cluster):
            os.makedirs(caminho_cluster)

    for nome, cluster_id in zip(nomes_arquivos, labels):
        origem = os.path.join(PASTA_DATASET, nome)
        destino = os.path.join(PASTA_OUTPUT, f"Cluster_{cluster_id}", nome)
        shutil.copy(origem, destino) # Copia para não deletar o original

    print("✅ Sucesso! Verifique a pasta 'output' para ver os grupos.")