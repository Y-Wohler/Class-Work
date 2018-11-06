class Node():
    __data = None
    def __init__(self, data = None):
        self.__data = data
        self.next = None
    def getData(self):
        if self.__data == n1:
            print("£2.50")

        return self.__data

n1 = Node("Fish")
n2 = Node("Chips")
n1.next = n2
n3 = Node("Mushy Peas")
n2.next = n3

current = n1
while current:
    print(current.getData())
    current = current.next

