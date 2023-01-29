from flask import Blueprint, request, jsonify
from langchain import OpenAI, ConversationChain
import os

chatbot_bp = Blueprint('chatbot', __name__)
key = os.environ['OPENAI_API_KEY']

llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm, verbose=True)

@chatbot_bp.route('/chatbot', methods=['POST'])
def chatbot():
    input_text = request.json['input_text']
    response = conversation.predict(input=input_text)
    return jsonify({'response': response})