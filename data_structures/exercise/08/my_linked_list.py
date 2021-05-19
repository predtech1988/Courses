class Node():
    def __init__(self, data = None, next = None) -> None:
        self.data = data
        self.next = next

class LinkedList():
    """
    Implementation of linked list.
access(index) - access element by index.\n
print_list - print's all element's in the list\n
append(data) - append's data to the end of the list\n
prepend(data) - append's data to the beggining of the list\n
__lookup__ - function for internal use only\n
insert(data, index) - inserts data at the given index\n 
remove(index) - remove's data at the given index\n 
    """
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


    def append (self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
            self.length += 1
            return
        else:
            #O(1)
            new_node = Node(data)
            self.tail.next  = new_node
            self.tail = new_node
            self.length += 1
            #O(n)
            # iterator = self.head
            # while iterator.next:
            #     iterator = iterator.next
            # iterator.next = Node(data)
            #self.length += 1


    def prepend(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        new_node = Node(data, self.head)
        self.head = new_node
        self.length += 1
        return


    def __lookup__(self, index):
        iterator = self.head 
        i = 0
        while  i < index:
            if i+1 == index:
                return iterator
            iterator = iterator.next
            i +=1


    def insert(self, index, data):
        #Cheking length of Linked list
        if index >= self.length:
            print("Out of range! Insert in to the end of list? y / n")
            answer = input().lower()
            if answer == "y":
                self.append(data)
                return
            return
        #If index == 0 or less, we attach data before head
        if index <= 0:
            self.prepend(data)
            return

        #Inserting code
        current_node = self.__lookup__(index)
        new_node = Node(data, current_node.next)
        current_node.next = new_node


    def access(self, index):
        if index >= self.length:
            print("Out of range!")
            return
        print(self.__lookup__(index + 1).data)


    def remove(self, index):
        if index >= self.length:
            print("Out of range!")
            return
        #Need more check's for index, and make separete function for checking...
        prev_node = self.__lookup__(index)
        current_node = self.__lookup__(index +1)
        prev_node.next = current_node.next
        self.length -= 1


    def reverse(self):
        if not(self.head):
            return self.head
        first = self.head
        self.tail = self.head
        second = first.next
        while(second):
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None
        self.head = first
        self.print_list()
#self.__lookup__(index+1)
test_list = LinkedList()
#test_list.print_list()
test_list.append(14)
#test_list.print_list()
test_list.prepend(10)
#test_list.print_list()
test_list.append(16)
test_list.append(22)
#test_list.print_list()
#test_list.insert(2, 90)
#test_list.print_list()
#test_list.access(3)
test_list.print_list()
#test_list.remove(2)
#test_list.print_list()
test_list.reverse()