from main import backTest
import logging
import backtrader as bt
import pathlib
import os

logging.basicConfig(filename=None, filemode='a', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(level=logging.INFO)

backTest(
            Russell3000=os.path.join(os.getcwd(), 'raw data/backtesting_data.csv'),
            start_date=bt.datetime.datetime(2018, 1, 31),
            end_date=bt.datetime.datetime(2021, 12, 2),
            logger=logger)