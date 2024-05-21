import unittest
from queue import Queue
import heapq

class Graph:
    def __init__(self, adjList: list[list[int]]=[], weighted: bool=False):
        self.vertices = len(adjList)
        if weighted:
            self.adjList = [x.copy() for x in adjList]
        else:
            self.adjList = [[(i, 1) for i in x] for x in adjList]
        self.time = 0
        self.sccCount = 0
    
    #Tarjan's Strongly Connected Component Algorithm
    def tarjanSCC(self):
        if self.vertices == 0:
            return -1
        def dfs(node, inStack, stack, visited, lowlink, inlink):
            stack.append(node)
            inStack[node] = True
            visited[node] = True
            lowlink[node] = self.time
            inlink[node] = self.time
            self.time += 1
            
            for neighbor, _ in self.adjList[node]:
                if not visited[neighbor]:
                    dfs(neighbor, inStack, stack, visited, lowlink, inlink)
                if neighbor in stack:
                    lowlink[node] = min(lowlink[node], lowlink[neighbor])

            if inlink[node] == lowlink[node]:
                while True:
                    curr = stack.pop()
                    inStack[curr] = False
                    lowlink[curr] = lowlink[node]
                    if curr == node:
                        break
                self.sccCount += 1
        
        
        
        visited = [False for i in range(self.vertices)] 
        lowlink = [0 for i in range(self.vertices)] #earlies
        inlink = [0 for i in range(self.vertices)]

        inStack = [False for i in range(self.vertices)]
        stack = []
        for i, x in enumerate(visited):
            if not x:
                dfs(i, inStack, stack, visited, lowlink, inlink)
        return self.sccCount
    
    def recursiveDFS(self):
        if self.vertices == 0:
            return -1
        visited = [False] * self.vertices
        def dfs(node, visited):
            visited[node] = True
            for neighbor, _ in self.adjList[node]:
                if not visited[neighbor]:
                    dfs(neighbor, visited)
        
        for node in range(self.vertices):
            if not visited[node]:
                dfs(node, visited)
    
    def stackDFS(self):
        if self.vertices == 0:
            return -1
        visited = [False] * self.vertices
        for i, x in enumerate(visited):
            if not x:
                #perform a stack DFS
                stack = []
                stack.append(x)
                while len(stack) > 0:
                    curr = stack.pop()
                    visited[curr] = True
                    for neighbor, _ in self.adjList[curr]:
                        if not visited[neighbor]:
                            stack.append(neighbor)
    def BFS(self):
        if self.vertices == 0:
            return -1
        queue = Queue()
        queue.put(0)
        visited = [False] * self.vertices
        for i, x in enumerate(visited):
            if not x:
                queue = Queue()
                queue.put(i)
                while queue.qsize() > 0:
                    curr = queue.get()
                    visited[curr] = True
                    for neighbor, _ in self.adjList[curr]:
                        if not visited[neighbor]:
                            queue.put(neighbor)
    def dijkstra(self, source):
        if self.vertices == 0:
            return -1
        
        distances = {}
        for x in range(self.vertices):
            distances[x] = float('inf')
        
        distances[source] = 0
        minHeap = []
        
        heapq.heappush(minHeap, (0, source))
        
        while len(minHeap) > 0:
            currDist, currNode = heapq.heappop(minHeap)
            for neighbor, cost in self.adjList[currNode]:
                if currDist + cost < distances[neighbor]:
                    distances[neighbor] = currDist + cost
                    heapq.heappush(minHeap, (currDist + cost, neighbor))
        return distances
class TestDirectedGraph(unittest.TestCase):
    def setUp(self):
        #multiple SCCs, dynamic 
        self.empty_graph = Graph()
        
        adjList1 = [    [1],
                        [2, 3, 0],
                        [3],
                        [2],
                        [3],
                        [6],
                        [5, 4, 7],
                        [8],
                        [7]]
        self.dynamic_graph = Graph(adjList1)

        #sparse graph, simple
        adjList2 = [    [1],
                        [0],
                        [],
                        [],
                        [],
                        [],
                        [],
                        [],
                        []]
        self.sparse_graph = Graph(adjList2)

        #one giant cycle
        adjList3 = [    [1],
                        [2],
                        [3],
                        [4],
                        [0]]
        self.cycle_graph = Graph(adjList3)

        adjList4 = [[(1, 1), (2,2)],
                     [(0,1), (3, 1)],
                     [(0, 2), (3, 1)],
                     [(1,1),(2,1)]]
        self.basic_graph_weighted = Graph(adjList4, True)

        adjList5 = [[(1, 5), (2, 3), (3, 4)],
                    [(2,1), (0, 5)],
                    [(0, 3), (4,6), (1,1)],
                    [(0, 4), (4, 2)],
                    [(3, 2), (2, 6)]]
        self.intermediate_graph_weighted = Graph(adjList5, True)

    def test_tarjanSCC(self):
        self.assertEqual(-1, self.empty_graph.tarjanSCC())
        
        self.assertEqual(self.dynamic_graph.tarjanSCC(), 5)
        self.assertEqual(self.sparse_graph.tarjanSCC(), 8)
        self.assertEqual(self.cycle_graph.tarjanSCC(), 1)
        
    def test_djikstra(self):
        expected1 = {0: 0, 1: 1, 2: 2, 3: 2}
        expected2 = {0: 0, 1: 4, 2: 3, 3: 4, 4: 6}

        self.assertEqual(-1, self.empty_graph.dijkstra(0))

        self.assertDictEqual(expected1, self.basic_graph_weighted.dijkstra(0))
        self.assertDictEqual(expected2, self.intermediate_graph_weighted.dijkstra(0))
        
    def test_DFS(self):
        self.assertEqual(-1, self.empty_graph.recursiveDFS())

        self.dynamic_graph.recursiveDFS()
        self.sparse_graph.recursiveDFS()
        self.cycle_graph.recursiveDFS()

        self.assertEqual(-1, self.empty_graph.stackDFS())

        self.dynamic_graph.stackDFS()
        self.sparse_graph.stackDFS()
        self.cycle_graph.stackDFS()
    def test_BFS(self):
        self.assertEqual(-1, self.empty_graph.BFS())
        
        self.dynamic_graph.BFS()
        self.sparse_graph.BFS()
        self.cycle_graph.BFS()
        

if __name__ == '__main__':
    unittest.main()
