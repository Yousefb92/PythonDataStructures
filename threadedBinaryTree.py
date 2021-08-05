class Node:
    def __init__(self):
        self.info = None
        self.ltag = None
        self.llink = None
        self.rtag = None
        self.rlink = None

root = Node()
root.llink = root
root.ltag = 1
