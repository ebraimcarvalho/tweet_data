import duckdb
from typing import List, Tuple
from pathlib import Path
from memory_profiler import profile

@profile
def q3_time(file_path):

    CURRENT_FOLDER = Path(__file__).resolve()
    PROJECT_ROOT = CURRENT_FOLDER.parent.parent
    
    query = f"""
        WITH mentions_extracted AS (
            SELECT REGEXP_EXTRACT_ALL(content, '@\\w+') AS mentions
            FROM read_parquet('{PROJECT_ROOT}/{file_path}')
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
    return duckdb.execute(query).fetchall()

def execute():

    file_path = "data/farmers.parquet"
    top_users = q3_time(file_path)
    print(top_users)

if __name__ == "__main__":
    execute()