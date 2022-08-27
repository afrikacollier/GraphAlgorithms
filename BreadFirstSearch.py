# Breadth First Search...
# Implementing breadth first search... involves taking into consideration the nearest edges before going deeper.
 # For instance consider the points
#        0 -------- 1 
#        |        / | \
#        |      /   |  \
#        |     /    |   \
#        |   /      |    2
#        |  /       |   /
#        |/         | /
#        4 ---------3
# Using bread first search we print out the nearest points before going for the deeper points.
# We get the following points using breadth first search...
# Suppose we set 0 as our starting point..  Then we have
# 0 1 4 2 3...
# Explanation...
# To use breadth first search we use a queue system... because in a queue.. the First element that goes in will the first to go out which is the perfect method we need to solve this problem since we need to account for the nearest elements before the deeper ones 
# Demonstrating the idea.. from the Example below..
# We instanstiate a queue. and the points( which contains the list of points)
# Queue = []
# Points = []
# Starting from 0.. we visit the point 0..
# which is enqueued into the Queue...
# Now we have Queue = [0]
# Then we pop 0 out since we are following the Queueing rules..(FIFO)
# thus the Queue goes empty and we now have Queue = []
# Since we popped a value we enlist the popped value into the Points array now we have Points = [0]
# Now we go for the the neighbors of 0 which was just popped  out... The two neigbors of 0 are 1 and 4 then we push those to values into the queue... now we have 
# Queue = [1, 4]
# we pop out the first as usual following the Queueing rules..(FIFO)
# and we enlist into points... we now have 
# Queue = [4] and Points = [0, 1]
# Since 1 was just dequeued we then check for the neighbors of 1 and enqueue them.. The neighbors of 1 are 2 and 3 we enqueue them too
# now we have Queue = [4, 2, 3]
# we pop out 4 and we add into Points 
# Points = [0, 1, 4] and Queue = [2, 3]
# The we check for the neighbors of 4 which are 0 1 3 but we realize that they've already been enlisted or queued.. so we don't do anything 
# We do the same thing for 2 and 3... and their neighbors have already been enlisted or queued thus we have
# Queue = [] and Points = [0, 1, 4, 2, 3]

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
