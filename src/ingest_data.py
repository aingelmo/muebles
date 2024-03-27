from pathlib import Path

import pandas as pd
from sqlalchemy import Engine, create_engine
from sqlalchemy.exc import IntegrityError

# Define the root directory and database name
ROOT_DIR = Path(__file__).parents[1]
DATA_DIR = ROOT_DIR / "data"
CSV_DIR = DATA_DIR / "csv"


# Function to import a CSV file into a SQLite database
def csv_to_sqlite(csv_file: Path, table_name: str, engine: Engine):
    if table_name == "articles":
        df = pd.read_csv(csv_file, index_col=0)
    else:
        df = pd.read_csv(csv_file, encoding="latin_1")

    df.to_sql(table_name, engine, if_exists="append", index=False)
    try:
        df.to_sql(table_name, engine, if_exists="append", index=False)
    except IntegrityError:
        print(f"Error importing {csv_file} into {table_name}")


# Main script
if __name__ == "__main__":
    engine = create_engine("postgresql://postgres:example@localhost:5432/muebles")

    # Iterate over CSV files and import them into the database
    for csv_file in CSV_DIR.glob("*.csv"):
        csv_to_sqlite(csv_file, csv_file.stem, engine)
