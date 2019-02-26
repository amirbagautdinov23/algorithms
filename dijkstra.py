from math import inf

# веса ребер(перехода)
graph = {
    "start": {
        "a": 6,
        "b": 2,
    },
    "a": {
        "end": 1,
    },
    "b": {
        "a": 3,
        "end": 5,
    },
    "end": {},
}

# стоимость всех узлов. Можно узнать стоимость от начального узла до конкретного
infinity = inf
costs = {
    "a": 6,
    "b": 2,
    "end": infinity
}

# таблица родитель-узел
parents = {
    "a": "start",
    "b": "start",
    "end": None,
}

# список пройденных узлов. Чтобы не проходить по пройденным узлам
processed = []


# возвращает узел с наименьшей стоимостью перехода. Простая реализация
def find_lowest_cost_node(costs):
    try:
        sorted_dict = sorted(costs.items(), key=lambda x: x[1])
        return sorted_dict[0][0]
    except:
        pass

node = find_lowest_cost_node(costs)

# алгоритм Дейкстры
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)


