from queue import PriorityQueue

def a_star_algorithm(graph, heuristics, start, goal):
    open_list = PriorityQueue()
    open_list.put((0, start))  # Priority queue to store nodes with cost
    came_from = {}  # To store the path
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristics[start]

    while not open_list.empty():
        _, current = open_list.get()

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor, weight in graph[current].items():
            tentative_g_score = g_score[current] + weight
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristics[neighbor]
                open_list.put((f_score[neighbor], neighbor))
    return None


# Graph representation and heuristic values
graph = {
    'A': {'B': 2, 'E': 3},
    'B': {'C': 6, 'A': 2},
    'C': {'F': 99, 'B': 6},
    'D': {'E': 6, 'F': 1},
    'E': {'A': 3, 'D': 6},
    'F': {'D': 1, 'C': 99},
}

heuristics = {
    'A': 11,
    'B': 6,
    'C': 99,
    'D': 1,
    'E': 7,
    'F': 0,
}

# Test the algorithm
start_node = 'A'
goal_node = 'F'
path = a_star_algorithm(graph, heuristics, start_node, goal_node)
if path:
    print(f"Path found: {' -> '.join(path)}")
else:
    print("No path found.")