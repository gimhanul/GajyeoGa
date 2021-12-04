def getBoxes():

    boxes = []
    with open('data.txt', 'r', encoding='UTF-8') as fp:
        data = fp.readlines()

    for one in data[1:]:
        temp = dict()
        one = one.split(',')
        temp['name'] = one[0]
        temp['studentNumber'] = one[1]
        temp['recievedDate'] = one[2]

        boxes.append(temp)
        
        
    return boxes