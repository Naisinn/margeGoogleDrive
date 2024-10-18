import os
import zipfile
from tqdm import tqdm

def extract_and_combine_zips(destination):
    print("Enter the paths of the ZIP files separated by 'Enter'. Type 'done' when finished:")

    zip_files = []
    while True:
        line = input().strip()
        if line.lower() == 'done':
            break
        # Remove double quotes and replace backslashes with forward slashes
        cleaned_line = line.strip('"').replace('\\', '/')
        zip_files.append(cleaned_line)

    if not zip_files:
        print("No ZIP files provided.")
        return

    if not os.path.exists(destination):
        print(f"Destination directory does not exist: {destination}")
        return

    # プログレスバーをZIPファイルの数で設定
    for zip_file in tqdm(zip_files, desc="Processing ZIP files", unit="file"):
        if not os.path.exists(zip_file):
            print(f"File not found: {zip_file}")
            continue

        try:
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                # 各ZIP内のファイル数でサブプログレスバーを設定（オプション）
                file_list = zip_ref.namelist()
                for file in tqdm(file_list, desc=f"Extracting {os.path.basename(zip_file)}", unit="file", leave=False):
                    zip_ref.extract(file, destination)
        except zipfile.BadZipFile:
            print(f"Bad ZIP file: {zip_file}")
            continue

    print("Extraction and combination complete.")

if __name__ == "__main__":
    dest = input("Enter the destination directory for extraction: ").strip()
    extract_and_combine_zips(dest)
