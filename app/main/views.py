from flask import Flask, redirect, render_template, request, url_for, Blueprint
from . import works

main = Blueprint('main', __name__, url_prefix='/')
boxes = works.dataToLinkedList()

@main.route('/')
def index():
    query = request.args.get('search', '')
    if query == '':
        that = works.getBoxes(boxes)
    else:
        that = works.findByStudentNumber(boxes, query)
    
    return render_template('test.html', boxes=that) #최태영거완성되면수정

'''
def register():
    return

def recieve():
    return

def myBox():
    myBox = works.findMyBox()
    context = {
        'myBox' : myBox,
    }
'''