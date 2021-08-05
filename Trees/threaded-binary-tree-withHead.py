import json
class Node:
    def __init__(self, val):
        self.llink = None
        self.rlink = None
        self.value = val
        self.ltag = None
        self.rtag = None

def createHead():
    head = Node("HEAD")
    head.value = "HEAD"
    head.rlink = head
    head.rtag = 0
    head.llink = head
    head.ltag = 1
    return head

inOrderResults = []
nodes = []

def inOrder(root):
    if root:
        #First recur on left child
        inOrder(root.llink)

        #Print the value of the node
        inOrderResults.append(root.value)
        nodes.append(root)

        #recur on right child
        inOrder(root.rlink)

def addThreads(head,root,nodes):
    """
    Updates our nodes with thread information

    :param head: Head Noode
    :param root: Root node
    :param nodes: List of all nodes in our tree
    :return:
    """
    inOrder(root)
    for node in nodes:
        if node == nodes[0]:
            #This is our left most node, adding a pointer back to the head
            node.ltag = 1
            node.llink = head
        if node == nodes[-1]:
            #This is the last node we visit in order, adding a pointer back to the head
            node.rtag = 1
            node.rlink = head
            node.ltag = 1
            node.llink = nodes[-2]
        else:
            #No left child so llink points to in order predecessor
            if node.llink is None:
                x = nodes.index(node)
                node.ltag = 1
                node.llink = nodes[x-1]
            else:
                #Setting ltag to equal 0 as llink points to the left child
                node.ltag = 0

            #No right child so rlink should point to in order successor
            if node.rlink is None:
                x = nodes.index(node)
                node.rtag = 1
                node.rlink = nodes[x+1]
            else:
                #Setting rtag to 0 as rlink points to right child
                node.rtag = 0

    #Updating our head to point to root node
    head.ltag = 0
    head.llink = root

    info = {}

    #Returning thread information
    for n in nodes:

        info["Node: "+str(n.value)] = {}
        info["Node: "+str(n.value)]["ltag"] = n.ltag
        info["Node: " + str(n.value)]["rtag"] = n.rtag
        info["Node: " + str(n.value)]["Left Thread"] = n.llink.value
        info["Node: " + str(n.value)]["Right Thread"] = n.rlink.value
    print(json.dumps(info,sort_keys=True,indent=5))




#Sample code to create a binary tree without threads
head = createHead()
root = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")
H = Node("H")
J = Node("J")

root.llink = B
B.llink = D
root.rlink = C
C.llink = E
E.rlink = G
C.rlink = F
F.llink = H
F.rlink = J

#Function to add threads and visualise information
addThreads(head,root,nodes)