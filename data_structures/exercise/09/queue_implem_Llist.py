# Queue Implementation (Linked Lists).


class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class Queue:
    def __init__(self) -> None:
        self.first = None
        self.last = self.first
        self.length = 0

    def peek(self):
        if not (self.first):
            return None
        print(self.first.data)

    # Adds value to the end of the queue
    def enqueue(self, value):
        new_node = Node(value)
        if not (self.first):
            self.first = new_node
            self.last = self.first
            self.length += 1
            return
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1

    # Remove's value from the beggining of the queue
    def dequeue(self):
        if not (self.first):
            return None
        else:
            self.first = self.first.next
            self.length -= 1

    def print_list(self):
        if self.first is None:
            print("Queue is empty")
            return
        iterator = self.first
        linked_lists = ""
        while iterator:
            linked_lists += str(iterator.data) + "-->"
            iterator = iterator.next
        print(linked_lists)


my_queue = Queue()
my_queue.enqueue("Joy")
my_queue.enqueue("Matt")
my_queue.enqueue("Pavel")
my_queue.enqueue("Samir")
# my_queue.print_list()
# my_queue.peek()
my_queue.dequeue()
# my_queue.peek()
# my_queue.dequeue()
my_queue.dequeue()
print(my_queue.dequeue())
my_queue.peek()
my_queue.print_list()
