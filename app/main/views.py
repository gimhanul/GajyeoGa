from flask import Flask, redirect, render_template, request, url_for, Blueprint
from . import works

main = Blueprint('main', __name__, url_prefix='/')
boxes = works.dataToLinkedList()

@main.route('/')
def index():
    nowBoxes = works.getBoxes(boxes)
    return render_template('test.html', boxes=nowBoxes) #최태영거완성되면수정

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