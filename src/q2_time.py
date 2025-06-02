import duckdb
import emoji
import time
from collections import Counter
from typing import List, Tuple
from pathlib import Path

def extract_emojis(text):
    return [char for char in text if char in emoji.EMOJI_DATA]

def q2_time(file_path: str) -> List[Tuple[str, int]]:

    CURRENT_FOLDER = Path(__file__).resolve()
    PROJECT_ROOT = CURRENT_FOLDER.parent.parent

    con = duckdb.connect()
    cur = con.cursor()

    query = f"SELECT content FROM read_parquet('{PROJECT_ROOT}/{file_path}')"
    cur.execute(query)

    contador = Counter()

    linha = cur.fetchone()
    while linha is not None:
        texto = linha[0]
        if texto:
            for char in texto:
                if char in emoji.EMOJI_DATA:
                    contador[char] += 1
        linha = cur.fetchone()
    
    return contador.most_common(10)

def execute():
    start = time.perf_counter()

    file_path = "data/farmers.parquet"
    print(q2_time(file_path))

    end = time.perf_counter()

    print(f"Elapsed: {end - start:.4f} seconds")

if __name__ == "__main__":
    execute()    
