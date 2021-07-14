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
    def insertAtIndex(self,index,newnode):
        count=0
        if index==0:
            self.insertAtFirst()
        else:
            tempnode=self.head
            count += 1
            while tempnode!=None:
                if count==index:
                    nextnode=tempnode.next
                    tempnode.next=newnode
                    newnode.next=nextnode
                    break
                tempnode=tempnode.next
    def findLengthUsingRecursion(self,tempnode):
        if tempnode == None:
            return 0
        else:
            tempnode=tempnode.next
            return 1+self.findLengthUsingRecursion(tempnode)
    def getRecursionCount(self):
        mainnode=self.head
        result=self.findLengthUsingRecursion(mainnode)
        return result
    def findLength(self):
        tempnode=self.head
        count=0
        while tempnode!=None:
            count+=1
            tempnode=tempnode.next
        return count
    def searchUsingRecursion(self,key,tempnode):
        if tempnode == None:
            return False
        else:
            if tempnode.data==key:
                return True
            else:
                return self.searchUsingRecursion(key,tempnode.next)
    def searchKey(self,key):
        mainnode=self.head
        if self.searchUsingRecursion(key,mainnode):
            return "Found"
        else:
            return "Not Found"
    def printLinkedList(self):
        tempnode=self.head
        while tempnode!=None:
            print(tempnode.data,end=" ")
            tempnode=tempnode.next
        print("\n")

linkedList=LinkedList()
while 1:
    print("1 - Insert Node at Last\n"
          "2 - Insert Node at First\n"
          "3 - Insert at Index\n"
          "4 - Find length of the list\n"
          "5 - Print the list\n"
          "6 - Search Key"
          "9 - Break\n"
          "Enter Desired Value\n")
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
        print("Enter Value\n")
        value = int(input())
        print("Enter Index\n")
        index=int(input())
        node = Node(value)
        linkedList.insertAtIndex(index,node)
    elif n == 4:
        print(linkedList.getRecursionCount())
    elif n == 5:
        linkedList.printLinkedList()
    elif n == 6:
        print("Enter Key\n")
        key=int(input())
        print(linkedList.searchKey(key))
    elif n == 9:
        break
    else:
        pass

