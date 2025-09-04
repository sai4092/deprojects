from dlt import *
from pyspark.sql.functions import *


dlt.create_streaming_table(name="customers_gold", comment="Clean, materialized customers")

dlt.create_auto_cdc_flow(
  target="customers_gold",  # The customer table being materialized
  source="customers_silver",  # the incoming CDC
  keys=["id"],  # what we'll be using to match the rows to upsert
  sequence_by=col("operation_date"),  # de-duplicate by operation date, getting the most recent value
  ignore_null_updates=False,
  apply_as_deletes=expr("operation = 'DELETE'"),  # DELETE condition
  except_column_list=["operation", "operation_date", "_rescued_data"],
)


# create the table
dlt.create_streaming_table(
    name="customers_history", comment="Slowly Changing Dimension Type 2 for customers"
)

# store all changes as SCD2
dlt.create_auto_cdc_flow(
    target="customers_history",
    source="customers_silver",
    keys=["id"],
    sequence_by=col("operation_date"),
    ignore_null_updates=False,
    apply_as_deletes=expr("operation = 'DELETE'"),
    except_column_list=["operation", "operation_date", "_rescued_data"],
    stored_as_scd_type="2",
)  
