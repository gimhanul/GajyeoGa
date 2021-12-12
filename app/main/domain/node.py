class Node(object):
    def __init__(self, name, studentNumber, date, time, id):
        self.name = name
        self.studentNumber = studentNumber
        self.date = date
        self.time = time
        self.id = id
        self.link = None