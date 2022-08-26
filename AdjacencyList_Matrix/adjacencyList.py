
"""
Converting edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3),  (3, 4)] to 
--- Adjacency list 
--- Adjacency Matrix.
"""

""" Adjacency List """


"""
-- Create a class graph 
-- Initialize a dictionary/objects (self.adjacencyList)...
-- Create a method to add adjacency nodes (add_adjacency_node) that takes in the edges as an argument
-- In the method iterate through the edges.
-- Extract n1 and n2... from the edges.. where n1 is the first point and n2 is the second point or n1 could be the source while n2 could be the destination...
-- Check if n1 is present in adjacency list... to avoid Nonetype error. if not initialize an array else
-- Append n2 to the array 
"""
# edge = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3),  (3, 4)]
edge = [
  ['i', 'j'],
  ['k', 'i'],
  ['m', 'k'],
  ['k', 'l'],
  ['o', 'n']
];
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
    l = ""
    for k, v in self.adjacencyList.items():
         l += f"{k}: {v}\n"
    return l
# directed graphs
class Graph2:
  def __init__(self):
    self.adjacencyList = {}
  def add_adjacency_node(self, edges):
    for n1, n2 in edges:
      if (n1 not in self.adjacencyList):
        self.adjacencyList[n1] = []
      if (n2 not in self.adjacencyList):
        self.adjacencyList[n2] = []
      self.adjacencyList[n1].append(n2)
  def __repr__(self):
    l = ""
    for k, v in self.adjacencyList.items():
         l += f"{k}: {v}\n"
    return l
    
graph = Graph()
graph.add_adjacency_node(edge)
print("Undirected graphs")
print(graph)

# Undirected graphs
# 0: [1, 4]
# 1: [0, 2, 3, 4]
# 4: [0, 1, 3]
# 2: [1, 3]
# 3: [1, 2, 4]

graph2 = Graph2()
graph2.add_adjacency_node(edge)
print("Directed Graph")
print(graph2)

# Output
# Directed Graph
# 0: [1, 4]
# 1: [2, 3, 4]
# 4: []
# 2: [3]
# 3: [4]
