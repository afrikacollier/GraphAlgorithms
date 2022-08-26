// Online Javascript Editor for free
// Write, Edit and Run your Javascript code using JS Online Compiler

// edges = [[0, 1], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3],  [3, 4]]

const edges = [
  ['i', 'j'],
  ['k', 'i'],
  ['m', 'k'],
  ['k', 'l'],
  ['o', 'n']
];
class Graph{
  constructor(){
    this.adjacencyList = {};
  }

  addNode(node){
    if (!this.adjacencyList[node])
        this.adjacencyList[node] = [];
  }

  addEdge(node1, node2) {
    this.adjacencyList[node1].push(node2);
    //don't need line if it's directed
    this.adjacencyList[node2].push(node1);
  }
  displayAdjacencyList () {
      console.log(this.adjacencyList)
  }
}
myGraph = new Graph()
for (node of edges)
{
  const [a, b] = node
  myGraph.addNode(a);
  myGraph.addNode(b);
  myGraph.addEdge(a, b);
}
myGraph.displayAdjacencyList()

// Undirected graphs Output
// { '0': [ 1, 4 ],
//   '1': [ 0, 2, 3, 4 ],
//   '2': [ 1, 3 ],
//   '3': [ 1, 2, 4 ],
//   '4': [ 0, 1, 3 ] }

// Directed graphs Output.
// { '0': [ 1, 4 ],
//   '1': [ 2, 3, 4 ],
//   '2': [ 3 ],
//   '3': [ 4 ],
//   '4': [] }
