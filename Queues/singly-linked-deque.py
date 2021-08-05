"""
Representing a DEQUE using singly linked list representation
"""

class getNode:
    """
    Lightweight class for storing a singly linked node
    """

    __slots__ = 'info','link'

    def __init__(self):
        self.info = None
        self.link = None

F = None #F will be Nil/None for an empty list
R = None

def Queue(f,r,y):
    """
    Add item y to the rear of Queue<F,R>
    """
    global F
    global R

    P = getNode()
    P.info = y
    P.link = None
    if F is None:
        #Set our front pointer to point to the newly created node
        F = P
    else:
        #Updating the node that our last node points to to point to the new node created
        R.link = P
    #Setting our rear pointer to point to the newly created node
    R = P

def Unqueue(f,r):
    """
    Returning the value of the front node of our queue and removing it from the queue
    :param F: Front pointer to our queue
    :param R: Rear pointer to our queue

    :return: The value of the front node in our queue
    """
    global F
    global R
    if F is None:
        print("Underflow")
    else:
        P = F
        F = P.link
        Result = P.info
        #Release (P)
        return Result

def FrontInsert(f,r,y):
    """
    Insert item y at the front of our queue
    :param f:
    :param r:
    :param y:
    :return:
    """
    global F
    global R
    P = getNode()
    P.info = y
    P.link = F
    if F is None:
        #Dealing with boundary case
        R = P
    F = P

def RearDelete(f,r):
    """
    Return the node at the rear of our queue
    :param f:
    :param r:
    :return: Node at the back of our queue
    """
    #Note the inefficiency of using a singly linked list to do this
    global F, R
    if F is None:
        print("Deal with Underflow")
        return None
    else:
        P = R
        if F == R:
            F = None
        else:
            R = F
            while R.link != P:
                R = R.link
            R.link = None
        Result = P.info
        #Release(P)
        return Result

def printQueue():
    global F
    x = F
    R = []
    R.append(x.info)
    while x.link is not None:
        x = x.link
        R.append(x.info)
    print("FRONT",R,"REAR")



Queue(F,R,"A")
Queue(F,R,"B")
Queue(F,R,"C")
printQueue()
Unqueue(F,R)
printQueue()
FrontInsert(F,R,"X")
RearDelete(F,R)
printQueue()


