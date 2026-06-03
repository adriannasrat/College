# Big Data Pipeline – E-commerce Analytics

This project implements a distributed data pipeline based on the Medallion Architecture (Bronze → Silver → Gold) using Dask and Apache Spark. The pipeline processes e-commerce data and generates business insights such as revenue trends over time.

---

## 1. Prepare the environment

Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate # macOS
pip install -r requirements.txt
```

---

## 2. Run the Data Pipeline (Step-by-Step)

The pipeline follows the Medallion architecture. Run the scripts in the following order:

### Ingest Bronze

Gets raw data from the Kaggle API to `data/bronze/`.

```bash
python3 scripts/01_ingest_bronze.py
```

### Process Silver

Washes the data, performs validation (e.g. null checks and filtering), and saves the result as Parquet in `data/silver/`.

```bash
python3 scripts/02_process_silver.py
```

### Analyze Gold (Spark)

Creates trend analysis using Window Functions in PySpark.

```bash
python3 scripts/03_analyze_gold_spark.py
```

### Analyze Gold (Dask)

Performs the same analysis in Dask for benchmarking and comparison.

```bash
python3 scripts/04_analyze_gold_dask.py
```

### Check Results

Compares the results between Spark and Dask to ensure data quality and consistency.

```bash
python3 scripts/99_check_results.py
```

Note: Each step builds on the results of the previous step. If a step is skipped, the next script will be missing the required input.

---

## Deployment in Kubernetes (Minikube)

The project is prepared to run in Kubernetes via Minikube, demonstrating a cloud-ready and scalable architecture.

### Prerequisites

- Docker Desktop installed and running
- Minikube installed
- Docker image built locally

```bash
docker build -t ecom-pipeline:v1 .
```

---

## Step-by-step instructions

### 1. Start the Minikube cluster

```bash
minikube start
```

### 2. Load the Docker image into Minikube

```bash
minikube image load ecom-pipeline:v1
```

### 3. Mount the data folder (important)

To allow the container to access the data from your local machine:

```bash
minikube mount "/absolute/path/to/project/data:/app/data"
```

Replace the path with your actual local path.

### 4. Start the pipeline in Kubernetes

```bash
kubectl apply -f pipeline-job.yaml
```

### 5. Monitor the execution

```bash
kubectl get pods
kubectl logs -f job/ecom-pipeline-vg
```

---

## Output

The result is saved in the Gold repository as Parquet:

- `data/gold/revenue_trends_spark.parquet/`

- `data/gold/revenue_trends_dask.parquet/`

Each dataset contains partitioned files and metadata (`_SUCCESS`).

---

## Technologies

- Python
- Dask
- Apache Spark
- Parquet
- Kubernetes (Minikube)
- Docker

### Important Python dependencies (requirements.txt)

- **kagglehub**: For programmatic downloading of raw data via the Kaggle API.
- **dask[dataframe]**: For memory-efficient washing and filtering of large datasets (Out-of-Core processing).
- **pyspark**: For advanced data analysis and distributed windowing.
- **pyarrow**: The underlying engine for reading and writing the compressed Parquet format.
- **tenacity**: For implementing fault-tolerant "retry" logic with exponential backoff when retrieving data.

---

## Purpose

- Demonstrate distributed data processing
- Compare Spark and Dask
- Implement a scalable data pipeline
- Generate insights from e-commerce data

---

## Benchmarking

The project compares:

- Execution time
- Correctness of results
- API and developer experience

---

## Project structure

```bash
project/
├── data/
│ ├── bronze/
│ ├── silver/
│ └── gold/
├── scripts/
│ ├── 01_ingest_bronze.py
│ ├── 02_process_silver.py
│ ├── 03_analyze_gold_spark.py
│ ├── 04_analyze_gold_dask.py
│ └── 99_check_results.py
├── Dockerfile
├── pipeline-job.yaml
├── requirements.txt
└── README.md
```

---

## Note

Large datasets are not included in the project. See `01_ingest_bronze.py` for the link from where the dataset is downloaded.
