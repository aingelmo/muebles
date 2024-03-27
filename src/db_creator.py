import sqlite3
from pathlib import Path

import pandas as pd

ROOT_DIR = Path(__file__).parents[1]
DATA_DIR = ROOT_DIR / "data"
CSV_DIR = DATA_DIR / "csv"

DB_NAME = "data.db"


def csv_to_sqlite(csv_file: Path, table_name: str, conn: sqlite3.Connection):
    df = pd.read_csv(csv_file)
    df.to_sql(table_name, conn, if_exists="replace", index=False)


if __name__ == "__main__":
    conn = sqlite3.connect(DATA_DIR / DB_NAME)
    cursor = conn.cursor()
    for csv_file in CSV_DIR.glob("*.csv"):
        table_name = csv_file.stem
        csv_to_sqlite(csv_file, table_name, conn)
