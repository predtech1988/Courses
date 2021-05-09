class HashTable():
    def __init__(self, size):
        self.data = []
        for i in range(size):
            self.data.append([[None]])
        self.pointer = 0 #for set_ordered version


    def __hash_key__(self, key):
        self.hash = 0
        for char in key:
            self.hash += (ord(char) + len(key))
        return self.hash % len(self.data)


    def set_item_(self, key, value):
        self.address = self.__hash_key__(key)
        if (len(self.data[self.address][0]) == 1):
            self.data[self.address] = [[(key), value]]
        else:
            self.data[self.address].append([(key), value])


    def set_item_ordered(self, key, value):
        self.data[self.pointer] = [(key), value]
        if self.pointer < len(self.data) -1:
            self.pointer  += 1
        else:
            self.pointer = 0 #rewriting existing list


    def get_item(self, key):
        self.address = self.__hash_key__(key)
        for element in self.data[self.address]:
            if element[0] == key:
                return element[1]
        else:
            return "Wrong key!"


    def keys(self): #Work's only if there is no collisions 
        keys = []
        for i in range(len(self.data)):
            if not(self.data[i][0][0] == None):
                keys.append(self.data[i][0][0])
        return keys



my_hash = HashTable(50)
my_hash.set_item_("grapes", 1000)
my_hash.set_item_("car", 2)
my_hash.set_item_("apple", 11)
my_hash.set_item_("oranges", 99)

answer  = my_hash.get_item("apple")
print(answer)

answer = my_hash.get_item("car")
print(answer)

keys_list =my_hash.keys()
print(keys_list)
