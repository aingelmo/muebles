import sqlite3
from pathlib import Path

import pandas as pd

# Define the root directory and database name
ROOT_DIR = Path(__file__).parents[1]
DATA_DIR = ROOT_DIR / "data"
CSV_DIR = DATA_DIR / "csv"
DB_NAME = "data.db"


conn = sqlite3.connect(DATA_DIR / DB_NAME)
cursor = conn.cursor()

query = """
SELECT articulo,
       acabado,
       acabado.coste   AS coste_acabado,
       largo,
       ancho,
       espesor,
       dimension.coste AS coste_dimension,
       madera,
       material.coste  AS coste_material
FROM   articulo
       INNER JOIN acabado
               ON articulo.id = acabado.id_articulo
       INNER JOIN dimension
               ON articulo.id = dimension.id_articulo
       INNER JOIN material
               ON articulo.id = material.id_articulo 
"""
df = pd.read_sql_query(query, conn)
print(df)
