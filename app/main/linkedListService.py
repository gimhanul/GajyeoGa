from datetime import datetime
from .domain import linkedList
from .domain import node
from .util import mergeSort
from .util import quickSort


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
    boxes = getBoxesAsTime(boxes)
    with open('data.txt', 'w', encoding='UTF-8') as fp:
        for box in boxes:
            data = f'{ box.name },{ box.studentNumber },{ box.date },{ box.time },{ box.id },\n'
            fp.write(data)


#Boxes To List
def getSortedBoxes(boxes, sort, abc):
    if sort == 'studentNumber':
        that = getBoxesAsStudentNumber(boxes)
    elif sort == 'name':
        that = getBoxesAsName(boxes)
    else:
        that = getBoxesAsTime(boxes)

    if abc == '1':
        that.reverse()
    
    return that


def getBoxesAsTime(boxes):
    boxesList = []
    temp = boxes.head

    while(temp != None):
        boxesList.append(temp)
        temp = temp.link

    return boxesList

def getBoxesAsStudentNumber(boxes):
    boxesList = getBoxesAsTime(boxes)
    boxesList = quickSort.quickSort(boxesList)
    return boxesList

def getBoxesAsName(boxes):
    boxesList = getBoxesAsTime(boxes)
    boxesList = mergeSort.mergeSort(boxesList)
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