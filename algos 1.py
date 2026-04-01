tree = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F','G'],
    'D' : ['H'],
    'E' : [],
    'F' : ['I'],
    'G' : [],
    'H' : [],
    'I' : []
}

# ---------------- BFS ----------------
def bfs(tree , start , goal):

    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    while queue:

        node = queue.pop(0)
        print(node,end=" ")

        if node == goal:
            print("\nGoal found :", node)
            return

        for i in tree[node]:
            if i not in visited:
                visited.append(i)
                queue.append(i)


# ---------------- DFS ----------------
def dfs(tree , start , goal):

    visited = []
    stack = []

    stack.append(start)

    while stack:

        node = stack.pop()

        if node not in visited:

            visited.append(node)
            print(node,end=" ")

            if node == goal:
                print("\nGoal found :", node)
                return

            for i in reversed(tree[node]):
                stack.append(i)


# ---------------- DLS ----------------
def dls(node, goal, depth, path):

    if depth == 0:
        return False

    if node == goal:
        path.append(node)
        return True

    if node not in tree:
        return False

    for child in tree[node]:
        if dls(child, goal, depth - 1, path):
            path.append(node)
            return True

    return False
# ---------------- IDS ----------------
def iterative_deepening(start, goal, max_depth):

    for depth in range(max_depth + 1):

        print("Depth:", depth)

        path = []

        if dls(start, goal, depth, path):

            print("\nPath to goal:", " -> ".join(reversed(path)))
            return

    print("Goal not found within depth limit.")

def ucs(tree, start, goal):
    queue = [(start, costs[start])]
    visited = []

    while queue:
        # sort by cost
        queue.sort(key=lambda x: x[1])
        node, cost = queue.pop(0)
        if node is None:
            continue
        visited.append(node)

        if node == goal:
            print("UCS Found:", visited, "Cost:", cost)
            return

        left, right = tree.get(node, [None, None])
        if left:
            queue.append((left, cost + costs[left]))
        if right:
            queue.append((right, cost + costs[right]))

    print("Not Found")

def dls(tree,start,goal,depth_limit):
    visited = []
    def dfs(node, depth):

        if depth>depth_limit:
            print("depth exceed")
            return None

        if node == goal:
            print("goal is found",node)
            return node
        
        visited.append(node)

        while i in tree.get(node,[]):
            if i not in visited:
                path = dfs(node,depth+1)
            if path:
                return path
        
        visited.pop(0)
        return None
            
# ---------------- Test ----------------
start = 'A'
goal = 'I'

print("BFS Traversal")
bfs(tree,start,goal)

print("\nDFS Traversal")
dfs(tree,start,goal)

print("\nIterative Deepening Search")
iterative_deepening(start,goal,5)