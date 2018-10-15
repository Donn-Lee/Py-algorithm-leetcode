class queue():
    def __init__(self):
        self.items = []
    def enquence(self,v): 
        self.items.append(v)
    def isEmpty(self):
        return len(self.items)== 0
    def dequence(self):
        if self.isEmpty():
            return None
        return self.items.pop(0)
    def peak(self):
        if self.isEmpty():
            return None
        return self.items[0]

q = queue()
q.enquence(1)
q.enquence(2)
q.enquence(3)
q.dequence()
q.dequence()
print(q.peak())