import sys
import time
sys.setrecursionlimit(10**6)

#Building Adjacency List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head =  None
    
    def add(self, end):
        new_node = Node(end)
        new_node.next = self.head
        self.head = new_node
    
    def search(self, x):
        current = self.head
  
        while current != None:
            if current.data == x:
                return True
            current = current.next
        return False

class AdjList:
    def __init__(self, v):
        self.v = v
        self.arr = []
        self.scc = []
        for i in range(v):
            a = LinkedList()
            self.arr.append(a)
    
    def add_edge(self, start, end):
        self.arr[start].add(end)

    def finder(self, start, v):
        return self.arr[start].search(v)
              
    def dfs(self, d, visited, ret_arr):
        visited[d] = True
        if(d != 0):
            # print(d, end='')
            ret_arr.append(d)
        
        for i in range(self.v):
            found = self.finder(i, d) 
            if(not visited[i] and found):
                self.dfs(i, visited, ret_arr)
        return ret_arr

    def fill_order(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in range(self.v):
            found = self.finder(i, d)
            if(not visited_vertex[i] and found):
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(d)

    def transpose(self):
        trans = AdjList(self.v)
        for i in range(self.v):
            tmp = self.arr[i].head
            while(tmp != None):
                trans.add_edge(tmp.data, i)
                tmp = tmp.next
        return trans

#Building Adjacency Matrix
class Mtx:

    def __init__(self, v):
        self.v = v
        self.graph = [[0 for i in range(v)] for j in range(v)]
        self.scc = []

    def add_edge(self, start, end):
        self.graph[start][end] = 1
    
    def dfs(self, start, visited, arr):
        visited[start] = True
        if(start != 0):
            # print(start, end=" ")
            arr.append(start)
        for i in range(self.v):
            if(self.graph[start][i] == 1 and not visited[i]):
                self.dfs(i, visited, arr)
        return arr

    def transpose(self):
        m = Mtx(self.v)
        for i in range(self.v):
            for j in range(self.v):
                if(self.graph[i][j] == 1):
                    m.add_edge(j, i)
        return m
    
    def fill_order(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in range(self.v):
            if not visited_vertex[i] and self.graph[d][i] == 1:
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(d)

#Building Adjacency Array
class AdjV:
    def __init__(self, no_of_adjv):
        self.no_of_adjv = no_of_adjv
        self.linked_arr = []

class AdjArr:
    def __init__(self, v):
        self.v = v
        self.arr = []
        self.scc = []
        for i in range(v):
            a = AdjV(0)
            self.arr.append(a)
    
    #arr = (a = (no_of_adjv, linked_arr = []))

    def add_edge(self, start, end):
        self.arr[start].no_of_adjv += 1
        self.arr[start].linked_arr.append(end)

    def dfs(self, d, visited, ret_arr):
        visited[d] = True
        if(d != 0):
            # print(d, end='')
            ret_arr.append(d)
        
        for i in range(self.v):
            if(not visited[i] and (d in self.arr[i].linked_arr)):
                self.dfs(i, visited, ret_arr)
        return ret_arr
    
    def fill_order(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in range(self.v):
            if(not visited_vertex[i] and (d in self.arr[i].linked_arr)):
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(d)
    
    def transpose(self):
        trans = AdjArr(self.v)
        for i in range(self.v):
            for j in range(len(self.arr[i].linked_arr)):
                trans.add_edge(self.arr[i].linked_arr[j], i)
        return trans

#Finiding the SCCs
def get_scc(graph):
    stack = []
    visited_vertex = [False] * (graph.v)

    for i in range(graph.v):
        if not visited_vertex[i]:
            graph.fill_order(i, visited_vertex, stack)

    gr = graph.transpose()

    visited_vertex = [False] * (graph.v)

    while stack:
        i = stack.pop()
        if not visited_vertex[i]:
            arr = []
            comp = gr.dfs(i, visited_vertex, arr)
            # print("")
            graph.scc.append(comp)
    #the last element is arbitrary        
    graph.scc.pop() 

#Lexicographic sorting
def lexi(scc_arr):
    a = []
    for i in range(len(scc_arr)):
        b = []
        for j in range(len(scc_arr[i])):
            b.append(str(scc_arr[i][j]))
        a.append(b)
    print("a: ")
    a.sort()
    return a

def main():
    fin = open(sys.argv[1], 'r')
    fout = open(sys.argv[2], 'w')
    gtype = sys.argv[3]
    n = int(fin.readline())

    if(gtype == "adj_list"):
        g = AdjList(n+1)
    elif(gtype == "adj_mat"):
        g = Mtx(n+1)
    elif(gtype == "adj_arr"):
        g = AdjArr(n+1)
    else:
        print("INVALID")
    
    for i, line in enumerate(fin.readlines()):
        v = line.split()
        for k in v[1:]:
            g.add_edge(i+1, int(k))

    
    start = time.time()
    get_scc(g)
    timetaken = time.time() - start


    # print(g.scc)

    for i in range(len(g.scc)):
        #sorted elements
        g.scc[i].sort()


    a = lexi(g.scc)
        
    for k in range(len(a)):
        for l in range(len(a[k])):
            fout.write((a[k][l]) + " ")
        fout.write("\n")
    fout.write(str(timetaken*1000) + "ms")
    print(timetaken)

main()   