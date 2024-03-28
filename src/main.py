import database
from crud import ArticleSelector, Dimensions, Finishings, Materials

if __name__ == "__main__":
    session = database.SessionLocal()

    article = input(
        f"Enter the article name: {ArticleSelector().list_articles(session)}\n"
    )
    article_id = ArticleSelector().find_article_id(article, session) or exit()

    materials = Materials(article_id=article_id)
    material = input(f"Select material: {materials.list_materials(session)}\n")
    material_price = (
        materials.seek_price(material, session) if material is not None else exit()
    )
    print(f"Price: {material_price}")

    finishings = Finishings(article_id=article_id)
    finishing = input(f"Select finishing: {finishings.list_finishings(session)}\n")
    finishing_price = (
        finishings.seek_price(finishing, session) if finishing is not None else exit()
    )
    print(f"Price: {finishing_price}")

    dimensions = Dimensions(article_id=article_id)
    dimension_list = dimensions.list_dimensions(session)
    dimension = int(input(f"Select dimension: {dimension_list}\n"))
    dimension_price = (
        dimensions.seek_price(dimension_list[dimension], session)
        if dimension_list
        else exit()
    )
    print(f"Price: {dimension_price}")

    print(f"Total price: {material_price + finishing_price + dimension_price}")  # type: ignore
