/*
    Queue = []
    Points = []
    Queue.enqueue(StartingPoint)
    marking StartingPoint as visited
    while Queue is not empty:
        CurrentValue = Dequeue the firstValue from queue and return it 
        Points.push(currentValue)
        for neighbors around currentValue:
            if neighbors have not been visited:
                Queue.enqueue(neighbors)
    return Points
*/

const bfs = (graph, root) => {
    let queue = []
    let points = []
    let visited = new Set()
    // We use a set because adding and searching of values in a set is done in constant time i.e 0(1) as the values will be unique so it won't have any effect on the overall time complexity...
    queue.push(root)
    visited.add(root)
    while (queue.length > 0)
    {
        const current = queue.shift()
        points.push(current)
        
        for (neighbors of graph[current])
        {
            if (!(visited.has(neighbors)))
            {
                queue.push(neighbors)
                visited.add(neighbors)
            }
        }
    }
    return points
}
// Undirected graphs
graph = {
     0: [1, 4],
     1: [0, 2, 3, 4],
     4: [0, 1, 3],
     2: [1, 3],
     3: [1, 2, 4]
}
console.log(bfs(graph, 0))

// [ 0, 1, 4, 2, 3 ] output

// Undirected graph
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

console.log(bfs(adjList, 0))
console.log(bfs(adjList2, 'a'))
// Output 1 [ 0, 1, 4, 2, 3 ]
// Output 2 [ 'a', 'c', 'b', 'e', 'd', 'f' ]

// Using Recursion

let points = []       
const bfs_recursion = (graph, root, visited = new Set()) => {
    if (!visited.has(root))
    {
        points.push(root)
        visited.add(root)
    }
    const len = graph[root].length
    for (neighbors of graph[root])
    {
        if (!visited.has(neighbors))
        {
            points.push(neighbors)
            visited.add(neighbors)
        }
    }
    let i = 0
    while (i < len)
    {
        bfs_recursion(graph, graph[root][i], visited)
        i++;
    }
}
console.log("Using recursion")
bfs_recursion(adjList, 0)
console.log(points)
points = []
bfs_recursion(adjList2, 'a')
console.log(points)

/*
 [ 0, 1, 4, 2, 3 ] Output 1
[ 'a', 'c', 'b', 'e', 'd', 'f' ] Output 2
*/

