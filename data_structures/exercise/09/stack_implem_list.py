# Stack Implementation (List)


class Stack:
    def __init__(self) -> None:
        self.data = []

    def peek(self):
        print(self.data[-1])

    def push(self, value):
        self.data.append(value)

    def pop(self):
        self.data.pop()

    def print_list(self):
        lists = ""
        for item in self.data:
            lists += str(item) + "-->"
        print(lists)


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
