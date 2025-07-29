import pandas as pd 
import numpy as np 
import sys 
from pathlib import Path 
sys.path.append(str(Path(__file__).resolve().parent.parent))
from utils.config import logger , RAW_DATA_DIR
import requests 

logger.info(f"Successfully initiated the logger file")



def fetch_Data_from_source(month:int, year: int) ->Path: 
    url = f"https://s3.amazonaws.com/tripdata/{year}{month:02d}-citibike-tripdata.zip"
    

    fetch = requests.get(url)

    if fetch.status_code == 200: 
        logger.info(f"Successfuly fetched the data! {url}")
        data = RAW_DATA_DIR/ f"citibike_{year}_{month:02d}.parquet"
        with open(data, "wb") as f:
            for chunk in fetch.iter_content(chunk_size=1024 * 1024):
                f.write(chunk)
        return data 

    else: 
        logger.error(f"Cannot download data , please check the url {url} once")


    