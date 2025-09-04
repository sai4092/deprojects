from dlt import *
from pyspark.sql.functions import *

# Create the target bronze table
dlt.create_streaming_table("customers_cdc_bronze", comment="New customer data incrementally ingested from cloud object storage landing zone")

# Create an Append Flow to ingest the raw data into the bronze table
@append_flow(
  target = "customers_cdc_bronze",
  name = "customers_bronze_ingest_flow"
)
def customers_bronze_ingest_flow():
  return (
      spark.readStream
          .format("cloudFiles")
          .option("cloudFiles.format", "json")
          .option("cloudFiles.inferColumnTypes", "true")
          .load("/Volumes/workspace/customers/raw_data/customers/")
  )