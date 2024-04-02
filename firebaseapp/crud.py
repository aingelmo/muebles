from firebase_admin import credentials, firestore, initialize_app

# Initialize Firebase Admin SDK
cred = credentials.Certificate("sa.json")
initialize_app(cred)
db = firestore.client()


def get_unique_items():
    collection_ref = db.collection("articles")
    docs = collection_ref.stream()

    articles = []
    for doc in docs:
        name = doc.get("name")
        doc_id = doc.id
        if name:
            articles.append({"name": name, "doc_id": doc_id})

    if not articles:
        raise Exception("Articles not found")

    return articles


def get_document(collection_name, document_id):
    doc_ref = db.collection(collection_name).document(document_id)
    doc = doc_ref.get()
    if doc.exists:
        # Convert the document data to a dictionary
        document_data = doc.to_dict()
        return document_data
    else:
        raise Exception("Document not found")
