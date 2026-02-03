import pandas as pd
from ingestion.fetch_stocks import fetch_and_store
from transformations.clean_data import clean
from transformations.features import add_features
from warehouse.load_warehouse import load
from ingestion.config import DATA_LAKE_RAW
from utils.logger import logger
import os

def run_pipeline():
    fetch_and_store()

    for file in os.listdir(DATA_LAKE_RAW):
        df = pd.read_parquet(f"{DATA_LAKE_RAW}/{file}")
        df = clean(df)
        df = add_features(df)
        load(df)

    logger.success("Pipeline executed successfully")
