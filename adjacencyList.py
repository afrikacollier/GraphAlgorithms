
"""
Converting edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3),  (3, 4)] to 
--- Adjacency list 
--- Adjacency Matrix.
"""

""" Adjacency List """
edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3),  (3, 4)]
# for n1, n2 in edges:
  # print(n1, n2)

# Undirected graphs

class Graph:
  def __init__(self):
    self.adjacencyList = {}
  def add_adjacency_node(self, edges):
    for n1, n2 in edges:
      if (n1 not in self.adjacencyList):
        self.adjacencyList[n1] = []
      if (n2 not in self.adjacencyList):
        self.adjacencyList[n2] = []
      self.adjacencyList[n1].append(n2)
      self.adjacencyList[n2].append(n1)
  def __repr__(self):
    return str(self.adjacencyList)
# directed graphs
class Graph2:
  def __init__(self):
    self.adjacencyList = {}
  def add_adjacency_node(self, edges):
    for n1, n2 in edges:
      if (n1 not in self.adjacencyList):
        self.adjacencyList[n1] = []
      self.adjacencyList[n1].append(n2)
  def __repr__(self):
    return str(self.adjacencyList)
graph = Graph()
graph.add_adjacency_node([(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3),  (3, 4)])
print("Directed graphs", graph)
graph2 = Graph2()
graph2.add_adjacency_node(edges)
print("Undirected graphs", graph2)

"""
-- Create a class graph 
-- Initialize a dictionary/objects (self.adjacencyList)...
-- Create a method to add adjacency nodes (add_adjacency_node) that takes in the edges as an argument
-- In the method iterate through the edges.
-- Extract n1 and n2... from the edges.. where n1 is the first point and n2 is the second point or n1 could be the source while n2 could be the destination...
-- Check if n1 is present in adjacency list... to avoid Nonetype error. if not initialize an array else
-- Append n2 to the array 
"""

"""
class Graph{
  constructor(){
    this.adjacencyList();
  }

  addNode(node){
    this.adjacencyList(node) = [];
  }

  addEdge(node1, node2) {
    this.adjacencyList[node1].push(node2);
    //don't need line if it's directed
    this.adjacencyList[node2].push(node1);
  }
}
for (node of edges)
{
  const [a, b] = node
  myGraph.addNode(a);
  myGraph.addNode(b);
  myGraph.addEdge(a, b);
}
"""
