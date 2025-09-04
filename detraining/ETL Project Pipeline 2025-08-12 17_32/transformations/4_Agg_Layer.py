from dlt import *
from pyspark.sql.functions import *


@dlt.table(
  name = "customers_history_agg",
  comment = "Aggregated customer history"
)
def customers_history_agg():
  return (
    dlt.read("customers_history")
      .groupBy("id")
      .agg(
          count("address").alias("address_count"),
          count("email").alias("email_count"),
          count("firstname").alias("firstname_count"),
          count("lastname").alias("lastname_count")
      )
  )
