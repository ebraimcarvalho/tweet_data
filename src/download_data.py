import gdown
import os
import time

def download_file_from_google_drive(file_id="1B-TywPDU-BBFbMFbrqy2v71FrFxUqsa7", target_file="farmers-protest-tweets-2021-2-4.json"):
    start = time.perf_counter()

    target_folder = "data"
    os.makedirs(target_folder, exist_ok=True)
    json_file_path = os.path.join(target_folder, target_file)

    url = f"https://drive.google.com/uc?id={file_id}"

    if not os.path.exists(json_file_path):
        print("⬇️ Downloading file...")
        gdown.download(url, output=json_file_path, quiet=False, fuzzy=True)
    else:
        print("✅ File already exists. Skipping download.")

    end = time.perf_counter()

    print(f"Elapsed: {end - start:.4f} seconds")

if __name__ == "__main__":
    download_file_from_google_drive()
