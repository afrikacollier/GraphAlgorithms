"""
         0 -------- 1
         |        / | \
         |      /   |  \                                                                                      |     /    |   \                                                                                     |   /      |    2
         |  /       |   /
         |/         | /                                                                                       4 ---------3
"""
# The pseudo-code

"""
    Queue = []
    Points = []
    Queue.enqueue(StartingPoint)
    marking StartingPoint as visited
    while Queue is not empty:
        CurrentValue = Dequeue the firstValue from queue and return it 
        Points.append(currentValue)
        for neighbors around currentValue:
            if neighbors have not been visited:
                Queue.enqueue(neighbors)
    return Points
"""

# Similarly We can also solve this same problem using recursion but it is not reliable as recursion is a call stack which by nature favours Stacking over Queueing...

# Also the method works for both directed graphs and undirected graphs as far as the adjacency List is implemented correctly


# Implementation Using Iteration.

def bfs(adjList, root):
    queue = []
    points = []
    visited = set([]) # We use a set because adding and searching of values in a set is done in constant time i.e 0(1) as the values will be unique so it won't have any effect on the overall time complexity...
    queue.append(root)
    visited.add(root)
    while len(queue) > 0:
        currentValue = queue.pop(0)
        points.append(currentValue)
        
        for neighbors in adjList[currentValue]:
            if neighbors not in visited:
                queue.append(neighbors)
                visited.add(neighbors)
    return points
    
# Undirected graphs
# adjList = {
#     0: [1, 4],
#     1: [0, 2, 3, 4],
#     4: [0, 1, 3],
#     2: [1, 3],
#     3: [1, 2, 4]
# }


# Output [0, 1, 4, 2, 3]

# Directed Graphs
adjList = {
    0: [1, 4],
    1: [2, 3, 4],
    4: [],
    2: [3],
    3: [4]
}
adjList2 = {
    "a": ["c", "b"], 
    "b": ["d"], 
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}
print(bfs(adjList, 0))
print(bfs(adjList2, "a"))
# [0, 1, 4, 2, 3] output 1
# ['a', 'c', 'b', 'e', 'd', 'f'] output 2

# Using Recursion
print("Using Recursion... ")

points = []

def bfs_recursion(adjList, root, visited = set([])):
    if root not in visited:
        points.append(root)
        visited.add(root)
    length = len(adjList[root])
    for neighbors in adjList[root]:
        if neighbors not in visited:
            points.append(neighbors)
            visited.add(neighbors)
    i = 0
    while (i < length):
        bfs_recursion(adjList, adjList[root][i], visited)
        i += 1
bfs_recursion(adjList, 0)
print(points)
points = []
bfs_recursion(adjList2, "a")
print(points)

# Output 1 [0, 1, 4, 2, 3]
# Output 2 ['a', 'c', 'b', 'e', 'd', 'f']
