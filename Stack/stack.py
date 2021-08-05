"""
Simple array based stack implementation
"""

class Stack:
    """Class must be initiated i.e. stack.Stack()"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def stack(self, item):
        print("Stack Operation Performed")
        return self.items.append(item)

    def unstack(self):
        print("Unstack Operation Performed")
        return self.items.pop()

    def peek(self):
        print(self.items[len(self.items)-1])
        return self.items[len(self.items)-1]

    def __len__(self):
        print(len(self.items))
        return len(self.items)

    def __str__(self):
        print("BOTTOM",self.items,"TOP")

