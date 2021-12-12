from datetime import datetime
from .domain import linkedList
from .domain import node


#linkedList file 관리
def dataToLinkedList():
    boxes = linkedList.BoxList()

    with open('data.txt', 'r', encoding='UTF-8') as fp:
        data = fp.readlines()

    for one in data:
        one = one.split(',')
        temp = node.Node(one[0], one[1], one[2], one[3], boxes.getCount())
        boxes.append(temp)
        
    return boxes
    
def linkedListToData(boxes):
    boxes = getBoxes(boxes)
    with open('data.txt', 'w', encoding='UTF-8') as fp:
        for box in boxes:
            data = f'{ box.name },{ box.studentNumber },{ box.date },{ box.time },{ box.id },\n'
            fp.write(data)


#Boxes To List
def getBoxes(boxes):
    boxesList = []
    temp = boxes.head

    while(temp != None):
        boxesList.append(temp)
        temp = temp.link

    return boxesList


#setBox and append to linkedList
def setBox(boxes, name, studentNumber):
    now = datetime.now()
    date = now.strftime('%y%m%d')
    time = now.strftime('%H:%M')
    box = node.Node(name, studentNumber, date, time, boxes.getCount())
    boxes.append(box)
    linkedListToData(boxes)
    
    return


#Search
def findByStudentNumber(boxes, query):
    boxesList = []
    temp = boxes.head

    while(temp != None):
        if temp.studentNumber == query:
            boxesList.append(temp)
        temp = temp.link

    return boxesList


#Delete Box and linkedList
def deleteBoxById(boxes, id):
    boxes.delete(id)
    linkedListToData(boxes)

    return