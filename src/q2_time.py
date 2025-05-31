import duckdb
import emoji
from collections import Counter
from typing import List, Tuple

def extract_emojis(text):
    return [char for char in text if char in emoji.EMOJI_DATA]

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    df = duckdb.query(f"SELECT content FROM read_parquet('{file_path}')").to_df()

    all_emojis = []

    for content in df['content'].dropna():
        all_emojis.extend(extract_emojis(content))

    counter = Counter(all_emojis)
    return counter.most_common(10)

if __name__ == "__main__":

    file_path = "data/farmers.parquet"
    print(q2_time(file_path))
