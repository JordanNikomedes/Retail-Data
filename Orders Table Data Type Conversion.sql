CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

ALTER TABLE orders_table
	ALTER COLUMN date_uuid SET DATA TYPE UUID USING date_uuid::UUID,
	ALTER COLUMN user_uuid SET DATA TYPE UUID USING user_uuid::UUID,
	ALTER COLUMN card_number SET DATA TYPE VARCHAR(50) USING card_number::VARCHAR,
	ALTER COLUMN store_code SET DATA TYPE VARCHAR(255) USING store_code::VARCHAR,
	ALTER COLUMN product_code SET DATA TYPE VARCHAR(255) USING product_code::VARCHAR,
	ALTER COLUMN product_quantity SET DATA TYPE SMALLINT USING product_quantity::SMALLINT;
