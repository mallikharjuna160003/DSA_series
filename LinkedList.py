class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.last_node = None

    def insert(self,data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
            
    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next


def merge(h1, h2):
    print("h1",h1,"h2",h2)
    if h1.head is None:
        return h2.head
    if h2.head is None:
        return h1.head

    # start with the linked list
    # whose head data is the least
    if h1.head.data < h2.head.data:
        h1.head.next = merge(h1.head.next, h2.head)
        return h1.head

    else:
        h2.head.next = merge(h1.head, h2.head.next)
        return h2.head

if __name__ == "__main__":
    linkedL = LinkedList()

    linkedL.insert(10)

    linkedL.insert(20)
    linkedL.insert(30)
    linkedL.display()
    print("\n",linkedL.head.next.data)
    linkedL1 = LinkedList()
    linkedL1.insert(100)
    linkedL1.insert(200)
    linkedL1.insert(300)
    linkedL1 = merge(linkedL, linkedL1)
    print("\n")
    linkedL1.display()



























    
    
