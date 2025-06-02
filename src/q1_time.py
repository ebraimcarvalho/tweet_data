import duckdb
import datetime, time
from typing import List, Tuple
from pathlib import Path

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:

    CURRENT_FOLDER = Path(__file__).resolve()
    PROJECT_ROOT = CURRENT_FOLDER.parent.parent

    con = duckdb.connect(database=':memory:')

    con.execute(f"""
        CREATE TABLE tweets AS 
        SELECT 
            CAST(SUBSTR(date, 1, 10) AS DATE) AS tweet_date,
            user['username'] AS username
        FROM read_parquet('{PROJECT_ROOT}/{file_path}')
    """)

    query = """
    WITH tweet_counts AS (
        SELECT tweet_date, COUNT(1) AS cnt
        FROM tweets
        GROUP BY tweet_date
        ORDER BY cnt DESC
        LIMIT 10
    ),
    user_counts AS (
        SELECT tweet_date, username, count(1) AS tweet_count
        FROM tweets
        WHERE tweet_date IN (SELECT tweet_date FROM tweet_counts)
        GROUP BY tweet_date, username
    ),
    ranked_users AS (
        SELECT *,
            ROW_NUMBER() OVER (PARTITION BY tweet_date ORDER BY tweet_count DESC) AS rn
        FROM user_counts
        QUALIFY rn = 1
    )
    SELECT tweet_date, username
    FROM ranked_users
    ORDER BY tweet_count DESC
    """

    result = con.execute(query).fetchall()
    con.close()
    return result

def execute():
    start = time.perf_counter()

    file_path = "data/farmers.parquet"

    top_users = q1_time(file_path)

    print(top_users)

    end = time.perf_counter()

    print(f"Elapsed: {end - start:.4f} seconds")

if __name__ == "__main__":
    execute()