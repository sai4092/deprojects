from dlt import *
from pyspark.sql.functions import *


dlt.create_streaming_table(
  name = "customers_silver",
  expect_all_or_drop = {
    "no_rescued_data": "_rescued_data IS NULL",
    "valid_id": "id IS NOT NULL",
    "valid_operation": "operation IN ('APPEND', 'DELETE', 'UPDATE')"
    }
  )

@append_flow(
  target = "customers_silver",
  name = "customers_silver_flow"
)
def customers_silver_flow():
  return (
      dlt.read_stream("customers_bronze")
          .select("*")
  )