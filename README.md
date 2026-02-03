# Financial Market Data Engineering Platform

## Overview
End-to-end data engineering system for ingesting, processing, and analyzing stock market time-series data.

## Architecture
- Ingestion: Yahoo Finance API
- Data Lake: Raw → Processed → Analytics (Parquet)
- Transformation: Feature engineering pipelines
- Warehouse: DuckDB (Analytics-ready SQL tables)
- Orchestration: Modular pipeline runner (Airflow-style)

## Execution
```bash
pip install -r requirements.txt
python main.py
```

## 📊 Data & Output

The pipeline generates data in `data_lake/`:

1.  **Raw Data**: `data_lake/raw/stocks/*.parquet` (Original downloads from Yahoo Finance)
2.  **Warehourse**: `data_lake/analytics/warehouse.duckdb`
    *   This is a **DuckDB** database file, not a text/parquet file.
    *   **To View**: Use [DBeaver](https://dbeaver.io/) or the python script below.

### Inspecting the Warehouse
Run this snippet to check the data:
```python
import duckdb
con = duckdb.connect("data_lake/analytics/warehouse.duckdb")
con.sql("SELECT * FROM stock_analytics LIMIT 10").show()
```

## Production Notes

* Airflow can orchestrate pipeline execution
* S3/GCS can replace local data lake
* PostgreSQL/Snowflake can replace DuckDB
