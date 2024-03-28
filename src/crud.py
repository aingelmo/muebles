from dataclasses import dataclass

import models
from models import Article, Dimension, Finishing, Material
from sqlalchemy.orm import Session


def get_article(db: Session, article_id: int):
    return db.query(models.Article).filter(models.Article.id == article_id).first()


@dataclass
class Materials:
    article_id: int

    def list_materials(self, session) -> list[str] | None:
        materials = (
            session.query(Material.name)
            .filter(Material.article_id == self.article_id)
            .distinct()
            .all()
        )
        if not materials:
            return None
        return [material[0] for material in materials]

    def seek_price(self, name: str, session) -> float | None:
        material = (
            session.query(Material.price)
            .filter(
                Material.name == name,
                Material.article_id == self.article_id,
            )
            .first()
        )
        return material[0] if material else None


@dataclass
class Finishings:
    article_id: int

    def list_finishings(self, session) -> list[str] | None:
        finishings = (
            session.query(Finishing.name)
            .filter(Finishing.article_id == self.article_id)
            .distinct()
            .all()
        )
        if not finishings:
            return None
        return [finishing[0] for finishing in finishings]

    def seek_price(self, name: str, session) -> float | None:
        finishing = (
            session.query(Finishing.price)
            .filter(Finishing.name == name, Finishing.article_id == self.article_id)
            .first()
        )
        return finishing[0] if finishing else None


@dataclass
class Dimensions:
    article_id: int

    def list_dimensions(self, session) -> dict[int, tuple[int, int, int]] | None:
        dimensions = (
            session.query(Dimension.length, Dimension.width, Dimension.thickness)
            .filter(Dimension.article_id == self.article_id)
            .all()
        )
        if not dimensions:
            return None
        return {idx: (row[0], row[1], row[2]) for idx, row in enumerate(dimensions)}

    def seek_price(self, dimensions: tuple[int, int, int], session) -> float | None:
        dimension = (
            session.query(Dimension.price)
            .filter(
                Dimension.length == dimensions[0],
                Dimension.width == dimensions[1],
                Dimension.thickness == dimensions[2],
                Dimension.article_id == self.article_id,
            )
            .first()
        )
        return dimension[0] if dimension else None


class ArticleSelector:
    def __init__(self) -> None:
        pass

    def list_articles(self, session) -> list[str] | None:
        articles = session.query(Article.name).distinct().all()
        if not articles:
            return None
        return [article[0] for article in articles]

    def find_article_id(self, article_name: str, session) -> int | None:
        article_id = (
            session.query(Article.id).filter(Article.name == article_name).first()
        )
        return article_id[0] if article_id else None
