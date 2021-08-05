class DeQueue:
    def __init__(self):
        self.data = []
        self.size = 0

    def __len__(self):
        print(self.size)

    def is_empty(self):
        return self.size == 0

    def left_Insert(self,e):
        self.data = [e] + self.data
        self.size += 1

    def left_Delete(self):
        x = self.data[0]
        self.data.remove(self.data[0])
        self.size -= 1
        return x

    def right_Insert(self,e):
        self.data.append(e)
        self.size += 1

    def right_Delete(self):

        x = self.data[(self.size)-1]
        self.data.remove(self.data[self.size-1])
        self.size -= 1
        return x


    def __str__(self):
        print("Front",self.data,"Rear")