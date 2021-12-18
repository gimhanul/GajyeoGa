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
        temp = node.Node(boxes.getCount(), one[1], one[2], one[3], one[4], one[5])
        print(temp)
        boxes.append(temp)
        
    return boxes
    
def linkedListToData(boxes):
    boxes = getBoxesAsTime(boxes)
    with open('data.txt', 'w', encoding='UTF-8') as fp:
        for box in boxes:
            data = f'{ box.id },{ box.name },{ box.studentNumber },{ box.content },{ box.date },{ box.time },\n'
            fp.write(data)


#Boxes To List
def getSortedBoxes(boxes, sort, abc):
    if sort == 'studentNumber':
        that = getBoxesAsStudentNumber(boxes)
    elif sort == 'name':
        that = getBoxesAsName(boxes)
    else:
        that = getBoxesAsTime(boxes)

    if abc == '0':
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
def setBox(boxes, name, studentNumber, content):
    now = datetime.now()
    date = now.strftime('%y%m%d')
    time = now.strftime('%H:%M')
    box = node.Node(boxes.getCount(), name, studentNumber, content, date, time)
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