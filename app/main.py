from typing import Any

from fastapi import FastAPI, HTTPException

from app.crud import get_document, get_unique_items

app = FastAPI()


@app.get("/articles/all")
async def get_all_articles() -> list[dict[str, str]] | None | HTTPException:
    """Get all articles from the Datastore."""
    try:
        return get_unique_items()
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.get("/articles/{document_id}")
async def get_article_info(
    document_id: str,
) -> dict[str, Any] | list[dict[str, Any]] | Any | HTTPException:
    """Get a specific article from the Datastore."""
    try:
        document_data = get_document("articles", document_id)
        return document_data
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
