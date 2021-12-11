from flask import Flask, redirect, render_template, request, url_for, Blueprint
from . import works

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/', methods=['POST', 'GET'])
def index():
    boxes = works.dataToLinkedList()
    query = request.args.get('search', '')

    
    if request.method == 'POST':
        data = request.get_json('id')
        print(data['id'])
        works.deleteBoxById(boxes, (int)(data['id']))


    if query == '':
        that = works.getBoxes(boxes)
        that.reverse()
    else:
        that = works.findByStudentNumber(boxes, query)
    
    return render_template('test.html', boxes=that, search=query) #최태영거완성되면수정

@main.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        boxes = works.dataToLinkedList()
        name = request.form['name']
        studentNumber = request.form['studentNumber']
        works.setBox(boxes, name, studentNumber)

    return render_template('registerTest.html')