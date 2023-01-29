from flask import Blueprint, request
from gpt_index import GPTListIndex, GoogleDocsReader
from IPython.display import Markdown, display
import os

index_bp = Blueprint('gptindex', __name__)


@index_bp.route('/index_docs', methods=['POST'])
def index_docs():
  # make sure credentials.json file exists
  if not os.path.exists('credentials.json'):
    return 'credentials.json file not found, please provide a valid file', 400
  document_ids = request.json.get('document_ids')
  documents = GoogleDocsReader().load_data(document_ids=document_ids)
  index = GPTListIndex(documents)
  index.save_to_disk('index.json')
  return 'Index created and saved to disk', 200


@index_bp.route('/query_docs', methods=['GET'])
def query_index():
  index = GPTListIndex.load_from_disk('index.json')
  query_text = request.args.get('query_text')
  response = index.query(query_text, verbose=True)
  display(Markdown(f"<b>{response}</b>"))
  return response, 200
