import pandas as pd

SPARK_PATH = "./data/gold/revenue_trends_spark.parquet"
DASK_PATH = "./data/gold/revenue_trends_dask.parquet"

print("Läser Spark-resultat...")
spark_df = pd.read_parquet(SPARK_PATH)

print("Läser Dask-resultat...")
dask_df = pd.read_parquet(DASK_PATH)

# Exakt likadana datumformat
spark_df["date"] = pd.to_datetime(spark_df["date"]).dt.strftime('%Y-%m-%d')
dask_df["date"] = pd.to_datetime(dask_df["date"]).dt.strftime('%Y-%m-%d')

# Säkerställ samma sortering
spark_df = spark_df.sort_values("date").reset_index(drop=True)
dask_df = dask_df.sort_values("date").reset_index(drop=True)

print("\n--- RESULTATJÄMFÖRELSE ---")
print(f"Rader i Spark-resultat: {len(spark_df)}")
print(f"Rader i Dask-resultat: {len(dask_df)}")

# Jämförelse av totala intäkter
spark_total = spark_df["daily_revenue"].sum()
dask_total = dask_df["daily_revenue"].sum()

print(f"\nTotala intäkter (Spark): ${spark_total:,.2f}")
print(f"Totala intäkter (Dask): ${dask_total:,.2f}")
print(f"Skillnad: ${abs(spark_total - dask_total):,.6f}")

# Dag med högsta intäkter
spark_top = spark_df.loc[spark_df["daily_revenue"].idxmax()]
dask_top = dask_df.loc[dask_df["daily_revenue"].idxmax()]

print("\nHögsta intäktsdag (Spark):")
print(spark_top.to_string())

print("\nHögsta intäktsdag (Dask):")
print(dask_top.to_string())

# Första 10 raderna
print("\nFörsta 10 raderna från Spark:")
print(spark_df.head(10).to_string(index=False))

print("\nFörsta 10 raderna från Dask:")
print(dask_df.head(10).to_string(index=False))

# Ungefärlig likhetskontroll
merged = spark_df.merge(
    dask_df,
    on="date",
    suffixes=("_spark", "_dask")
)

merged["daily_revenue_diff"] = (merged["daily_revenue_spark"] - merged["daily_revenue_dask"]).abs()
merged["rolling_diff"] = (merged["rolling_7d_avg_spark"] - merged["rolling_7d_avg_dask"]).abs()

print("\nMax skillnad i daily_revenue:", merged["daily_revenue_diff"].max())
print("Max skillnad i rolling_7d_avg:", merged["rolling_diff"].max())

if merged["daily_revenue_diff"].max() < 0.01 and merged["rolling_diff"].max() < 0.01:
    print("\nLYCKAD: Spark- och Dask-resultaten är i praktiken identiska.")
else:
    print("\nVARNING: Det finns märkbara skillnader mellan Spark och Dask resultat.")