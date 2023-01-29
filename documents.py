
def create_embeddings(docstore: InMemoryDocstore):
  # Initialize embeddings using the OpenAIEmbeddings model
  embeddings = OpenAIEmbeddings()

  # Iterate through the documents in the docstore and create embeddings for each one
  for doc_id, doc in docstore.items():
    doc.embedding = embeddings.embed_query(doc.text)

  return docstore


  
# Initialize an in-memory docstore
docstore = InMemoryDocstore()

@app.route("/upload_docs", methods=["POST"])
def upload_docs():
    # Get the documents from the request
    documents = request.json.get("documents")

    # Add the documents to the docstore
    docstore.add(documents)

    # Return a response indicating that the documents were successfully uploaded
    return jsonify({"message": "Documents uploaded successfully"})
