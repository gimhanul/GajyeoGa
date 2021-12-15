from flask import render_template, request, Blueprint
from . import linkedListService

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/', methods=['DELETE', 'GET', 'POST'])
def index():
    boxes = linkedListService.dataToLinkedList()
    query = request.args.get('search', '')
    sort = 'time'
    abc = '1'

    if request.method == 'POST':
        data = request.get_json('sort')
        sort = data['sort']
        abc = data['abc']
        print(data)
        that = linkedListService.getSortedBoxes(boxes, sort, abc)
        
        for i in that:
            print(i.name)

        return render_template('index.html', boxes=that, search=query, abc=abc, sort=sort)
        print("return이 안 되니?시발")
    
    if request.method == 'DELETE':
        data = request.get_json('id')
        linkedListService.deleteBoxById(boxes, (int)(data['id']))

    if query == '':
        that = linkedListService.getBoxesAsTime(boxes)
    else:
        that = linkedListService.findByStudentNumber(boxes, query)
    
    return render_template('index.html', boxes=that, search=query, abc=abc, sort=sort)


@main.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        boxes = linkedListService.dataToLinkedList()
        name = request.form['name']
        studentNumber = request.form['studentNumber']

        if name == '' or studentNumber == '':
            return '값을 입력해 주세요.'
        linkedListService.setBox(boxes, name, studentNumber)

    return render_template('register.html')