import duckdb
import datetime
from typing import List, Tuple

def q3_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    query = """
        WITH mentions_extracted AS (
            SELECT REGEXP_EXTRACT_ALL(content, '@\\w+') AS mentions
            FROM read_parquet(?)
        ),
        mentions_flat AS (
            SELECT unnest(mentions) AS mention
            FROM mentions_extracted
        ),
        mentions_counted AS (
            SELECT mention, COUNT(*) AS count
            FROM mentions_flat
            GROUP BY mention
            ORDER BY count DESC
            LIMIT 10
        )
        SELECT REPLACE(mention, '@', '') as username_mentioned, count FROM mentions_counted
    """
    return duckdb.execute(query, [file_path]).fetchall()

if __name__ == "__main__":
    file_path = "data/farmers.parquet"
    top_users = q3_time(file_path)
    print(top_users)