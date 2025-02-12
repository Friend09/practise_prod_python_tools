"""fetch.py
Fetch the data for the given ticker
"""

import pandas as pd
from logger import logger

def download_data():
    url = 'https://calmcode.io/static/data/stocks.csv'
    logger.warning(f"Fetching from {url}")
    return pd.read_csv(url)
