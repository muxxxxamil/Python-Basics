import sys as s
class Basics:
    def __init__(self, n=4, word="MOM", sentence="Is MOM there?"):
        self.n = n
        self.word = word
        self.sentence = sentence

    def fact(self, n):
        if n < 3:
            return n
        else:
            return (n * self.fact(n - 1))

    def fibNum(self, n):
        if n in {0, 1}:
            return n
        else:
            return self.fibNum(n - 1) + self.fibNum(n - 2)

    def fibonacciSequence(self, n):
        return [self.fibNum(num) for num in range(0, n)]

    def isPrime(self, n):
        return self.fact(n - 1) % n == n - 1 # wilson's theorem

    def isEven(self, n):
        if (n % 2) == 0:
            return True
        else:
            return False
    
    def isPalindrome(self, word):
        word_reverse = word[::-1]
        if word_reverse == word:
            return True
        else:
            return False

    def inSentence(self, sentence, word):
        return (' '+ word + ' ') in (' '+ sentence + ' ')

class Stack:
    def __init__(self):
        self.items = []

    def isEmpyty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

# Tree is non-linear data structure (Node = (L, R) where L is set of left child node 
# and R is a set of right child node)
#  used in routes and bridges having heirarchical data
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
    
    def treeHeigth(self, root):
        if root is None:
            return -1
        leftHeigth = self.treeHeigth(root.left_child)
        rightHeigth = self.treeHeigth(root.right_child)
        max_heigth = leftHeigth
        if max_heigth < rightHeigth:
            max_heigth = rightHeigth
        return max_heigth + 1   

    def insert(self, root, value):
        if root is None:
            root = BinaryTreeNode(value)
            return root
        if value < root.data:
            root.left_child = self.insert(root.left_child, value)
        else:
            root.right_child = self.insert(root.right_child, value)
        return root

    # Graph is a non-linear data structure (G = (V, E) where V is set of vertices
    # and E is set of edges in graph) used in routes and social network 
    # perhaps finding a shortest path or relationship.

    # Types of graphs 
    # 1. Direction based (Directed graph is a path bw E(X,Y) != E(Y,X) and Undirected is other way around) 
    # 2. Weight based (represented as (u, v, w) where u is source vertex, 
    # and v is destination vertex and w is weigth to go from u to v). 
    # Relationship in query language like GraphQL can represent using unweighted graph. 
    # 3. Special graphs 3.1 = Trees undirected graph with zero cycle is tree. 
    # Cycle is a sequence(path) starts and ends at the same vertex. 
    # 3.2 = Rooted Tree has root E away from root is arborescence/out-tree 
    # and E towards the root is anti-aborescence/in-tree
    # 3.3 = Directed Acyclic Graphs also DAGs with no directed cylces
    # 3.4 = Complete Graph have unique edge between every pair of vertices)
    # To represent graph adjacency matrix A[x][y]   

    # Assuming a weighted graph where V = {a, b, c} 
    # and E = {(a, b, 3), (a, c, 5), (b, c, 4)}

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = s.maxsize
        # Mark all nodes unvisited        
        self.visited = False  
        # Predecessor
        self.previous = None

    def __iter__(self):
        return iter(self.adjacent.values())

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def addNeighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def getConnections(self):
        return self.adjacent.keys()  

    def getId(self):
        return self.id

    def getWeight(self, neighbor):
        return self.adjacent[neighbor]
        
    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True
    
class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())
    
    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

    def addVertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def getVertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def addEdge(self, u, v, cost = 0):
        if u not in self.vert_dict:
            self.addVertex(u)
        if v not in self.vert_dict:
            self.addVertex(v)

        self.vert_dict[u].addNeighbor(self.vert_dict[v], cost)
        self.vert_dict[v].addNeighbor(self.vert_dict[u], cost)

    def getVertices(self):
        return self.vert_dict.keys()

    def shortest(self, v, path):
        #''' make shortest path from v.previous'''
        if v.previous:
            path.append(v.previous.getId())
            self.shortest(v.previous, path)
        return

    def createGraph(self):
        
        # Adding vertices in graphs
        self.addVertex('a')
        self.addVertex('b')
        self.addVertex('c')

        # Adding edges 
        self.addEdge('a', 'b', 3) 
        self.addEdge('a', 'c', 5)
        self.addEdge('b', 'c', 4)
        return self      

# Main()

if __name__ == '__main__':
    basic = Basics(7)
    
    print("1). Factorial of "+ str(basic.n) + " =  "+ str(basic.fact(basic.n)) + "!")
    print("2). Fibonacci sequence of "+ str(basic.n) + " = " + str(basic.fibonacciSequence(basic.n)))
    print("3). Is '"+ basic.word + "' palindrome (True/False) = "+ str(basic.isPalindrome(basic.word)))
    print("4). Is "+ str(basic.n) + " an even number? = "+ str(basic.isEven(basic.n)))
    print("5). Is "+ str(basic.n) + " a prime number? = "+ str(basic.isPrime(basic.n)))
    print("6). Is '"+ basic.word + "' in '"+ basic.sentence + "' = " + str(basic.inSentence(basic.sentence, basic.word)))
    
    #Tree
    tree = BinaryTreeNode(None)
    # root
    root = tree.insert(None, 6)
    # reft subtree
    tree.insert(root, 5)
    tree.insert(root, 4)
    tree.insert(root, 3)
    # right subtree
    tree.insert(root, 8)
    tree.insert(root, 7)
    tree.insert(root, 9)

    print("Height of a Binary tree is = " + str(tree.treeHeigth(root)))

    
    graph = Graph()
    graph.createGraph()

    print("Edges and weight between vertices")
    for vert in graph:
        for w in vert.getConnections():
            print("(" + str(vert.getId()) + "," + str(w.getId()) + "," + str(vert.getWeight(w)) + ")")
    

    