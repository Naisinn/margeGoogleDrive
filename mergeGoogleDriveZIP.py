import os
import zipfile

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

    for zip_file in zip_files:
        if not os.path.exists(zip_file):
            print(f"File not found: {zip_file}")
            continue

        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(destination)

    print("Extraction and combination complete.")

if __name__ == "__main__":
    dest = input("Enter the destination directory for extraction: ").strip()
    extract_and_combine_zips(dest)
