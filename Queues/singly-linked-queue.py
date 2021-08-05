"""
Representing a queue using singly linked list representation
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



