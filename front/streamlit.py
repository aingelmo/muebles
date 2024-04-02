import requests
import streamlit as st

API_HOST = st.secrets["api_host"]


def format_option(option):
    if isinstance(option, dict) and "name" in option:
        return option["name"]
    else:
        return str(option)


st.title("API for the model")

available_articles = requests.get(f"http://{API_HOST}/articles/all").json()

article_names = [article["name"] for article in available_articles]

desired_article = st.selectbox(
    "Desired article", available_articles, index=None, format_func=format_option
)

if not desired_article:
    st.error("Please select an article")
    st.stop()

article = requests.get(f"http://{API_HOST}/articles/{desired_article["doc_id"]}").json()


# Use the format_func parameter to display only the names
desired_material = st.selectbox(
    "Desired material", article["materials"], format_func=format_option
)
desired_material_cost = desired_material["price"]


desired_finishing = st.selectbox(
    "Desired finishing", article["finishings"], format_func=format_option
)
desired_finishing_cost = desired_finishing["price"]

desired_dimensions = st.selectbox(
    "Desired dimensions", article["dimensions"], format_func=format_option
)
desired_dimensions_cost = desired_dimensions["price"]

st.write(f"Material cost: {desired_material_cost}")
st.write(f"Finishing cost: {desired_finishing_cost}")
st.write(f"Dimensions cost: {desired_dimensions_cost}")

st.write(
    f"The total cost is: {desired_material_cost + desired_dimensions_cost + desired_finishing_cost}"
)
