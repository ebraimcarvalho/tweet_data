import os
import json
import pandas as pd

json_path = "data/farmers-protest-tweets-2021-2-4.json"
parquet_path = "data/farmers.parquet"

# If parquet already exists, skip
if not os.path.exists(parquet_path):
    print("🔄 Converting JSON to Parquet...")

    # Load JSON line by line
    data = []
    with open(json_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line))

    # Convert to DataFrame
    df = pd.DataFrame(data)
    df.to_parquet(parquet_path, index=False)

    print("✅ Parquet file created:", parquet_path)
else:
    print("✅ Parquet file already exists.")
