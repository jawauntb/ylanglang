from flask import Flask
from flask_cors import CORS
from chatbot import chatbot_bp
# from generate_response import generate_response_bp
from vectordb import vectordb_blueprint
from embed import embed_bp
from gpt_index_api import index_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(chatbot_bp)
# app.register_blueprint(generate_response_bp)
app.register_blueprint(vectordb_blueprint)
app.register_blueprint(embed_bp)
app.register_blueprint(index_bp)

@app.route('/')
def index():
  return 'Hello from Flask!'

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)
