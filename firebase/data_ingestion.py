import json
from pathlib import Path

import firebase_admin
from firebase_admin import credentials, firestore

# Use a service account
cred = credentials.Certificate("sa.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Directory containing your JSON files
json_files_dir = Path(__file__).parents[1] / "data" / "json"

# Iterate over each JSON file in the directory
for json_file in json_files_dir.glob("*.json"):
    # Open and load the JSON file
    with open(json_file, "r") as file:
        data = json.load(file)

    # Assuming each JSON file contains a single article
    article_id = data["id"]
    article_name = data["name"]

    # Create a document in Firestore for the article
    doc_ref = db.collection("articles").document(json_file.stem)
    doc_ref.set(data)

    print(f"Imported {article_name} with ID {article_id} to Firestore.")
