from datetime import datetime
from . import linkedList

def dataToLinkedList():
    boxes = linkedList.BoxList()

    with open('data.txt', 'r', encoding='UTF-8') as fp:
        data = fp.readlines()

    for one in data:
        one = one.split(',')
        temp = linkedList.Node(one[0], one[1], one[2], one[3])
        boxes.append(temp)
        
    return boxes
    
def linkedListToData(boxes):
    boxes = getBoxes(boxes)
    with open('data.txt', 'w', encoding='UTF-8') as fp:
        for box in boxes:
            data = f'{ box.name },{ box.studentNumber },{ box.date },{ box.time },\n'
            fp.write(data)

def getBoxes(boxes):
    boxesList = []
    temp = boxes.head

    while(temp != None):
        boxesList.append(temp)
        temp = temp.link

    return boxesList


def findByStudentNumber(boxes, query):
    boxesList = []
    temp = boxes.head

    while(temp != None):
        if temp.studentNumber == query:
            boxesList.append(temp)
        temp = temp.link

    return boxesList

def setBox(boxes, name, studentNumber):
    now = datetime.now()
    date = now.strftime('%y%m%d')
    time = now.strftime('%H:%M')
    box = linkedList.Node(name, studentNumber, date, time)
    boxes.append(box)
    linkedListToData(boxes)
    
    return

def deleteBoxById(boxes, id):
    boxes.delete(id)
    linkedListToData(boxes)

    return