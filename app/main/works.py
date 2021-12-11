import linkedList

def dataToLinkedList():

    boxes = linkedList.BoxList()

    with open('data.txt', 'r', encoding='UTF-8') as fp:
        data = fp.readlines()

    for one in data[1:]:
        one = one.split(',')
        temp = linkedList.Node(one[0], one[1], one[2])
        boxes.append(temp)
        
    boxes.printAll()
    #return boxes

dataToLinkedList()