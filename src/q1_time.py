import duckdb
import datetime
from typing import List, Tuple

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    con = duckdb.connect(database=':memory:')

    con.execute(f"""
        CREATE TABLE tweets AS 
        SELECT 
            CAST(SUBSTR(date, 1, 10) AS DATE) AS tweet_date,
            user['username'] AS username
        FROM read_parquet('{file_path}')
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

if __name__ == "__main__":
    file_path = "data/farmers.parquet"
    top_users = q1_time(file_path)
    print(top_users)