# 232. Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/
class MyQueue:
    def __init__(self):
        self.one = []  # Using only to add (enqueue) new items
        self.two = []  # Using only to pop (dequeue) new items

    def push(self, x: int) -> None:  # enqueue
        """
        Push element x to the back of queue.
        """
        one = self.one
        one.append(x)

    def pop(self) -> int:  # dequeue
        """
        Removes the element from in front of queue and returns that element.
        """
        one = self.one
        two = self.two
        if not (len(two)):
            while len(one):  # Move all element's from 1st list, until length == 0
                tmp = one.pop()
                two.append(tmp)
            return two.pop()
        else:
            return two.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.two):
            return self.two[-1]
        else:
            return self.one[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if (len(self.one) == 0) and (len(self.two) == 0):
            return True
        else:
            return False

    def show(self):
        print(f"1st stack = {self.one},\n2nd stack = {self.two} ")


obj = MyQueue()
# obj.push(5)
# obj.push(2)
# obj.push(3)
# obj.show()
# obj.pop()
# obj.push(7)
# obj.push(9)
# obj.pop()
# obj.show()
# obj.pop()
# obj.show()
# obj.pop()
# obj.show()
obj.push(5)
obj.push(2)
print(obj.peek())
