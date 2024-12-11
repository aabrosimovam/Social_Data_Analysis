import networkx as nx
import matplotlib.pyplot as plt

# Заданные параметры модели Эрдёша-Реньи
n = 45  # количество вершин
p = 0.65  # вероятность появления ребра

# Генерация случайного графа
graph = nx.erdos_renyi_graph(n, p)

# Вычисление средней степени вершины в графе
average_degree_actual = sum(dict(graph.degree()).values()) / n

# Теоретическая средняя степень вершины
average_degree_theoretical = p * (n - 1)

# Вывод результатов
print("Средняя степень вершины (фактическая):", round(average_degree_actual, 2))
print("Средняя степень вершины (теоретическая):", round(average_degree_theoretical, 2))


