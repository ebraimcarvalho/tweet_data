import duckdb
import emoji
from collections import Counter
from typing import List, Tuple
from pathlib import Path
from memory_profiler import profile

def extract_emojis(text):
    return [char for char in text if char in emoji.EMOJI_DATA]

@profile
def q2_time(file_path: str) -> List[Tuple[str, int]]:

    CURRENT_FOLDER = Path(__file__).resolve()
    PROJECT_ROOT = CURRENT_FOLDER.parent.parent

    df = duckdb.query(f"SELECT content FROM read_parquet('{PROJECT_ROOT}/{file_path}')").to_df()

    all_emojis = []

    for content in df['content'].dropna():
        all_emojis.extend(extract_emojis(content))

    counter = Counter(all_emojis)
    return counter.most_common(10)

def execute():

    file_path = "data/farmers.parquet"
    print(q2_time(file_path))

if __name__ == "__main__":
    execute()    
