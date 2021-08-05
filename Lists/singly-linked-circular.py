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

    r = []
    x = PTR.link
    r.append(x.info)
    #print(x.info)
    y = x.link
    while y.info != x.info:
        #print(y.info)
        r.append(y.info)
        y = y.link
    print("TOP/Front",r,"BOTTOM/Rear")

LEFTINSERT(PTR,"A")
LEFTINSERT(PTR,"B")
LEFTINSERT(PTR,"C")
RIGHTINSERT(PTR,"A")
RIGHTINSERT(PTR,"D")

stringRep()
