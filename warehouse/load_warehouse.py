import duckdb
import pandas as pd
from utils.logger import logger

DB_PATH = "data_lake/analytics/warehouse.duckdb"

def load(df: pd.DataFrame):
    logger.info("Loading data into warehouse")

    con = duckdb.connect(DB_PATH)
    con.execute(open("warehouse/schema.sql").read())
    con.register("df", df)

    con.execute("""
        INSERT INTO stock_analytics
        SELECT Date, ticker, Close, returns, ma_20, ma_50, volatility FROM df
    """)

    con.close()
    logger.success("Warehouse load complete")
