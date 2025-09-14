class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
       
    def insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("none")

l1=Linkedlist()
l1.insert(10)
l1.insert(20)
l1.insert(30)
l1.display()

