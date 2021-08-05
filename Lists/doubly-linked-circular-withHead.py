class Node:
    """
    Lightweight node, does not require any parameters to initiate
    """
    def __init__(self):
        self.info = None
        self.llink = None
        self.rlink = None

def getNode():
    return Node()

head = getNode()
head.rlink = head.info
head.llink = head.info

def leftInsert(head,y):
    """
    Insert value y at the left end of our list
    :param l:
    :param r:
    :param y: Value to insert in our list
    :return:
    """

    p = getNode()
    p.info = y
    p.llink = None
    p.rlink = head.rlink
    if head.rlink is None:
        head.llink = p
    else:
        head.rlink.llink = p
    head.rlink = p

def rightInsert(head,y):

    p = getNode()
    p.info = y
    p.rlink = None
    p.llink = head.llink
    if head.rlink is None:
        head.rlink = p
    else:
        head.llink.rlink = p
    head.llink = p

#TO DO, NO MORE RIGHT AND LEFT POINTERS, CHANGE ALGO TO USE HEAD
def leftDelete(l,r):
    """
    Returns the node at the left most end of our list
    :param l:
    :param r:
    :return: The node at the left most end of our list
    """
    global Left
    global Right
    if Left is None:
        print("Deal with Underflow")
        return None
    else:
        P = Left
        Left = P.rlink
        if Left is None:
            Right = None
        else:
            Left.llink = None
        Result = P.info
        #Release(P)
        return Result

def rightDelete(l,r):
    """
    Returns the right most node from our list
    :param l:
    :param r:
    :param y:
    :return: The node at the right most end of our list
    """
    global Left
    global Right
    if Right is None:
        print("Deal with Underflow")
        return None
    else:
        P = Right
        Right = P.llink
        if Right is None:
            Left = None
        else:
            Right.rlink = None
        Result = P.info
        #Release(P)
        return Result

def printCircular():
    global head
    r = []
    r.append(head.info)
    x = head.rlink
    while x is not None:
        r.append(x.info)
        x = x.rlink
    print("FRONT",r,"REAR")

leftInsert(head,"A")
printCircular()
leftInsert(head,"B")
printCircular()
leftInsert(head,"C")
printCircular()
rightInsert(head,"D")
rightInsert(head,"E")
leftDelete(Left,Right)
printCircular()
# rightDelete(Left,Right)
# printDeque()