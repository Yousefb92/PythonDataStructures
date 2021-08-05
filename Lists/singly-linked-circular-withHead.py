#Global pointer variable, referenced in latter functions
PTR = None

def getNode():
    return Node()

class Node:
    """
    Lightweight node, does not require any parameters to initiate
    """
    def __init__(self):
        self.info = None
        self.link = None

def LEFTINSERT(ptr, y):
    global PTR
    P = getNode()
    P.info = y

    if (PTR == None):
        PTR = P
    else:
        P.link = PTR.link

    PTR.link = P

def LEFTDELETE(ptr):
    global PTR
    if (PTR is None):
        raise Exception("Deal with Underflow")
    else:
        P = PTR.link
        if (PTR == P):
            #Setting our pointer to equal None if our structure contains a single node pointing to itself
            PTR = None
        else:
            PTR.link = P.link
        result = P.info
        return result

def RIGHTINSERT(ptr,y):
    global PTR
    LEFTINSERT(PTR,y)
    PTR = PTR.link


def stringRep():
    global PTR
    r = []
    x = head.link
    while x.info is not None:
        print(x.info)
        x = x.link
    print("TOP/Front",r,"BOTTOM/Rear")

#Setting head node
head = getNode()
head.link = head.info
PTR = head

LEFTINSERT(PTR,"A")
RIGHTINSERT(PTR,"B")
RIGHTINSERT(PTR,"C")
stringRep()




