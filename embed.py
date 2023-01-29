from flask import Blueprint, request
from langchain.embeddings import OpenAIEmbeddings, CohereEmbeddings, HuggingFaceEmbeddings

embed_bp = Blueprint('embed', __name__)

@embed_bp.route('/embed', methods=['POST'])
def embed():
    data = request.get_json()
    provider = data.get('provider')
    cohere_api_key = data.get('cohere_api_key')
    documents = data.get('documents')
    embeddings = None

    if provider == 'OpenAI':
        embeddings = OpenAIEmbeddings()
    elif provider == 'Cohere':
        embeddings = CohereEmbeddings(cohere_api_key=cohere_api_key)
    elif provider == 'Hugging_face':
        embeddings = HuggingFaceEmbeddings()
    else:
        return {'error': 'Invalid embedding provider'}, 400
        
    if not documents:
        return {'error': 'No documents provided'}, 400
    
    result = embeddings.embed_documents(documents)
    return {'result': result}, 200
