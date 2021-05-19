#From YT video
class Node:
    def __init__(self, value = None) -> None:
        self.value = value
        self.next_node = None        

class LinkedList:
    def __init__(self) -> None:
        self.head  = Node()
        self.length = 1

    
    def append(self, data):
        self.length +=1
        new_node = Node(data)
        current = self.head
        while current.next_node != None:
            current = current.next_node
        current.next_node = new_node

test = LinkedList()
test.append(333)
test.append(74)
test.append(99)
