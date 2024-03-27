from dataclasses import dataclass

import pandas as pd
from config import POSTGRES_SETTINGS
from sqlalchemy import URL, Engine, create_engine


@dataclass
class Materials:
    article_id: int

    def list_materials(self, engine: Engine) -> list[str] | None:
        query = f"""SELECT DISTINCT name FROM materials WHERE article_id = {self.article_id};"""
        result = pd.read_sql_query(query, engine)
        if result.empty:
            return None
        return result["name"].tolist()

    def seek_price(self, name: str, engine: Engine) -> float | None:
        query = f"""SELECT price FROM materials WHERE name = '{name}' AND article_id = {self.article_id};"""
        result = pd.read_sql_query(query, engine)
        if result.empty:
            return None
        return result.iloc[0, 0]


@dataclass
class Finishings:
    article_id: int

    def list_finishings(self, engine: Engine) -> list[str] | None:
        query = f"""SELECT DISTINCT name FROM finishings WHERE article_id = {self.article_id};"""
        result = pd.read_sql_query(query, engine)
        if result.empty:
            return None
        return result["name"].tolist()

    def seek_price(self, name: str, engine: Engine) -> float | None:
        query = f"""SELECT price FROM finishings WHERE name = '{name}' AND article_id = {self.article_id};"""
        result = pd.read_sql_query(query, engine)
        if result.empty:
            return None
        return result.iloc[0, 0]


@dataclass
class Dimensions:
    article_id: int

    def list_dimensions(self, engine: Engine) -> dict[int, tuple[int, int, int]] | None:
        query = f"""SELECT length, width, thickness FROM dimensions WHERE article_id = {self.article_id};"""
        result = pd.read_sql_query(query, engine)
        if result.empty:
            return None
        return {
            idx: (row[0], row[1], row[2])
            for idx, row in enumerate(result.itertuples(index=False))
        }

    def seek_price(
        self, dimensions: tuple[int, int, int], engine: Engine
    ) -> float | None:
        query = f"""SELECT price FROM dimensions WHERE article_id = {self.article_id} AND length = {dimensions[0]} AND width = {dimensions[1]} AND thickness = {dimensions[2]};"""
        result = pd.read_sql_query(query, engine)
        if result.empty:
            return None
        return result.iloc[0, 0]


class ArticleSelector:
    def __init__(self) -> None:
        pass

    def _list_articles(self, engine: Engine) -> list[str] | None:
        query = """SELECT DISTINCT name FROM articles;"""
        result = pd.read_sql_query(query, engine)
        if result.empty:
            return None
        return result["name"].tolist()

    def _find_article_id(self, article_name: str, engine: Engine) -> int | None:
        query = f"""SELECT id FROM articles WHERE name = '{article_name}';"""
        result = pd.read_sql_query(query, engine)
        if result.empty:
            return None
        return result.iloc[0, 0]


if __name__ == "__main__":
    connection_string = URL.create(
        "postgresql",
        username=POSTGRES_SETTINGS.user,
        password=POSTGRES_SETTINGS.password,
        host=POSTGRES_SETTINGS.host,
        database=POSTGRES_SETTINGS.db_name,
    )

    engine = create_engine(
        connection_string,
        connect_args={"sslmode": "require"},
    )

    articles_helper = ArticleSelector()
    articles_list = articles_helper._list_articles(engine)
    article_selection = input(
        f"Select an article from the following list: {articles_list}\n"
    )

    article_id = articles_helper._find_article_id(article_selection, engine)

    if article_id is None:
        print("Article not found")
        exit(1)

    material_helper = Materials(article_id)
    material_list = material_helper.list_materials(engine)
    material_selection = input(
        f"Select a material from the following list: {material_list}\n"
    )
    material_cost = material_helper.seek_price(material_selection, engine)
    print(f"Material cost: {material_cost}")

    finishing_helper = Finishings(article_id)
    finishing_list = finishing_helper.list_finishings(engine)
    finishing_selection = input(
        f"Select a finishing from the following list: {finishing_list}\n"
    )
    finishing_cost = finishing_helper.seek_price(finishing_selection, engine)
    print(f"Finishings cost: {finishing_cost}")

    dimension_helper = Dimensions(article_id)
    dimension_list = dimension_helper.list_dimensions(engine)
    dimension_selection = int(
        input(f"Select dimensions from the following list: {dimension_list}\n")
    )
    dimension_cost = dimension_helper.seek_price(
        dimension_list[dimension_selection], engine
    )

    print(f"Dimensions cost: {dimension_cost}")

    print(f"Total cost: {material_cost + finishing_cost + dimension_cost}")
