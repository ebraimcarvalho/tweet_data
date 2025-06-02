import os
import time
import duckdb
from pathlib import Path

def convert_json_to_parquet(json_path = "data/farmers-protest-tweets-2021-2-4.json", parquet_path = "data/farmers.parquet"):
    start = time.perf_counter()

    CURRENT_FOLDER = Path(__file__).resolve()
    PROJECT_ROOT = CURRENT_FOLDER.parent.parent

    if not os.path.exists(f"{PROJECT_ROOT}/{parquet_path}"):
        print("🔄 Converting JSON to Parquet...")

        duckdb.sql(f"""
            COPY (
                SELECT * FROM read_json_auto('{json_path}')
            ) TO '{parquet_path}' (FORMAT PARQUET)
        """)

        print("✅ Parquet file created:", parquet_path)
    else:
        print("✅ Parquet file already exists.")

    end = time.perf_counter()

    print(f"Elapsed: {end - start:.4f} seconds")

if __name__ == "__main__":
    convert_json_to_parquet()
