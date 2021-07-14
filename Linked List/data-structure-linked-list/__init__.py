class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insertlast(self,newnode):
        if self.head is None:
            self.head=newnode
        else:
            tempnode=self.head
            while tempnode.next!=None:
                tempnode=tempnode.next
            tempnode.next = newnode
    def insertfirst(self,newnode):
        if self.head is None:
            self.head=newnode
        else:
            tempnode=self.head
            self.head=newnode
            self.head.next=tempnode
    def printnode(self):
        tempnode=self.head
        while 1:
            print(tempnode.data,end=" ")
            if tempnode.next is None:
                break
            tempnode = tempnode.next
n1=node("teja")
n2=node("krishna")
n3=node("sarvade")
l1=linkedlist()
l1.insertlast(n1)
l1.insertlast(n2)
l1.insertfirst(n3)
l1.printnode()

while 1:
    if tempnode.next is None:
        tempnode.next = newnode
        break
    tempnode = tempnode.next