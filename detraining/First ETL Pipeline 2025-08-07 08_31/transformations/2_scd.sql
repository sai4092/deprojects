-- Create and populate the target table.

CREATE OR REFRESH STREAMING TABLE users_bronze_scd_2;

CREATE FLOW bronze_scd2_flow
AS AUTO CDC INTO
  users_bronze_scd_2
FROM
  stream(cdc_data.users)
KEYS
  (userId)
APPLY AS DELETE WHEN operation = "DELETE"
SEQUENCE BY
  sequenceNum
COLUMNS * EXCEPT
  (operation, sequenceNum)
STORED AS
  SCD TYPE 2;
  --/Volumes/workspace/dlt/raw/orders_batch1.csv