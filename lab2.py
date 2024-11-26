import networkx as nx
import matplotlib.pyplot as plt

# Создаём граф с 4 узлами
G = nx.Graph()
G.add_edges_from([
    (0, 1),
    (0, 2),
    (0, 3)
])
# Узел 0 связан с 1, 2 и 3, но между 1, 2 и 3 нет прямых связей

# Считаем центральности в собственных векторах
centrality = nx.eigenvector_centrality(G)

# Выводим результаты
print("Центральности узлов:")
for node, value in centrality.items():
    print(f"Узел {node}: Центральность {value:.4f}")