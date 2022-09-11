import Basics as bs
import heapq
import BoyerMoore as bm

class BasicAlgorithms:
    def __init__(self, list = [3, 2, 4, 1, 0], valueExist=False):
        self.list = list
        self.valueExist = valueExist

    # sorting algorithms
    
    # bubble sort used for small datasets harldy used, time complexity is quadratic O(n^2) in avg and worst case, 
    # linear O(n)  in best case 
    def bubbleSort(self, list):
        sorted_list = []
        for i in range(0, len(list) - 1):
            for j in range(0, len(list) - 1):
                    if list[j] > list[j + 1]:
                        temp = list[j]
                        list[j] = list[j + 1]
                        list[j + 1] = temp        
        sorted_list = list
        
        return sorted_list

    # Merge sort, fast and efficient algorithm, recursivly divides and sorts an array into sub-arrays then merges it. Time complexity is logarithmic 
    # O(nlog(n)) in avg and worst case.
    def mergeSort(self, list):
        sorted_list = []
        if len(list) > 1:
        #  mid is the point where the array is divided into two subarrays
            mid = len(list)//2
            left = list[:mid]
            right = list[mid:]

            self.mergeSort(left)
            self.mergeSort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    list[k] = left[i]
                    i += 1
                else:
                    list[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                list[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                list[k] = right[j]
                j += 1
                k += 1

        sorted_list = list
        return sorted_list
     
    def listPartition(slef, list, head,tail):
        i = ( head - 1 )
        pivot_element = list[tail] # pivot element
        for j in range(head , tail):
            if list[j] <= pivot_element:
                i = i + 1
                list[i],list[j] = list[j], list[i]
        list[i + 1], list[tail] = list[tail], list[i+1]
        return (i + 1)

    # Quick sort, fast and efficient algorithm, divides using pivot element into sub-array. Time complexity
    # Best and avg case O(nlog(n)) and worst case is O(n^2).
    def quickSort(self, list, head, tail):
        sorted_list = []
        if head < tail:
            part = self.listPartition(list, head, tail)
            self.quickSort(list, head, part - 1)
            self.quickSort(list, part + 1, tail)
        sorted_list = list
        return sorted_list

    
    #  Searching Algorithms
    
    # Binary search algo is performed in non-linear data structure. It runs on logarithmic time 
    # in worst and avg case O(log(n)) also known as logarithmic search. 
    def binarySearchTree(self, value, tree):
        node = tree
        exist = False
        while node != None:
            if value == node.data:
                exist = True
                print("Value Found!")
                break
            elif value < node.data:
                node = node.left_child
            elif value > node.data:
                node = node.right_child
        if exist == False:
            print("Value not found!")

    # Time Complexity of BFS = O(V+E) where V is vertices and E is edges.
    def breathFirstSearchGraph(self, g, u, v):
        visted = []
        next_nodes = [u]
        while len(next_nodes) > 0:
            next = next_nodes[0]
            next_nodes.pop(0)

            if next not in visted:
                visted.append(next)
                if next == v:
                    print("Found '"+ v +"' traversing through : "+ str(visted))
                else:
                    neighbours = list(g[next].getConnections())
                    ids = [next_nodes.append(idx.getId()) for idx in neighbours]
        print("Not found '"+ v +"' traversing through : "+ str(visted))
    
    # Time Complexity of DFS is also O(V+E) where V is vertices and E is edges.
    def depthFirstSearchGraph(self, g, u, v):
        visted = []
        next_nodes = [u]

        while len(next_nodes) > 0:
            next = next_nodes[0]
            next_nodes.pop(0)
            if next not in visted:
                visted.append(next)
                if next == v:
                    print("Found '"+ v +"' traversing through : "+ str(visted))
                else:
                    neighbours = list(g[next].getConnections())
                    ids = [next_nodes.insert(0, idx.getId()) for idx in neighbours]
        print("Not found '"+ v +"' traversing through : "+ str(visted))

    # Time Complexity of DFS is also O(V+E) where V is vertices and E is edges.
    def depthFirstSearchTree(self, tree):
        node_visted = []
        stack = bs.Stack()
        stack.push(tree)
        while(not stack.isEmpyty()):
            node = stack.pop()
            node_visted.append(node.data)
            if node.right_child is not None:
                stack.push(node.right_child)
            if node.left_child is not None:
                stack.push(node.left_child)
        return node_visted  

    # String Matching Algorithms
    # In the worst-case the performance of the Boyer-Moore-Horspool algorithm is O(mn),
    #  where m is the length of the substring and n is the length of the string. 
    # The average time is O(n).

    def boyerMoore(self, p, p_bm, t):
        #""" Do Boyer-Moore matching """
        i = 0
        occurrences = []
        while i < len(t) - len(p) + 1:
            shift = 1
            mismatched = False
            for j in range(len(p)-1, -1, -1):
                if p[j] != t[i+j]:
                    skip_bc = p_bm.bad_character_rule(j, t[i+j])
                    skip_gs = p_bm.good_suffix_rule(j)
                    shift = max(shift, skip_bc, skip_gs)
                    mismatched = True
                    break
            if not mismatched:
                occurrences.append(i)
                skip_gs = p_bm.match_skip()
                shift = max(shift, skip_gs)
            i += shift
        return occurrences    
    # Graph shortest path between nodes
    # time complexity to Θ ( | E | + | V | log ⁡ | V | ) in worst case
    def dijkstra(self, aGraph, start, target):
        print ('''Dijkstra's shortest path Algorithm''')
        # Set the distance for the start node to zero 
        start.set_distance(0)

        # Put tuple pair into the priority queue
        unvisited_queue = [v.get_distance() for v in aGraph]
        heapq.heapify(unvisited_queue)

        while len(unvisited_queue):
            # Pops a vertex with the smallest distance 
            uv = heapq.heappop(unvisited_queue)
            current = list([v for v in aGraph if v.get_distance() is uv])[0] or uv[1]
            current.set_visited()

            #for next in v.adjacent:
            for next in current.adjacent:
                # if visited, skip
                if next.visited:
                    continue
                new_dist = current.get_distance() + current.getWeight(next)
            
                if new_dist < next.get_distance():
                    next.set_distance(new_dist)
                    next.set_previous(current)
                    print ('updated : current = %s next = %s new_dist = %s' \
                            %(current.getId(), next.getId(), next.get_distance()))
                else:
                    print ('not updated : current = %s next = %s new_dist = %s' \
                            %(current.getId(), next.getId(), next.get_distance()))

            # Rebuild heap
            # 1. Pop every item
            while len(unvisited_queue):
                heapq.heappop(unvisited_queue)
            # 2. Put all vertices not visited into the queue
            unvisited_queue = [v.get_distance() for v in aGraph if not v.visited]
            heapq.heapify(unvisited_queue)

if __name__ == '__main__':
    algos = BasicAlgorithms()
    algos.quickSort(algos.list, 0, 4)
    print("Sorted list...")
    print(algos.list)
    print("Binary Search Tree..")

    tree = bs.BinaryTreeNode(None)
    # root
    root = tree.insert(None, 6)
    
    # left subtree                  #              6
    tree.insert(root, 5)            #          5       8
    # left left subtree
    tree.insert(root, 4)            #      4       7       9
    # left left left leaf node
    tree.insert(root, 3)            #   3
    
    # right subtree
    tree.insert(root, 8)
    # right left leaf node
    tree.insert(root, 7)
    # right right leaf node
    tree.insert(root, 9)

    # print("Inorder DFS (Binary Tree Traverse) left -> root -> right : ")
    print("DFS (Preorder traversed, Root -> Left -> Right) : "+ str(algos.depthFirstSearchTree(root)))

    # Graph  DSF and BSF
    graph = bs.Graph()
    graph.createGraph()

    algos.depthFirstSearchGraph(graph.vert_dict, "a", "c")

    t = 'GCTAGCTCTACGAGTCTA'
    p = 'TCTA'
    p_bm = bm.BoyerMoore(p, alphabet='ACGT')

    print(algos.boyerMoore(p, p_bm, t))

    algos.dijkstra(graph, graph.getVertex('a'), graph.getVertex('c')) 

    target = graph.getVertex('c')
    path = [target.getId()]
    graph.shortest(target, path)
    print ('The shortest path : %s' %(path[::-1]))