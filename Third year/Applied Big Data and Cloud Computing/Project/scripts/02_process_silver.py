import dask.dataframe as dd
import os
from tenacity import retry, stop_after_attempt, wait_exponential 

# Sökvägar
BRONZE_DIR = "./data/bronze/"
SILVER_DIR = "./data/silver/"
os.makedirs(SILVER_DIR, exist_ok=True)

# Error handling med retry logic för transienta fel 
@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=4, max=60))
def load_data_with_retry(path):
    """Försöker läsa in data och gör om vid misslyckande"""
    print(f"Försöker läsa data från {path}...")
    return dd.read_csv(os.path.join(path, "*.csv"))

def process_pipeline():
    try:
        # 1. Ingestion med Retry
        ddf = load_data_with_retry(BRONZE_DIR)

        # 2. Data Validation
        # Null-kontroll
        null_counts = ddf[['event_type', 'price']].isnull().sum().compute()
        print("Data Kvalitet - Null Analys:\n", null_counts)
        
        # range assertions (priset måste vara positivt)
        # Vi filtrerar bort ogiltiga rader för att säkra datakvaliteten i Silver
        ddf_cleaned = ddf[(ddf['event_type'] == 'purchase') & (ddf['price'] > 0)]

        # 3. Spara som Parquet 
        # Vi använder 'overwrite' för att göra steget idempotent 
        ddf_cleaned.to_parquet(SILVER_DIR, engine="pyarrow", overwrite=True)
        print(f"SUCCESS: Silver-lager sparat i {SILVER_DIR}")

    except Exception as e:
        print(f"PERMANENT FAILURE: Pipelinen stannade på grund av: {e}")

if __name__ == "__main__":
    process_pipeline()