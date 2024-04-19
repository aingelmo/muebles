from google.cloud.datastore import Client

from app.validation import Item, UniqueItemId

client = Client(project="muebles-chuchi")


def get_unique_items(collection_name: str = "articles") -> list[UniqueItemId]:
    """Get unique items from a collection"""
    collection_ref = client.query(kind=collection_name)
    docs = collection_ref.fetch()

    articles = [
        UniqueItemId(name=doc["name"], doc_id=doc["id"]) for doc in docs if doc["name"]
    ]

    if not articles:
        raise Exception("Articles not found")

    return articles


def get_document(collection_name: str, document_id: str) -> Item:
    """Get a document from a collection"""
    key = client.key(collection_name, document_id)
    entity = client.get(key)

    if entity is None:
        raise Exception("Document not found")

    return Item(**entity)
