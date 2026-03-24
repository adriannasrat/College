import time
import logging
from pyspark.sql import SparkSession, Window
from pyspark.sql import functions as F

# Strukturerad loggning konfigurerad
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

def run_spark_analysis():
    start_time = time.time()
    logging.info("Startar Spark Gold-analys...")

    spark = SparkSession.builder \
        .appName("Ecom_Gold_Spark") \
        .config("spark.executor.memory", "4g") \
        .getOrCreate()

    logging.info("Läser Silver-lagret (Parquet)...")
    df_silver = spark.read.parquet("./data/silver/")

    # 1. Daglig intäkt
    daily_revenue_df = df_silver.withColumn("date", F.to_date("event_time")) \
        .groupBy("date") \
        .agg(F.sum("price").alias("daily_revenue"))

    # 2. Window Function: 7-dagars rullande medelvärde
    window_spec = Window.orderBy("date").rowsBetween(-6, 0)
    gold_analysis = daily_revenue_df.withColumn(
        "rolling_7d_avg", 
        F.avg("daily_revenue").over(window_spec)
    ).orderBy("date")

    logging.info("Skriver Spark Gold-lager...")
    gold_analysis.write.mode("overwrite").parquet("./data/gold/revenue_trends_spark.parquet")

    elapsed = time.time() - start_time
    logging.info(f"Spark Gold-analys klar på {elapsed:.2f} sekunder")
    
    print(f"\nExekveringstid (Spark): {elapsed:.2f} sekunder")
    gold_analysis.show(10)

if __name__ == "__main__":
    run_spark_analysis()