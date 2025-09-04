-- EXAMPLE 1:
-- Create a streaming table, and add two flows that append data to it:
CREATE OR REFRESH STREAMING TABLE simple_multi_flow_users;

-- first flow into target_table:
CREATE FLOW users_scd1_flow AS
INSERT INTO simple_multi_flow_users BY NAME
SELECT * FROM stream(workspace.dlt.users_bronze_scd_1);

-- second flow into target_table:
CREATE FLOW users_scd2_flow AS
INSERT INTO ONCE simple_multi_flow_users BY NAME
SELECT userId, name, city FROM workspace.dlt.users_bronze_scd_2;

