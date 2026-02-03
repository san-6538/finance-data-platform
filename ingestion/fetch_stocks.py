import yfinance as yf
import pandas as pd
from ingestion.config import STOCKS, START_DATE, DATA_LAKE_RAW
from utils.logger import logger
import os

def fetch_and_store():
    os.makedirs(DATA_LAKE_RAW, exist_ok=True)

    for ticker in STOCKS:
        logger.info(f"Fetching data for {ticker}")
        df = yf.download(ticker, start=START_DATE, progress=False)

        # Flatten MultiIndex columns if present
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        df.reset_index(inplace=True)
        df["ticker"] = ticker

        path = f"{DATA_LAKE_RAW}/{ticker}.parquet"
        df.to_parquet(path, index=False)

        logger.success(f"Stored raw data → {path}")
