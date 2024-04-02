import requests
import streamlit as st

API_HOST = st.secrets["api_host"]

st.title("API for the model")

available_articles = requests.get(f"http://{API_HOST}/articles/all").json()

article_names = [article["name"] for article in available_articles]


desired_article_name = st.selectbox("Desired article", article_names)
desired_article_id = [
    article["doc_id"]
    for article in available_articles
    if article["name"] == desired_article_name
][0]

article = requests.get(f"http://{API_HOST}/articles/{desired_article_id}").json()


desired_material = st.selectbox("Desired material", article["materials"])
desired_material_cost = desired_material["price"]

desired_dimensions = st.selectbox("Desired dimensions", article["dimensions"])
desired_dimensions_cost = desired_dimensions["price"]

desired_finishing = st.selectbox("Desired finishing", article["finishings"])
desired_finishing_cost = desired_finishing["price"]

st.write(f"Material cost: {desired_material_cost}")
st.write(f"Dimensions cost: {desired_dimensions_cost}")
st.write(f"Finishing cost: {desired_finishing_cost}")

st.write(
    f"The total cost is: {desired_material_cost + desired_dimensions_cost + desired_finishing_cost}"
)

st.json(article)
