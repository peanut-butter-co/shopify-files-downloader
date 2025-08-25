# Bulk Image Downloader

This project provides a simple Python script to download images in bulk from a CSV file.  
It is designed to work with a **Files Matrixify export** (with all columns selected).  
The script looks at the **4th column** of the CSV, where image URLs are stored, and downloads them automatically.

---

## Requirements

- Python 3.x (recommended) or Python 2.7
- The [`requests`](https://pypi.org/project/requests/) library

Install dependencies with:

```bash
pip install requests
```

---

## Usage

1. Place your CSV file in the same folder as the script and name it:

```
images.csv
```

This CSV should be an export from **Matrixify**, with **all columns selected**.

2. Run the script:

For Python 3:

```bash
python3 download-images.py
```

For Python 2 (if still in use):

```bash
python download-images.py
```

3. The script will:

- Create a subfolder called `images` (if it doesn’t already exist).  
- Read the 4th column of the CSV (excluding the header row).  
- Download all images from the URLs found there.  
- Save them inside the `images` folder, using the filename from the URL.  

---

## Notes

- If the same filename appears multiple times in the CSV, the latest download will overwrite the previous one.  
- If you need to keep duplicates, you may want to add a unique prefix or row number to filenames.  
