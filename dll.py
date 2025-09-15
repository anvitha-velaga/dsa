class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=new_node
            new_node.prev=curr
    def display_forward(self):
        curr=self.head
        while curr:
            print(curr.data, end="<->")
            curr=curr.next
        print("none")
    def display_backward(self):
        curr=self.head
        if curr is None:
            return
        while curr.next:
            curr=curr.next
        while curr:
            print(curr.data, end="<->")
            curr=curr.prev
        print("none")
dll=dll()
dll.insert_end('10')
dll.insert_end('20')
dll.insert_end('30')
dll.display_forward()
        