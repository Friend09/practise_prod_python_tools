import sys

from logger import logger
from summarize import summary

if __name__ == "__main__":
    ticker = sys.argv[1]
    logger.warning(f"Will find summary for {ticker}")
    print(f"The average stock price is {summary(ticker)}")
