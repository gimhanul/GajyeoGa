class Node(object):
    def __init__(self, name, studentNumber, date, time, id):
        self.name = name
        self.studentNumber = studentNumber
        self.date = date
        self.time = time
        self.id = id
        self.link = None


class BoxList(object):
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

    def delete(self, id):
        if self.head == None or id < 0: 
            return -1
        elif id == 0:
            self.head = self.head.link
        else:
            temp = self.head
            preNode = None

            while temp.id != id:
                preNode = temp
                temp = temp.link

            preNode.link = temp.link


    def printAll(self):
        temp = self.head

        while(temp != None):
            print(temp.name)
            temp = temp.link

            if temp != None:
                print(" -> ")

    def getCount(self):
        return self.count


