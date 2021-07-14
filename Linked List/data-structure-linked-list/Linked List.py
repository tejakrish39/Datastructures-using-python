class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insertNodeAtLast(self,newnode):
        if self.head is None:
            self.head = newnode
        else:
            tempnode=self.head
            while tempnode.next!=None:
                tempnode=tempnode.next
            tempnode.next=newnode
    def insertAtFirst(self,newnode):
        if self.head is None:
            self.head = newnode
        else:
            tempnode = self.head
            self.head = newnode
            self.head.next = tempnode
    def findLength(self):
        tempnode=self.head
        count=0
        while tempnode!=None:
            count+=1
            tempnode=tempnode.next
        return count
    def printLinkedList(self):
        tempnode=self.head
        while tempnode!=None:
            print(tempnode.data,end=" ")
            tempnode=tempnode.next
        print("\n")

linkedList=LinkedList()
while 1:
    print("1 - Insert Node at Last\n2 - Insert Node at First\n3 - Find length of the list\n4 - Print the list\n5 - Break\nEnter Desired Value\n")
    n=int(input())
    if n == 1:
        print("Enter Value\n")
        value=int(input())
        node=Node(value)
        linkedList.insertNodeAtLast(node)
    elif n == 2:
        print("Enter Value\n")
        value = int(input())
        node = Node(value)
        linkedList.insertAtFirst(node)
    elif n == 3:
        print(linkedList.findLength())
    elif n == 4:
        linkedList.printLinkedList()
    elif n == 5:
        break
    else:
        pass

