import kagglehub
import shutil
import os

# Bronze-mapp definierad
BRONZE_DIR = "./data/bronze/"
os.makedirs(BRONZE_DIR, exist_ok=True)

# Laddar ner datasetet
print("Laddar ner data från Kaggle...")
download_path = kagglehub.dataset_download("mkechinov/ecommerce-behavior-data-from-multi-category-store")

# Flytta filerna från cache till projektmapp
files = os.listdir(download_path)
for f in files:
    source = os.path.join(download_path, f)
    destination = os.path.join(BRONZE_DIR, f)
    if not os.path.exists(destination):
        print(f"Flyttar {f} till {BRONZE_DIR}")
        shutil.move(source, destination)

# Kontrollerar storleken
total_size = sum(os.path.getsize(os.path.join(BRONZE_DIR, f)) for f in os.listdir(BRONZE_DIR)) / (1024**3)
print(f"Total storlek i Bronze: {total_size:.2f} GB")