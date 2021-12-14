def quickSort(list):
    if len(list) <= 1: return list
    pivot = list[len(list) // 2].studentNumber
    lessBay, equalBay, bigBay = [], [], []
    for i in list:
        if i.studentNumber < pivot: lessBay.append(i)
        elif i.studentNumber > pivot: bigBay.append(i)
        else: equalBay.append(i)
    return quickSort(lessBay) + equalBay + quickSort(bigBay)