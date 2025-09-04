import dlt
from pyspark.sql.functions import *

customer_path = spark.conf.get("customer_path")
orders_path = spark.conf.get("orders_path")

@dlt.table(
  comment="New customer data incrementally ingested from cloud object storage landing zone"
)
def customers_bronze():
  return (
    spark.readStream
      .format("cloudFiles")
      .option("cloudFiles.format", "json")
      .option("cloudFiles.inferColumnTypes", "true")
      .load(customer_path)
  )

@dlt.table(
  comment="New orders data incrementally ingested from cloud object storage landing zone"
)
def orders_bronze():
  return (
    spark.readStream
      .format("cloudFiles")
      .option("cloudFiles.format", "csv")
      .option("header", "true")
      .option("cloudFiles.inferColumnTypes", "true")
      .load(orders_path)
  )