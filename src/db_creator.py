import sqlite3
from pathlib import Path

import pandas as pd

# Define the root directory and database name
ROOT_DIR = Path(__file__).parents[1]
DATA_DIR = ROOT_DIR / "data"
CSV_DIR = DATA_DIR / "csv"
DB_NAME = "data.db"


# Function to import a CSV file into a SQLite database
def csv_to_sqlite(csv_file: Path, table_name: str, conn: sqlite3.Connection):
    df = pd.read_csv(csv_file)
    # Assuming all IDs are integers, set the ID column as the primary key
    if "ID" in df.columns:
        df.to_sql(
            table_name,
            conn,
            if_exists="replace",
            index=False,
            dtype={"ID": "INTEGER PRIMARY KEY"},
        )
    else:
        df.to_sql(table_name, conn, if_exists="replace", index=False)


# Main script
if __name__ == "__main__":
    # Connect to the SQLite database
    conn = sqlite3.connect(DATA_DIR / DB_NAME)
    cursor = conn.cursor()

    # Iterate over CSV files and import them into the database
    for csv_file in CSV_DIR.glob("*.csv"):
        table_name = csv_file.stem
        csv_to_sqlite(csv_file, table_name, conn)

    # Close the connection
    conn.close()
