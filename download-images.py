import os
import csv
import requests

def download_images_from_csv(csv_filename="images.csv", output_folder="images"):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the CSV file
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row

        for i, row in enumerate(reader, start=1):
            if len(row) < 4:
                print(f"Row {i} skipped: not enough columns")
                continue

            image_url = row[3].strip()
            if not image_url:
                print(f"Row {i} skipped: empty URL")
                continue

            try:
                response = requests.get(image_url, timeout=10)
                response.raise_for_status()

                # Extract filename from URL
                filename = os.path.basename(image_url.split("?")[0])
                filepath = os.path.join(output_folder, filename)

                with open(filepath, "wb") as f:
                    f.write(response.content)

                print(f"Downloaded: {filename}")
            except Exception as e:
                print(f"Failed to download image from {image_url} (Row {i}): {e}")

if __name__ == "__main__":
    download_images_from_csv()