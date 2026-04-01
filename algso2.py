graph = {
    'S': [('A', 3), ('B', 6), ('C', 5)],
    'A': [('D', 9), ('E', 8)],
    'B': [('F', 12), ('G', 14)],
    'C': [('H', 7)],
    'H': [('I', 5), ('J', 6)],
    'I': [('K', 1), ('L', 10), ('M', 2)],
    'D': [],'E': [],
    'F': [],'G': [],
    'J': [],'K': [],
    'L': [],'M': []
}
# Beam Search function
def beam_search(start, goal, beam_width=2):
    # Initialize the beam with the start state
    beam = [(0, [start])]  # (cumulative cost, path)

    while beam:
        candidates = []
        # Expand each path in the beam
        for cost, path in beam:
            current_node = path[-1]
            if current_node == goal:
                return path, cost  # Return the path and cost if goal
            # Generate successors
            for neighbor, edge_cost in graph.get(current_node, []):
                new_cost = cost + edge_cost
                new_path = path + [neighbor]
                candidates.append((new_cost, new_path))

        # Select top-k paths based on the lowest cumulative cost
        beam = heapq.nsmallest(beam_width, candidates, key=lambda x: x[0])
        #print(beam)
    return None, float('inf')  # Return None if no path is found


# Run Beam Search
start_node = 'S'
goal_node = 'L'
beam_width = 3
path, cost = beam_search(start=start_node, goal=goal_node, beam_width=beam_width)


# Print results
if path:
    print(f"Path found: {' → '.join(path)} with total cost: {cost}")
else:
    print("No path found.")









graph = {
    'S': {'A': 3, 'B': 6, 'C': 5},
    'A': {'D': 9, 'E': 8},
    'B': {'F': 12, 'G': 14},
    'C': {'H': 7},
    'H': {'I': 5, 'J': 6},
    'I': {'K': 1, 'L': 10, 'M': 2},
    'D': {}, 'E': {}, 'F': {}, 'G': {},
    'J': {}, 'K': {}, 'L': {}, 'M': {}
}

heuristic = {
    'S': 10, 'A': 9, 'B': 7, 'C': 5, 'D': 8, 'E': 6, 'F': 4, 'G': 3,
    'H': 3, 'I': 2, 'J': 6, 'K': 2, 'L': 0, 'M': 1
}

def ucs(graph, start, goal):
    frontier = [(start, 0)]  # (node, cost)
    visited = set()
    cost_so_far = {start: 0}
    came_from = {start: None}

    while frontier:
        frontier.sort(key=lambda x: x[1])
        current_node, current_cost = frontier.pop(0)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"Goal found with UCS. Path: {path}, Total Cost: {current_cost}")
            return

        for neighbor, cost in graph[current_node].items():
            new_cost = current_cost + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current_node
                frontier.append((neighbor, new_cost))

    print("Goal not found")

def best_first_search(graph, start, goal):
    frontier = [(start, heuristic[start])]
    visited = set()
    came_from = {start: None}

    while frontier:
        frontier.sort(key=lambda x: x[1])
        current_node, _ = frontier.pop(0)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"Goal found with Best First Search. Path: {path}")
            return

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                frontier.append((neighbor, heuristic[neighbor]))
                came_from[neighbor] = current_node

    print("Goal not found")

def a_star_search(graph, start, goal):
    frontier = [(start, 0 + heuristic[start])]
    visited = set()
    cost_so_far = {start: 0}
    came_from = {start: None}

    while frontier:
        frontier.sort(key=lambda x: x[1])
        current_node, _ = frontier.pop(0)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"Goal found with A*. Path: {path}, Total Cost: {cost_so_far[goal]}")
            return

        for neighbor, cost in graph[current_node].items():
            new_cost = cost_so_far[current_node] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                frontier.append((neighbor, new_cost + heuristic[neighbor]))
                came_from[neighbor] = current_node

    print("Goal not found")

def beam_search(graph, start, goal, beam_width=2):
    frontier = [(start, heuristic[start])]
    visited = set()
    came_from = {start: None}

    while frontier:
        frontier.sort(key=lambda x: x[1])
        frontier = frontier[:beam_width]  # Keep only top beam_width nodes
        next_frontier = []

        for current_node, _ in frontier:
            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node == goal:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = came_from[current_node]
                path.reverse()
                print(f"Goal found with Beam Search. Path: {path}")
                return

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    next_frontier.append((neighbor, heuristic[neighbor]))
                    came_from[neighbor] = current_node

        frontier = next_frontier

    print("Goal not found")

# Running all algorithms
ucs(graph, 'S', 'L')
best_first_search(graph, 'S', 'L')
a_star_search(graph, 'S', 'L')
beam_search(graph, 'S', 'L')

















def hill_climbing(graph, start, goal):
    current_node = start
    path = [current_node]

    while current_node != goal:
        neighbors = graph.get(current_node, [])
        if not neighbors:
            print("No path found with Hill Climbing.")
            return None

        # Choose the best neighbor based on the heuristic (lowest value)
        best_neighbor = min(neighbors, key=lambda x: heuristic[x[0]])
        best_neighbor_node = best_neighbor[0]

        # If the best neighbor is worse than the current node, stop (local maximum)
        if heuristic[best_neighbor_node] >= heuristic[current_node]:
            print("Stuck at local maximum. No path found with Hill Climbing.")
            return None

        current_node = best_neighbor_node
        path.append(current_node)

        if current_node == goal:
            print(f"Goal found with Hill Climbing. Path: {path}")
            return path

    print("Goal not found.")
    return None
hill_climbing(graph, 'S', 'L')


import random
# Heuristic function: Counts the number of pairs of attacking queens
def calculate_conflicts(state):
    print(state)
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            # Check same column or diagonal
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts


# Generate neighbors by moving one queen at a time
def get_neighbors(state):
    neighbors = []
    n = len(state)
    for row in range(n):
        for col in range(n):
            if col != state[row]:
                new_state = list(state)
                new_state[row] = col
                neighbors.append(new_state)
    return neighbors


# Simple Hill Climbing function
def simple_hill_climbing(n):
    # Random initial state
    current_state = [random.randint(0, n - 1) for _ in range(n)]
    current_conflicts = calculate_conflicts(current_state)

    while True:
        neighbors = get_neighbors(current_state)
        next_state = None
        next_conflicts = current_conflicts
        # Find the first better neighbor
        for neighbor in neighbors:
            neighbor_conflicts = calculate_conflicts(neighbor)
            if neighbor_conflicts < next_conflicts:
                next_state = neighbor
                next_conflicts = neighbor_conflicts
                break  # Move to the first better neighbor

        # If no better neighbor is found, return the current state
        if next_conflicts >= current_conflicts:
            break

        # Move to the better neighbor
        current_state = next_state
        current_conflicts = next_conflicts

    return current_state, current_conflicts


# Run Simple Hill Climbing for N-Queens
n = 8  # Change N here for different sizes
solution, conflicts = simple_hill_climbing(4)


# Print results
if conflicts == 0:
    print(f"Solution found for {n}-Queens problem:")
    print(solution)
else:
    print(f"Could not find a solution. Stuck at state with {conflicts} conflicts:")
    print(solution)
