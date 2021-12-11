from flask import Flask, redirect, render_template, request, url_for, Blueprint
from . import works

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def index():
    deleteBox = request.get_json()
    if deleteBox:
        works.deleteBoxById(deleteBox['id'])

    boxes = works.dataToLinkedList()
    query = request.args.get('search', '')
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