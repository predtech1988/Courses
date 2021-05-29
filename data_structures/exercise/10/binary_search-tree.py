class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        flag = True
        if not (self.root):
            self.root = Node(value)
            return
        new_node = Node(value)
        current_node = self.root
        while flag:
            if value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                    continue
                else:
                    current_node.left = new_node
                    flag = False
                    return
            if value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                    continue
                else:
                    current_node.right = new_node
                    flag = False
                    return

    def lookup(self, value):
        flag = True
        current_node = self.root
        # while not (current_node.value == None):
        while flag:
            if current_node == None:
                print(f"Value {value} not found")
                flag = False
                return False
            if value == current_node.value:
                # print(f"Value {value} Found")
                return current_node
            if value < current_node.value:
                current_node = current_node.left
                continue
            if value > current_node.value:
                current_node = current_node.right
                continue

    def print_tree(self):
        if self.root != None:
            self.printt(self.root)

    # Inorder Traversal (We get sorted order of elements in tree)

    def printt(self, curr_node):
        if curr_node != None:
            self.printt(curr_node.left)
            print(str(curr_node.value))
            self.printt(curr_node.right)


my_tree = BinarySearchTree()
my_tree.insert(9)
my_tree.insert(4)
my_tree.insert(15)
my_tree.insert(3)
my_tree.insert(10)
my_tree.insert(17)
my_tree.insert(16)
# my_tree.print_tree()
# my_tree.lookup(10)
my_tree.print_tree()
