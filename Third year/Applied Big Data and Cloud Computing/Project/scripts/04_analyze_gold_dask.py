import os
import time
import logging
import dask.dataframe as dd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

SILVER_DIR = "./data/silver/"
GOLD_DASK_DIR = "./data/gold/revenue_trends_dask.parquet"

os.makedirs("./data/gold", exist_ok=True)

def run_dask_gold_analysis():
    start = time.time()

    logging.info("Läser Silver-lagret med Dask...")
    ddf = dd.read_parquet(SILVER_DIR)

    row_count = ddf.shape[0].compute()
    logging.info(f"Rader i Silver: {row_count}")

    # Säkerställ att event_time är datetime
    ddf["event_time"] = dd.to_datetime(ddf["event_time"], errors="coerce")

    # Ta fram datum och gruppera per dag
    daily_revenue = (
        ddf.assign(date=ddf["event_time"].dt.floor("D"))
           .groupby("date")["price"]
           .sum()
           .reset_index()
           .rename(columns={"price": "daily_revenue"})
    )

    # Sortera och beräkna 7-dagars rullande medelvärde
    # Rolling i Dask fungerar säkrast efter att vi räknat ut och gått till pandas
    daily_revenue_pd = daily_revenue.compute().sort_values("date")
    daily_revenue_pd["rolling_7d_avg"] = (
        daily_revenue_pd["daily_revenue"].rolling(7, min_periods=1).mean()
    )

    # Dask sparar som parquet
    result_ddf = dd.from_pandas(daily_revenue_pd, npartitions=1)

    logging.info(f"Skriver Dask Gold-lagret till {GOLD_DASK_DIR} ...")
    result_ddf.to_parquet(GOLD_DASK_DIR, engine="pyarrow", write_index=False, overwrite=True)

    elapsed = time.time() - start
    logging.info(f"Dask Gold-analys slutförd på {elapsed:.2f} sekunder")

    print("\n--- DASK-ANALYS ---")
    print("Första 10 raderna av trend analys:")
    print(daily_revenue_pd.head(10).to_string(index=False))
    print(f"\nExekveringstid (Dask): {elapsed:.2f} sekunder")

if __name__ == "__main__":
    run_dask_gold_analysis()