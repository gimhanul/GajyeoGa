fp = open('data.txt', 'r', encoding='UTF-8')
data = fp.read()
fp.close()
print(data)

def getBoxes():
    return