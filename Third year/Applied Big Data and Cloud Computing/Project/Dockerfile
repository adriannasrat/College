# Använder en officiell Python-image som bas
FROM python:3.10-slim

# Installera Java, det krävs för Spark
RUN apt-get update && apt-get install -y default-jre && apt-get clean

WORKDIR /app

# Installera beroenden
RUN pip install dask[complete] pandas pyarrow kagglehub tenacity pyspark

# Kopiera skripten
COPY scripts/ /app/scripts/

# Skapa mappstruktur för volymmontering
RUN mkdir -p /app/data/bronze /app/data/silver /app/data/gold

CMD ["python", "scripts/02_process_silver.py"]