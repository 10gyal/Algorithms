#AUTHOR- Tashi Tengyal (2020-15441) 
#As lot of algorithms in this program is refferred from CLRS
import time

#black = 0, red = 1 
class Node:
    def __init__(self, key):
        self.parent = None
        self.color = 1
        self.key = key
        self.left = None
        self.right = None
        self.size = 0

class Tree:
    def __init__(self):
        self.TNULL = Node(0)
        self.parent = self.TNULL
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL
        self.TNULL.size = 0

    def os_insert(self, key):
        if(self.search(self.root, key).key == key):
            return 0

        node = Node(key)
        node.parent = None
        node.key = key
        node.color = 1
        node.left = self.TNULL
        node.right = self.TNULL
        node.size = 1

        y = None
        x = self.root

        while x != self.TNULL:
            x.size += 1
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            node.size = node.right.size + node.left.size + 1
            return node.key

        if node.parent.parent == None:
            node.size = node.right.size + node.left.size + 1
            return node.key

        self.fix_insert(node)
        node.size = node.right.size + node.left.size + 1

        return node.key
    
    def fix_insert(self, z):
        while z.parent.color == 1:
            if z.parent == z.parent.parent.right:
                u = z.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    self.left_rotate(z.parent.parent)
            else:
                u = z.parent.parent.right

                if u.color == 1:
                    u.color = 0
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    self.right_rotate(z.parent.parent)
            if z == self.root:
                break
        self.root.color = 0


    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if(y.left != self.TNULL):
            y.left.parent = x

        y.parent = x.parent
        if(x.parent == None):
            self.root = y
        elif(x == x.parent.left):
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

        y.size = x.size
        x.size = x.left.size + x.right.size + 1

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if(y.right != self.TNULL):
            y.right.parent = x
        
        y.parent = x.parent
        if (x.parent == None):
            self.root = y
        elif (x == x.parent.right):
            x.parent.right = y
        
        else:
            x.parent.left = y
        
        y.right = x
        x.parent = y

        y.size = x.size
        x.size = x.left.size + x.right.size + 1

    def os_delete(self, node, key):
        if(self.search(node, key) == self.TNULL or self.search(node, key) == None):
            return 0
        z = self.TNULL
        while node != self.TNULL:
            if node.key == key:
                z = node

            if node.key <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            # print("Cannot find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            self.del_phase(z)
            x = z.right
            self.transplant(z, z.right)
        elif (z.right == self.TNULL):
            self.del_phase(z)
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.tree_min(z.right)
            self.del_phase(y)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
            y.size = y.right.size + y.left.size + 1
        if y_original_color == 0:
            self.fix_delete(x)
        
        return key

    def fix_delete(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 1:
                    w.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    w = x.parent.right

                if w.left.color == 0 and w.right.color == 0:
                    w.color = 1
                    x = x.parent
                else:
                    if w.right.color == 0:
                        w.left.color = 0
                        w.color = 1
                        self.right_rotate(w)
                        w = x.parent.right

                    w.color = x.parent.color
                    x.parent.color = 0
                    w.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 1:
                    w.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    w = x.parent.left

                if w.right.color == 0 and w.left.color == 0:
                    w.color = 1
                    x = x.parent
                else:
                    if w.left.color == 0:
                        w.right.color = 0
                        w.color = 1
                        self.left_rotate(w)
                        w = x.parent.left

                    w.color = x.parent.color
                    x.parent.color = 0
                    w.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0
    
    def os_select(self, node, i):
        if(node.size >= i):
            rank = node.left.size + 1
            if (i == rank):
                # print("Selected " + str(node.key))
                return node.key
            elif(i < rank):
                return self.os_select(node.left, i)
            else:
                return self.os_select(node.right, i-rank)
        else:
            # print("Selected 0")
            return 0

    def os_rank(self, key):
        node = self.search(self.root, key)
        if(node != self.TNULL):
            rank = node.left.size + 1
            y = node
            while(y != self.root):
                if(y == y.parent.right):
                    rank = rank + y.parent.left.size + 1
                y = y.parent
            # print("rank of " + str(key) + " is " + str(rank))
            return rank
        else: 
            # print("rank of " + str(key) + " is " + "0")
            return 0

    # def __repr__(self):
    #     lines = []
    #     print_tree(self.root, lines)
    #     return '\n'.join(lines)

    def search(self, node, key):
        if(node == self.TNULL or key == node.key):
            return node
        if(key < node.key):
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)
            
    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def tree_min(self, node):
        while (node.left != self.TNULL):
            node = node.left
        return node
    
    #decrements the size of each node on a path from the lowest node that moves to the root
    def del_phase(self, node):
        while(node != self.root):
            node = node.parent
            node.size -= 1

# # Prints a visual representation of the RB Tree
# def print_tree(node, lines, level=0):
#     if node.key != 0:
#         print_tree(node.right, lines, level + 1)
#         lines.append('-' * 4 * level + '> ' +
#                     str(node.key) + " *" + str(node.size) + " " + ('r' if node.color == 1 else 'b'))
#         print_tree(node.left, lines, level + 1)


#FUNCTIONS FOR CHECKER PROGRAM
def check_insert(arr, x):
    if(x not in arr):
        arr.append(x)
        return arr
    else:
        return [0]

def check_del(i_arr, d_arr, x):
    if(x in i_arr):
        i_arr.remove(x)
        d_arr.append(x)
        return d_arr
    else:
        return [0]

def check_sel(i_arr, s_arr, x):
    if(x <= len(i_arr)):
        tmp = i_arr
        tmp.sort()
        s_arr.append(tmp[x-1])
        return s_arr
    else: return [0]

def check_rank(i_arr, r_arr, x):
    if(x in i_arr):
        count = 0
        for i in range(len(i_arr)):
            if(i_arr[i] <= x):
                count += 1
        r_arr.append(count)
        return r_arr
    else:
        return [0]


def file_io(name):
    if(name == "input1/" or name == "input2/"):
        i_name = name + "input.txt"
        o_name = name + "output.txt"
        c_name = name + "checker.txt"

    else:
        i_name = name
        o_name = "output_for_" + name
        c_name = "checker_for_" + name    


    input_arr = []
    output_arr = []

    #FILE IO
    with open(i_name, 'r') as f:
        for line in f:
            data = line.split()
            input_arr.append(data)
            # print(data[0] + " " + data[1])
        # print(input_arr)

    tree = Tree()

    #Measuring time for RB tree algorithm
    startm = time.time()

    #------MAIN ALGO-----------
    for i in range(len(input_arr)):
        if(input_arr[i][0] == "I"):
            output_arr.append(tree.os_insert(int(input_arr[i][1])))
        elif(input_arr[i][0] == "D"):
            output_arr.append(tree.os_delete(tree.root, int(input_arr[i][1])))
        elif(input_arr[i][0] == "R"):
            output_arr.append(tree.os_rank(int(input_arr[i][1])))
        elif(input_arr[i][0] == "S"):
            output_arr.append(tree.os_select(tree.root, int(input_arr[i][1])))
    endm = time.time()-startm
    
    #prints the given input sequence and the corresponding output sequence
    # print(output_arr)

    # print(tree) ##prints a visual representation of rb tree

    with open(o_name, 'w') as f:
        for i in range(len(input_arr)):
            f.write(input_arr[i][0] + " " + input_arr[i][1] + "\n")
        for i in range(len(output_arr)):
            f.write(str(output_arr[i]) + "\n")
    
    #-----FOR CHECKER--------
    insert_arr = []
    del_arr = []
    sel_arr = []
    rank_arr = []
    checker_arr = []

    #Measuring time for checker
    startc = time.time()

    for i in range(len(input_arr)):
        if(input_arr[i][0] == "I"):
            checker_arr.append(check_insert(insert_arr, int(input_arr[i][1]))[-1])
        elif(input_arr[i][0] == "D"):
            checker_arr.append(check_del(insert_arr, del_arr, int(input_arr[i][1]))[-1])
        elif(input_arr[i][0] == "R"):
            checker_arr.append(check_rank(insert_arr, rank_arr, int(input_arr[i][1]))[-1])
        elif(input_arr[i][0] == "S"):
            checker_arr.append(check_sel(insert_arr, sel_arr, int(input_arr[i][1]))[-1])
    
    endc = time.time()-startc
    # print("Output: ")
    # print(checker_arr)

    #Checker comparison
    with open(c_name, 'w') as f:
        if(output_arr==checker_arr):
            f.write("CORRECT\n" + "Time taken by main algorithm: " + str(endm) + " s\n" + "Time taken by checker program: " + str(endc) + " s")
        else:
            f.write("INCORRECT")

#MAIN FUNCTION
def main():
    inst = int(input("To test my inputs press 1 and Enter. To test your own inputs press 2 and Enter. To quit, press 3 and Enter\n"))    
    while(inst != 3):
        if(inst == 1):
            file_io("input1/")
            file_io("input2/")
            break
        if(inst == 2):
            name = input("First make sure your test file is in the same directory as main.py. \nNext enter the file name inside quotation marks: ")
            file_io(name)
            break
    
main()











    




        








        
            
