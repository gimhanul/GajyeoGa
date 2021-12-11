from flask import Flask, redirect, render_template, request, url_for, Blueprint
from . import works

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def main():
    boxes = works.getboxes()
    context = {
        'boxes' : boxes,
    }

def register():
    return

def recieve():
    return

def myBox():
    myBox = works.findMyBox()
    context = {
        'myBox' : myBox,
    }