"""fetch.py
Fetch the data for the given ticker
"""

import pandas as pd

from logger import logger

def download_data():
    url = 'https://calmcode.io/static/data/stocks.csv'
    logger.debug(f"Fetching from {url}.")
    df = pd.read_csv(url)
    logger.info(f"File downloaded from {url}.")
    return df

download_data()
