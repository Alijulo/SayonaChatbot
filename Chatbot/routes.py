from flask import Blueprint,request,jsonify
from chatbot.chat import chat_response;

routes=Blueprint('routes',__name__)

@routes.route('/chat',methods=['POST'])
def lets_chat():
    text=request.get_json().get('message')
    respose=chat_response(text)
    return jsonify(respose)

