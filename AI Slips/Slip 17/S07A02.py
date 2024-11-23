import heapq

# Define the graph as an adjacency list
graph = {
    'A': {'B': 9, 'C': 7, 'D': 21},
    'B': {'E': 14},
    'C': {'E': 17, 'F': 12},
    'D': {'F': 14},
    'E': {'G': 5},
    'F': {'G': 8},
    'G': {}
}

# Define the heuristic values for each node
heuristic = {
    'A': 25,
    'B': 14,
    'C': 20,
    'D': 35,
    'E': 10,
    'F': 15,
    'G': 0
}

# A* algorithm
def a_star_algorithm(start, goal):
    open_set = []
    heapq.heappush(open_set, (0 + heuristic[start], 0, start, []))  # (f_score, g_score, current_node, path)
    visited = set()

    while open_set:
        _, g_score, current, path = heapq.heappop(open_set)

        if current in visited:
            continue

        visited.add(current)
        path = path + [current]

        if current == goal:
            return path, g_score

        for neighbor, cost in graph[current].items():
            if neighbor not in visited:
                new_g_score = g_score + cost
                f_score = new_g_score + heuristic[neighbor]
                heapq.heappush(open_set, (f_score, new_g_score, neighbor, path))

    return None, None

# Define start and goal
start_node = 'A'
goal_node = 'G'

# Run the algorithm
path, cost = a_star_algorithm(start_node, goal_node)

# Output the results
if path:
    print(f"Path: {' -> '.join(path)}")
    print(f"Cost: {cost}")
else:
    print("No path found")