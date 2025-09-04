from dlt import *
from pyspark.sql.functions import col


# Please edit the sample below

@dlt.table
def orders_bronze_file():
    path = "/Volumes/workspace/dlt/raw/"
    return (
        spark.readStream
            .format("cloudFiles")
            .option("cloudFiles.format", "csv")
            .option("cloudFiles.inferColumnTypes", "true")
            .load(path)
    )


#@dlt.table(name="orders_bronze")