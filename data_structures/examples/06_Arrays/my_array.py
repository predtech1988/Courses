class MyArray():
    def __init__(self):
        self.length = 0
        self.data = {}


    def get(self, index):
        return self.data[index]


    def push(self, item):
        self.data[self.length] = item
        self.length +=1
        return self.length

    #Instead of "self.data.pop(self.length-1)" need to use "del self.data[self.length-1]"
    def pop(self):
        self.last_item = self.data[self.length-1]
        self.data.pop(self.length-1)
        self.length -=1
        return self.last_item


    def shift_items(self, index):
        for i in range(index, self.length -1):
            self.data[i] = self.data[i+1]


    #Need to make generator, and redo it later with __iter__
    def iterate(self):
        for key, item in self.data.items():
            print(key, item)


    def delete(self, index):
        self.shift_items(index)
        self.data.pop(self.length-1)
        self.length -=1


test_array = MyArray()
test_array.push("Hello")
test_array.push("World")
test_array.push("!!!")
test_array.iterate()
test_array.delete(1)
test_array.iterate()
