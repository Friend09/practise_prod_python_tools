from fetch import download_data
from logger import logger

def summary(ticker):
    logger.info(f"About to download data.")
    dataf = download_data()
    logger.debug(f"Dataset downloaded. shape={dataf.shape}")
    logger.debug(f"Dataset downloaded. columns={dataf.columns}")
    return dataf[ticker].mean()
