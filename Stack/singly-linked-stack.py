"""
Stack representation using a singularly linked list
"""

class getNode:
    """
    Lightweight class for storing a singly linked node
    """

    __slots__ = '_info','_link'

    def __init__(self):
        self._info = None
        self._link = None


def Stack(T,y):
    """
    Insert item y on top of Stack T
    :param T: Pointer to the top of the stack, for an empty stack T is null
    :param y: The node to stack
    :return:
    """
    global Top #Global declarations are not needed when writing answers for exam
    P = getNode()
    P._info = y
    P._link = T
    Top = P

def Unstack(T):
    """
    Returns the top value from our stack T, removes node from stack and updates stack
    :param T: Pointer to top of stack
    :return: The node from the top of our stack
    """
    global Top #Global declarations are not needed when writing answers for exam
    if Top is None:
        print("Underflow: Stack is empty")
        return None
    else:
        P = Top
        Top = P._link
        Result = P._info
        return Result


def printStack():
    global Top
    X = Top
    print("Top of Stack")
    while X is not None:
        print(X._info)
        X = X._link
    print("Bottom of Stack")

Top = None #Top is nil when our stack is empty, following initialisation it will point to the top of our stack, often called first too

Stack(Top, "A")
Stack(Top,"B")
Stack(Top,"C")
Stack(Top,"D")
Stack(Top,"e")
printStack()

Unstack(Top)
Unstack(Top)
Unstack(Top)
printStack()