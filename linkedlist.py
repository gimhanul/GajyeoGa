class node(object):
    def __init__(self, data):
        self.data = data
        self.link = None


class boxList(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.link != None:
                temp = temp.link

            temp.link = node
            self.count += 1

    def insert(self, node, idx):
        if self.head == None: self.head = node
        elif idx == 0:
            node.link = self.head
            self.head = node
        elif idx < 0 or idx > self.count:
            return -1
        
        else:
            temp = self.head
            preNode = None

            for i in range(0, idx):
                preNode = temp
                temp = temp.link

            node.link = temp
            preNode.link = node

        self.count += 1

    def printAll(self):
        temp = self.head

        while(temp != None):
            print(temp.data)
            temp = temp.link

            if temp != None:
                print(" -> ")





