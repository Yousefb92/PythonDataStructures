from Stack.stack import Stack
from Queues.queue import Queue

inOrderResults = []
preOrderResults = []
postOrderResults = []
tArray = []

class Node:
    def __init__(self, val):
        self.llink = None
        self.rlink = None
        self.value = val

def treeDiag(root):
    inOrder(root)
    postOrder(root)
    preOrder(root)
    print("In Order Traversal: ",inOrderResults)
    print("Post Order Traversal: ",postOrderResults)
    print("Pre Order results: ",preOrderResults)
    getThreads(A, tArray)


def inOrder(root):
    if root:
        #print("Called on ",root.value)
        #First recur on left child
        inOrder(root.llink)

        #Print the value of the node
        inOrderResults.append(root.value)
        #print("Visiting: ",root.value)
        tArray.append(root)

        #recur on right child
        inOrder(root.rlink)

def postOrder(root):
    if root:
        #First recur on left child
        postOrder(root.llink)

        #Then recur on the right child
        postOrder(root.rlink)

        #Visit the value of the node
        postOrderResults.append(root.value)


def preOrder(root):
    if root:
        #print the data of the node
        preOrderResults.append(root.value)

        #Recur on the left child
        preOrder(root.llink)

        #Then recur on the right child
        preOrder(root.rlink)

def pretraverse(P):
    """
    Traverses our tree in pre order using a stack
    :param P:
    :return:
    """
    S = stack()
    while True:
        if P is not None:
            print(P.value, " visited")
            if P.rlink is not None:
                print(P.rlink.value, " added to stack")
                S.stack(P.rlink)
            P = P.llink
        else:
            if S.isEmpty():
                break
            P = S.unstack()


# function to find left most node in a tree
def leftMostNode(node):
    while (node != None and node.llink != None):
        node = node.llink
    return node


# function to find right most node in a tree
def rightMostNode(node):
    while (node != None and node.rlink != None):
        node = node.rlink
    return node

# recursive function to find the Inorder Successor
# when the right child of node x is None
def findInorderRecursive(root, x):
    """
    Given the root of a tree and a pointer to a node X, returns the in order successor
    of the node x (Right Thread)
    :param root:
    :param x:
    :return:
    """
    if x.rlink is None:
        if (not root):
            return None
        if (root == x or (findInorderRecursive(root.llink, x)) or
                (findInorderRecursive(root.rlink, x))):
            if findInorderRecursive(root.rlink, x):
                temp = findInorderRecursive(root.rlink, x)
            else:
                temp = findInorderRecursive(root.llink, x)
            if (temp):

                if (root.llink == temp):
                    print("Inorder Successor (Right Thread) of",
                          x.value, end="")
                    print(" is", root.value)
                    return None
            return root
        return None
    else:
        if (x.rlink != None):
            inorderSucc = leftMostNode(x.rlink)
            print("Inorder Successor (Right Thread) of", x.value,
                  "is", end=" ")
            print(inorderSucc.value)

def getThreads(root: Node, nodeList: list):
    for n in nodeList:
        if n.rlink is None:
            findInorderRecursive(root, n)
    for n in nodeList:
        if n.llink is None:
            x = inOrderResults.index(n.value)

            #So that we dont run for the first node visited in in-order i.e. the left most node
            if x > 0:
                print("Inorder Predecessor (Left Thread) of ", n.value," is ",inOrderResults[x-1])


A = Node("log")
B = Node("F")
A.llink = B
C = Node("-")
B.llink = C
D = Node("/")
C.llink = D

E = Node("n")
F = Node("k")
G = Node("4")
D.rlink = F
D.llink = E
E.rlink = G


Sq = Node("Sqrt")
secondN = Node("N")
x = Node("x (mult)")
S = Node("5")
K = Node("k")

C.rlink = Sq
Sq.llink = secondN
Sq.rlink = x
x.llink = S
S.rlink = K


treeDiag(A)


