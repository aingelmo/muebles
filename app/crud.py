from typing import Any

from google.cloud import datastore

client = datastore.Client(project="muebles-chuchi")


def get_unique_items(collection_name: str = "articles") -> list[dict[str, str]] | None:
    collection_ref = client.query(kind=collection_name)
    docs = collection_ref.fetch()

    articles = []
    for doc in docs:
        name = doc.get("name")
        doc_id = doc["id"]
        if name:
            articles.append({"name": name, "doc_id": doc_id})

    if not articles:
        raise Exception("Articles not found")

    return articles


def _entity_to_dict(
    entity: datastore.Entity | list[datastore.Entity] | Any,
) -> dict[str, Any] | list[dict[str, Any]] | Any:
    if isinstance(entity, datastore.Entity):
        return {key: _entity_to_dict(value) for key, value in entity.items()}
    elif isinstance(entity, list):
        return [_entity_to_dict(item) for item in entity]
    else:
        return entity


def get_document(collection_name: str, document_id: str):
    key = client.key(collection_name, document_id)
    entity = client.get(key)

    if entity is None:
        raise Exception("Document not found")

    return _entity_to_dict(entity)
