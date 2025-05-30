import gdown
import json
import os

target_folder = "data"
os.makedirs(target_folder, exist_ok=True)
json_file_path = os.path.join(target_folder, "farmers-protest-tweets-2021-2-4.json")

file_id = "1B-TywPDU-BBFbMFbrqy2v71FrFxUqsa7"
url = f"https://drive.google.com/uc?id={file_id}"

if not os.path.exists(json_file_path):
    print("⬇️ Downloading file...")
    gdown.download(url, output=json_file_path, quiet=False, fuzzy=True)
else:
    print("✅ File already exists. Skipping download.")

data = []
with open(json_file_path, "r", encoding="utf-8") as f:
    for line in f:
        if line.strip():
            data.append(json.loads(line))

print("✅ JSON loaded successfully.")
print(data[0])
