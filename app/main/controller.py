from flask import render_template, request, Blueprint

from app.main.domain import linkedList
from . import linkedListService

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/', methods=['DELETE', 'GET', 'POST'])
def index():
    boxes = linkedListService.dataToLinkedList()
    query = request.args.get('search', '')
    sort = ''
    abc = 0

    if request.method == 'POST':
        sort = request.form['sort']
        abc = request.form['abc']
    
    if request.method == 'DELETE':
        data = request.get_json('id')
        linkedListService.deleteBoxById(boxes, (int)(data['id']))

    if query == '':
        if sort == 'studentNumber':
            that = linkedListService.getBoxesAsStudentNumber(boxes)
        elif sort == 'name':
            that = linkedListService.getBoxesAsName(boxes)
        else:
            that = linkedListService.getBoxesAsTime(boxes)
        if abc == '0':
            that.reverse()
    else:
        that = linkedListService.findByStudentNumber(boxes, query)
    
    return render_template('index.html', boxes=that, search=query)


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