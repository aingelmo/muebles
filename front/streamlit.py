import requests
import streamlit as st

st.title("API for the model")

available_articles_request = requests.get("http://34.148.201.53/articles/all")
available_articles = available_articles_request.json()

desired_article = st.selectbox("Desired article", available_articles)

article_id_request = requests.get(f"http://34.148.201.53/articles/{desired_article}")
article_id = article_id_request.json()

possibilities_request = requests.get(f"http://34.148.201.53/articles/id/{article_id}")
possibilities = possibilities_request.json()


possible_dimensions = {
    "length": set(
        dimension["length"] for _, dimension in possibilities["dimensions"].items()
    ),
    "width": set(
        dimension["width"] for _, dimension in possibilities["dimensions"].items()
    ),
    "thickness": set(
        dimension["thickness"] for _, dimension in possibilities["dimensions"].items()
    ),
}


desired_material = st.radio("Desired material", possibilities["materials"])
desired_finishing = st.radio("Desired finishing", possibilities["finishings"])
desired_length = st.selectbox("Desired length", list(possible_dimensions["length"]))
desired_width = st.selectbox("Desired width", list(possible_dimensions["width"]))
desired_thickness = st.selectbox(
    "Desired thickness", list(possible_dimensions["thickness"])
)

materials_request = requests.get(
    f"http://34.148.201.53/materials/{article_id}/{desired_material}"
)
material_cost = materials_request.json()
st.write(f"Material cost: {material_cost}")

finishing_request = requests.get(
    f"http://34.148.201.53/finishing/{article_id}/{desired_finishing}"
)
finishing_cost = finishing_request.json()
st.write(f"Finishing cost: {finishing_cost}")

dimensions_request = requests.get(
    f"http://34.148.201.53/dimensions/{article_id}/l={desired_length}&w={desired_width}&t={desired_thickness}"
)
dimensions_cost = dimensions_request.json()
st.write(f"Dimensions cost: {dimensions_cost}")

total_cost = material_cost + finishing_cost + dimensions_cost
st.write(f"Total cost: {total_cost}")
