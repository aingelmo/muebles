import database
from crud import ArticleSelector, DesiredArticle, Dimensions, Finishings, Materials
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/articles/all")
def list_articles(session=Depends(get_db)):
    articles = ArticleSelector().list_articles(session)
    if not articles:
        raise HTTPException(status_code=404, detail="Articles not found")
    return articles


@app.get("/articles/{article_name}")
def get_article_id(article_name: str, session=Depends(get_db)):
    article_id = ArticleSelector().find_article_id(article_name, session)
    if not article_id:
        raise HTTPException(status_code=404, detail="Article not found")
    return article_id


@app.get("/articles/id/{article_id}")
def list_possibilities(article_id: int, session=Depends(get_db)):
    materials = Materials(article_id=article_id).list_materials(session)
    finishings = Finishings(article_id=article_id).list_finishings(session)
    dimensions = Dimensions(article_id=article_id).list_dimensions(session)
    return {"materials": materials, "finishings": finishings, "dimensions": dimensions}


@app.get("/materials/{article_id}/{material_name}")
def get_price_material(article_id: int, material_name: str, session=Depends(get_db)):
    price = Materials(article_id=article_id).seek_price(material_name, session)
    if not price:
        raise HTTPException(status_code=404, detail="Material not found")
    return price


@app.get("/finishing/{article_id}/{finishing_name}")
def get_price_finishing(article_id: int, finishing_name: str, session=Depends(get_db)):
    price = Finishings(article_id=article_id).seek_price(finishing_name, session)
    if not price:
        raise HTTPException(status_code=404, detail="Finishing not found")
    return price


@app.get("/dimensions/{article_id}/l={length}&w={width}&t={thickness}")
def get_price_dimensions(
    article_id: int, length: int, width: int, thickness: int, session=Depends(get_db)
):
    dimensions = (length, width, thickness)
    price = Dimensions(article_id=article_id).seek_price(dimensions, session)
    if not price:
        raise HTTPException(status_code=404, detail="Dimensions not found")
    return price
