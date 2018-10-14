# A stack is an ordered collection of items where the insertion of new item and the removal of 
# existing item takes place at the same end.

# Items that are closer to the base means those the longest.

class Stack():
    def __init__(self):
        self.items = []
    def push(self,new_item):
        self.items.append(new_item)
    def pop(self):
        if len(self.items)==0:
            return None
        return  self.items.pop()
    def isEmpty(self):
        return len(self.items) == 0 
    def peak(self):
        if self.isEmpty == True:
            return None
        else:
            return self.items[-1]

# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# print(s.pop())
# print(s.pop())
# print(s.peak())
# print(s.items)
