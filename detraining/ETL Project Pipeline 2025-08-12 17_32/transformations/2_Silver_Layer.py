from dlt import *
from pyspark.sql.functions import *


dlt.create_streaming_table(
  name = "customers_cdc_clean",
  expect_all_or_drop = {"no_rescued_data": "_rescued_data IS NULL","valid_id": "id IS NOT NULL","valid_operation": "operation IN ('APPEND', 'DELETE', 'UPDATE')"}
  )

@append_flow(
  target = "customers_cdc_clean",
  name = "customers_cdc_clean_flow"
)
def customers_cdc_clean_flow():
  return (
      dlt.read_stream("customers_cdc_bronze")
          .select("address", "email", "id", "firstname", "lastname", "operation", "operation_date", "_rescued_data")
  )