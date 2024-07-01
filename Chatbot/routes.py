from flask import Blueprint

routes=Blueprint('routes',__name__)

@routes.route('/',methods=['POST'])
def lets_chat():
    return "hello there!"
