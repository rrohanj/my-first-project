class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CircularLinkedList:
    def __init__(self):
        self.head=None
    def insert_beginning(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new_node
            new_node.next=self.head
            self.head=new_node
    def delete_end(self):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.next == self.head: 
            self.head = None
            return
        temp = self.head
        prev = None
        while temp.next != self.head:
            prev = temp
            temp = temp.next
        prev.next = self.head 
        temp = None 
    def display(self):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        while True:
            print(temp.data,end="->")
            temp=temp.next
            if temp==self.head:
                break
        print("Head")
csll=CircularLinkedList()
csll.insert_beginning(1)
csll.insert_beginning(2)
csll.insert_beginning(3)
csll.display()
csll.delete_end()
csll.display()
