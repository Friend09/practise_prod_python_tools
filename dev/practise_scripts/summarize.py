"""summarize.py
summarize the downloaded data and return the average from the data
"""

from fetch import download_data
from logger import logger

def summary(ticker):
    logger.warning("About to download data...")
    dataf = download_data()
    logger.warning("Dataset downloaded.")
    return dataf[ticker].mean()
