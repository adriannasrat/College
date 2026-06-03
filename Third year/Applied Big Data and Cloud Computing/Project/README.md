# Big Data Pipeline – E-commerce Analytics

Detta projekt implementerar en distribuerad datapipeline baserad på Medallion Architecture (Bronze → Silver → Gold) med hjälp av Dask och Apache Spark. Pipelinen bearbetar e-handelsdata och genererar affärsinsikter såsom intäktstrender över tid.

---

## 1. Förbered miljön

Skapa en virtuell miljö och installera beroenden:

```bash
python3 -m venv venv
source venv/bin/activate  # macOS
pip install -r requirements.txt
```

---

## 2. Kör Data-pipelinen (Steg-för-steg)

Pipelinen följer Medallion-arkitekturen. Kör skripten i följande ordning:

### Ingest Bronze

Hämtar rådata från Kaggle API till `data/bronze/`.

```bash
python3 scripts/01_ingest_bronze.py
```

### Process Silver

Tvättar datan, utför validering (t.ex. null-checks och filtrering), och sparar resultatet som Parquet i `data/silver/`.

```bash
python3 scripts/02_process_silver.py
```

### Analyze Gold (Spark)

Skapar trendanalys med hjälp av Window Functions i PySpark.

```bash
python3 scripts/03_analyze_gold_spark.py
```

### Analyze Gold (Dask)

Utför samma analys i Dask för benchmarking och jämförelse.

```bash
python3 scripts/04_analyze_gold_dask.py
```

### Check Results

Jämför resultaten mellan Spark och Dask för att säkerställa datakvalitet och konsistens.

```bash
python3 scripts/99_check_results.py
```

Notera: Varje steg bygger på resultatet från föregående steg. Om ett steg hoppas över kommer nästa skript att sakna nödvändig indata.

---

## Deployment i Kubernetes (Minikube)

Projektet är förberett för körning i Kubernetes via Minikube, vilket demonstrerar en cloud-ready och skalbar arkitektur.

### Förutsättningar

- Docker Desktop installerat och igång
- Minikube installerat
- Docker-image byggd lokalt

```bash
docker build -t ecom-pipeline:v1 .
```

---

## Steg-för-steg instruktioner

### 1. Starta Minikube-klustret

```bash
minikube start
```

### 2. Ladda in Docker-imagen i Minikube

```bash
minikube image load ecom-pipeline:v1
```

### 3. Montera datamappen (viktigt)

För att containern ska få tillgång till datan från din lokala maskin:

```bash
minikube mount "/absolut/sökväg/till/project/data:/app/data"
```

Ersätt sökvägen med din faktiska lokala path.

### 4. Starta pipelinen i Kubernetes

```bash
kubectl apply -f pipeline-job.yaml
```

### 5. Övervaka körningen

```bash
kubectl get pods
kubectl logs -f job/ecom-pipeline-vg
```

---

## Output

Resultatet sparas i Gold-lagret som Parquet:

- `data/gold/revenue_trends_spark.parquet/`
- `data/gold/revenue_trends_dask.parquet/`

Varje dataset innehåller partitionerade filer samt metadata (`_SUCCESS`).

---

## Teknologier

- Python
- Dask
- Apache Spark
- Parquet
- Kubernetes (Minikube)
- Docker

### Viktiga Python-beroenden (requirements.txt)

- **kagglehub**: För programmatisk nedladdning av rådata via Kaggle API.
- **dask[dataframe]**: För minneseffektiv tvätt och filtrering av stora dataset (Out-of-Core processing).
- **pyspark**: För avancerad dataanalys och distribuerade fönsterfunktioner.
- **pyarrow**: Den underliggande motorn för att läsa och skriva det komprimerade formatet Parquet.
- **tenacity**: För att implementera feltolerant "retry"-logik med exponential backoff vid datahämtning.

---

## Syfte

- Demonstrera distribuerad databehandling
- Jämföra Spark och Dask
- Implementera en skalbar datapipeline
- Generera insikter från e-handelsdata

---

## Benchmarking

Projektet jämför:

- Execution time
- Resultatens korrekthet
- API och utvecklarupplevelse

---

## Projektstruktur

```bash
project/
├── data/
│   ├── bronze/
│   ├── silver/
│   └── gold/
├── scripts/
│   ├── 01_ingest_bronze.py
│   ├── 02_process_silver.py
│   ├── 03_analyze_gold_spark.py
│   ├── 04_analyze_gold_dask.py
│   └── 99_check_results.py
├── Dockerfile
├── pipeline-job.yaml
├── requirements.txt
└── README.md
```

---

## Notering

Stora datamängder inkluderas inte i projektet. Se `01_ingest_bronze.py` för länken från var datasetet laddas ner.
