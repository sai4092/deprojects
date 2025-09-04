--https://docs.databricks.com/aws/en/dlt/sql-dev

--CREATE OR REFRESH MATERIALIZED VIEW basic_mv_SQL
--AS SELECT * FROM samples.nyctaxi.trips;

--CREATE OR REFRESH STREAMING TABLE basic_st_SQL
--AS SELECT * FROM STREAM samples.nyctaxi.trips;


CREATE OR REFRESH STREAMING TABLE ingestion_st
AS SELECT *
FROM STREAM read_files(
  "/databricks-datasets/retail-org/sales_orders",
  format => "json");

CREATE OR REFRESH MATERIALIZED VIEW batch_mv
AS SELECT *
FROM read_files(
  "/databricks-datasets/retail-org/sales_orders",
  format => "json");