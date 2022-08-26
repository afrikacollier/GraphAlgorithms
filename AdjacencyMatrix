# Adjacency Matrix
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
    self.a = []
    for a1, a2 in edges:
        if a1 not in self.a:
            self.a.append(a1)
        if a2 not in self.a:
            self.a.append(a2)
    for n1, n2 in edges:
      if (n1 not in self.adjacencyList):
        self.adjacencyList[n1] = [0] * len(self.a)
      if (n2 not in self.adjacencyList):
        self.adjacencyList[n2] = [0] * len(self.a)
      i = self.a.index(n1)
      j = self.a.index(n2)
      self.adjacencyList[n1][j] = 1
      self.adjacencyList[n2][i] = 1
  def __repr__(self):
    # return str(self.adjacencyList)
    l = ""
    d = "__"
    l += "   "
    
    for i in self.a:
        l += f"{i}  "
        d += "___"
    l += "\n"
    d += "\n"
    for k, v in self.adjacencyList.items():
         s = "  ".join([f"{w}" for w in v])
         l += f"{k}: {s}\n"
    return d + l
graph = Graph()
graph.add_adjacency_node(edge)
print("Adjacency Matrix")
print(graph)


# Adjacency Matrix
# _______________________
#    i  j  k  m  l  o  n  
# i: 0  1  1  0  0  0  0
# j: 1  0  0  0  0  0  0
# k: 1  0  0  1  1  0  0
# m: 0  0  1  0  0  0  0
# l: 0  0  1  0  0  0  0
# o: 0  0  0  0  0  0  1
# n: 0  0  0  0  0  1  0

# Adjacency Matrix
# _________________
#    0  1  4  2  3  
# 0: 0  1  1  0  0
# 1: 1  0  1  1  1
# 4: 1  1  0  0  1
# 2: 0  1  0  0  1
# 3: 0  1  1  1  0
