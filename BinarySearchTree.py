from IPython.core.display import display
from graphviz import Digraph
from IPython.display import Image
Image('digraph.png')

queue = []
counter = 0
class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val
        self.left_tag = None
        self.right_tag = None

class BinarySearchTree():
    def __init__(self,children: list):
        self.root = None
        if len(children) == 1:
            self.root = Node(children[0])
        else:
            self.root = Node(children[0])
            for x in range(1,len(children)):
                self.insert(node=Node(children[x]))

    def insert(self,node):
        if self.root is None:
            self.root = node
        else:
            if self.root.data > node.data:
                if self.root.l_child is None:
                    self.root.l_child = node
                else:
                    insert(self.root.l_child, node)
            else:
                if self.root.r_child is None:
                    self.root.r_child = node
                else:
                    insert(self.root.r_child, node)

    def render(self,filename: str):
        """
        Saves a visualisation of the tree in PNG format to the current working directory
        :param filename: Desired filename of the visualisation (does not need to include extension)
        """
        visualize_tree(self,filename)

    def deletion_p29(self,value):
        """
        Deletes a node from the tree and updates links accordingly
        :param value: Value that the node that is to be deleted contains in its 'data' field
        """
        bst_deletion_p29(self.root,value)

    ### TRAVERSAL TECHNIQUES
    def non_recursive_preorder(self, showStack: bool):
        """
        This function traverses the tree in Pre-Order non-recursively and prints the Node values to the console
        :param showStack: Set to True to see stack contents after each Node visit. Must be set to False otherwise
        :return:
        """
        print("Traversing the tree in non-recursive pre order")
        non_recursive_preorder(self.root, showStack)

    def post_order_traversal(self):
        print("Traversing the given tree in Post-Order")
        post_order_print(self.root)

    def in_order_traversal(self):
        print("Traversing the given tree in In-Order")
        in_order_print(self.root)





def non_recursive_preorder(root, showStack):
    stack = []
    if showStack is None:
        showStack = False
    while True:
        if root != None:
            #Printing is us visting the Node
            print("Visiting Node: "+str(root.data))
            if showStack:
                print("Stack Contents")
                for n in stack:
                    print(n.data)
                #print('\n')
            stack.append(root)
            root = root.l_child
        else:
            if(stack == []):
                return
            else:
                root = stack.pop()
                root = root.r_child


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                insert(root.r_child, node)

def post_order_print(root):
    if root:
        #First recurse on left child
        post_order_print(root.l_child)
        #Then recurse on the right child
        post_order_print(root.r_child)
        #Printing Value
        print(root.data)


def in_order_print(root):

    if not root:
        return
    in_order_print(root.l_child)
    print(root.data)
    queue.append(root)
    in_order_print(root.r_child)

def bst_deletion_p29(root, value):
    A = root
    while A is not None and A.data != value:
        B = A
        A = A.l_child if (value < A.data) else A.r_child
    if(A is None):
        print("Exception: Value not found in tree")
    else:
        # A Points to the node to be deleted and B to its parent, unless A = Root
        # Now we look for C (perhaps nil) to replace A, and prepare for linking B to it
        if A.l_child is None:
            C = A.r_child
        elif A.r_child is None:
            C = A.l_child
        else:
            # Node A has two non-empty subtrees, so we make C the In Order Successor of A
            C = A.r_child
            if C.l_child is None:
                #C Inherits A's left subtree
                C.l_child = A.l_link
            else:
                while C.l_child is not None:
                    D = C
                    C = C.l_child # D is C's parent
                D.l_child = C.r_child # Link C's right subtree to D
                C.l_child = A.l_link #C inherits A's subtrees
                C.r_child = A.r_child
        #Lastly we link B to C
        if A == root:
            root = C
        elif B.l_child == A:
            B.l_child = C
        else:
            B.r_child = C

def pre_order_print(root):
    if not root:
        return
    print(root.data)
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)


def visualize_tree(tree,filename):
    def add_nodes_edges(tree, dot=None):
        # Create Digraph object
        if dot is None:
            dot = Digraph()
            dot.node(name=str(tree), label=str(tree.data))

        # Add nodes
        if tree.l_child:
            dot.node(name=str(tree.l_child), label=str(tree.l_child.data))
            dot.edge(str(tree), str(tree.l_child), " L")
            dot = add_nodes_edges(tree.l_child, dot=dot)

        if tree.r_child:
            dot.node(name=str(tree.r_child), label=str(tree.r_child.data))
            dot.edge(str(tree), str(tree.r_child)," R")
            dot = add_nodes_edges(tree.r_child, dot=dot)

        dot.render(filename=filename,format='png')
        return dot

    # Add nodes recursively and create a list of edges
    dot = add_nodes_edges(tree.root)

    # Visualize the graph
    #display(dot)

    return dot

# def list_to_bst(input):
#     r = Node(input[0])
#     for x in range(1,len(input)):
#         insert(r,Node(input[x]))
#     return r


# r = Node("matt")
# insert(r,Node('exam'))
# insert(r,Node('boar'))
# insert(r,Node('deci'))
# insert(r,Node('happ'))
# insert(r,Node('occa'))
# insert(r,Node('does'))
# insert(r,Node('supe'))
# insert(r,Node('thin'))
# insert(r,Node('that'))
# insert(r,Node('proj'))
# insert(r,Node('dese'))
# insert(r,Node('pass'))
# insert(r,Node('othe'))
# insert(r,Node('disa'))


#vis = visualize_tree(r,"Question1",'png')

# tree = list_to_bst(["Mark",'John','Sam','Fred','Leslie','Nigel','Tom','David','George','Kenneth','Neil','Oliver','Vic','Kurt','Neville','Peter','Kris','Lawrie','Orlando'])
# #visualize_tree(tree,"pre_deletion","png")
# bst_deletion_p29(tree,"David")
# visualize_tree(tree,"post deletion",'png')
