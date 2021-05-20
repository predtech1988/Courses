# Stack Implementation (Linked Lists)


class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class Stack:
    def __init__(self) -> None:
        self.top = None
        self.bottom = self.top
        self.length = 0

    def peek(self):
        if self.length:
            print(self.top.data)
            return
        else:
            print("Stack is empty!")

    def push(self, value):
        new_node = Node(data=value)
        if not (self.top):
            self.top = new_node
            self.bottom = self.top
            self.length += 1
            return
        new_node.next = self.top
        self.top = new_node
        self.length += 1
        return

    def pop(self):
        if self.length == 0:
            self.bottom = None
            print("Stack is empty")
            return
        else:
            self.top = self.top.next
            self.length -= 1

    def print_list(self):
        if self.top is None:
            print("Stack is empty")
            return
        iterator = self.top
        linked_lists = ""
        while iterator:
            linked_lists += str(iterator.data) + "-->"
            iterator = iterator.next
        print(linked_lists)

    def test(self):
        print(self.top.next)


my_stack = Stack()
# my_stack.push(10)
# my_stack.push(14)
# my_stack.push(16)
# my_stack.peek()
# my_stack.print_list()
# my_stack.pop()
# my_stack.pop()
# my_stack.pop()
# my_stack.peek()
# my_stack.print_list()
my_stack.push("Google")
my_stack.push("Udemy")
my_stack.push("Discrod")
my_stack.print_list()
my_stack.peek()
my_stack.pop()
my_stack.peek()
my_stack.print_list()
