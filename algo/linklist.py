class Node():
    def __init__(self,data = None, prev = None,next = None):
        self.data = data
        self.prev = prev
        self.next = next

class doublelinklist():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node = Node(data, None, None)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node
    def remove(self,data):
        curr = self.head
        while curr is not None:
            if curr.data == data:
                if curr == self.head:
                    self.head = self.head.next
                else:
                    #a >> curr >> b a>>b
                    curr.prev.next = curr.next
                    
                if curr == self.tail:
                    #a >> curr
                    # curr.prev.next = None (same as last sentence)
                    self.tail = curr.prev
                else: 
                    #a >> curr>>b b.preb>a
                    curr.next.prev = curr.prev
            curr = curr.next
    def printout(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
        print('============')

    def hascicle(self):
        slow, fast = self.head,self.head
        while fast and slow:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
            
            

d = doublelinklist()
# d.append(1)
# d.append(2)
# d.append(3)
# d.append(4)
# d.printout()
# d.remove(2)
# d.printout()
# d.remove(4)
# d.printout()
# print(d.head.data)

d.append(1)
d.append(2)
d.append(3)
d.append(4)
#n1 = d.tail
d.append(5)
d.append(6)
#d.tail.next = n1
print(d.hascicle())



                



            
