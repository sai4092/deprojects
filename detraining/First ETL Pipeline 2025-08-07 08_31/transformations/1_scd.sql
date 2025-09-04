-- Create and populate the target table.

CREATE OR REFRESH STREAMING TABLE users_bronze_scd_1;

CREATE FLOW bronze_scd1_flow
AS AUTO CDC INTO
  users_bronze_scd_1
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
  SCD TYPE 1;