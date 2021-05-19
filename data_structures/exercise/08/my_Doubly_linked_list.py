class Node():
    def __init__(self,data = None, next = None, previous = None ):
        self.data = data
        self.next = next
        self.previous = previous


class DoublyLinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = self.head
        self.length = 0

    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        iterator = self.head
        linked_lists = ""
        while iterator:
            linked_lists += str(iterator.data) + "-->"
            iterator = iterator.next
        print(linked_lists)
        print(f"Tail data: {self.tail.data}")       #test


    def append (self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
            self.length += 1
            return
        else:
            #O(1)
            new_node = Node(data = data, previous=self.tail)  
            self.tail.next  = new_node
            self.tail = new_node
            self.length += 1
            #print(new_node.previous.data)


    def prepend(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        new_node = Node(data= data, next= self.head)
        self.head.previous = new_node
        self.head = new_node

    def __lookup__(self, index):
        iterator = self.head 
        i = 0
        while  i < index:
            if i+1 == index:
                return iterator
            iterator = iterator.next
            i +=1
        


    def insert(self, index, data):
        #if index < = 0 insert() if > length append()
        if index >= self.length:
            print("Out of range! Insert in to the end of list? y / n")
            return
        current_node = self.__lookup__(index)
        next_node = current_node.next
        new_node = Node(data = data 
                        ,next = current_node.next
                        ,previous = current_node)
        current_node.next = new_node
        next_node.previous = new_node
        self.length += 1


    def remove(self, index):
        #Add more check's for the index
        if index >= self.length:
            print("Out of range! Insert in to the end of list? y / n")
            return        
        current_node = self.__lookup__(index+1)
        prev_node = current_node.previous
        next_node = current_node.next
        prev_node.next = current_node.next
        next_node.previous = prev_node
        self.length -=1
        
        
    def print_reverse(self):
        node = self.tail
        i = self.length + 1
        while i > 0:
            print(node.data) 
            node = node.previous
            i-=1
        return



test_list = DoublyLinkedList()
#test_list.print_list()
test_list.append(14)
test_list.prepend(10)
test_list.append(16)
test_list.append(22)
#test_list.print_list()
#print(test_list.__lookup__(2).next.data)

#test_list.insert(2, 90)
test_list.print_list()
#print(test_list.__lookup__(3).data)
#test_list.print_reverse()
test_list.remove(2)
test_list.print_list()