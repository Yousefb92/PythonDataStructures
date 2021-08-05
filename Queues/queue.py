"""
Simple array based implementation of a queue, handy for sanity checkng
"""
class Queue:
    def __init__(self):
        self.data = []
        self.size = 0

    def __len__(self):
        print(self.size)

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            raise ("Queue is Empty")
        else:
            return self.data[self.front]

    def unqueue(self):
        """
        Remove and return the first element of the Queue using FIFO
        :return:
        """
        if self.is_empty():
            raise ("Queue is Empty")
        else:
            print("Un-queue operation performed")
            x = self.data[0]
            self.data.remove(self.data[0])
            self.size -= 1
            return x

    def __str__(self):
        print("Front",self.data,"Rear")

    def enqueue(self, e):
        """
        Add an element to the rear of the queue
        :param e: The element to be added
        :return: Null
        """
        print("Queue Operation performed")
        self.data.append(e)
        self.size += 1