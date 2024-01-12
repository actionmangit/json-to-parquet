import pyarrow
import pyarrow.parquet as pq
import pandas as pd
import json


def lambda_handler():
    print("testsssssssssssss")

    df = spark.read.json()
    df.to_parquet('myfile.parquet')


lambda_handler()
