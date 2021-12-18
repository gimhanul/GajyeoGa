class Node(object):
    def __init__(self, id, name, studentNumber, content, date, time):
        self.id = id
        self.name = name
        self.studentNumber = studentNumber
        self.content = content
        self.date = date
        self.time = time
        self.link = None