import dlt
from pyspark.sql.functions import *

#https://docs.databricks.com/aws/en/dlt/python-dev
# CREATE A METERIALIZE VIEW
@dlt.table()
def basic_mv():
  return spark.read.table("samples.nyctaxi.trips")

@dlt.table()
def basic_st():
  return spark.readStream.table("samples.nyctaxi.trips")


@dlt.table(name = "trips_mv")
def basic_mv():
  return spark.read.table("samples.nyctaxi.trips")

@dlt.table(name = "trips_st")
def basic_st():
  return spark.readStream.table("samples.nyctaxi.trips")








