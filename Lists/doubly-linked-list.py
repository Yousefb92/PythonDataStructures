Left = None
Right = None

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

def leftInsert(l,r,y):
    """
    Insert value y at the left end of our list
    :param l:
    :param r:
    :param y: Value to insert in our list
    :return:
    """
    global Left
    global Right
    p = getNode()
    p.info = y
    p.llink = None
    p.rlink = Left
    if Left is None:
        Right = p
    else:
        Left.llink = p
    Left = p

def rightInsert(l,r,y):
    global Left
    global Right
    p = getNode()
    p.info = y
    p.rlink = None
    p.llink = Right
    if Left is None:
        Left = p
    else:
        Right.rlink = p
    Right = p

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

def printDeque():
    global Left
    r = []
    r.append(Left.info)
    x = Left.rlink
    while x is not None:
        r.append(x.info)
        x = x.rlink
    print("FRONT",r,"REAR")

leftInsert(Left,Right,"A")
printDeque()
leftInsert(Left,Right,"B")
printDeque()
rightInsert(Left,Right,"C")
printDeque()
rightDelete(Left,Right)
printDeque()