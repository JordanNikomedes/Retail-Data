ALTER TABLE dim_products
	ADD weight_class VARCHAR(30);
UPDATE dim_products
	SET weight_class = 
		CASE 
			when weight/1000 < 2 then 'Light'
			when weight/1000 between 2 and 40 then 'Mid_Sized'
			when weight/1000 between 41 and 140 then 'Heavy'
			when weight/1000 > 140 then 'Truck_Required'  
		else 'Invalid' 
		END;

UPDATE dim_products 
SET product_price = REPLACE(product_price, '£', '')::NUMERIC;

ALTER TABLE dim_products
	RENAME COLUMN removed TO still_available;
  
UPDATE dim_products
	SET still_available = 
		CASE 
			when still_available = 'Still_available' then True
			when still_available = 'Removed' then False
		END;

ALTER TABLE dim_products
	ALTER COLUMN product_price SET DATA TYPE NUMERIC USING product_price::NUMERIC,
	ALTER COLUMN weight SET DATA TYPE NUMERIC USING weight::NUMERIC,
	ALTER COLUMN product_code SET DATA TYPE VARCHAR(255) USING product_code::VARCHAR,
	ALTER COLUMN "EAN" SET DATA TYPE VARCHAR(255) USING "EAN"::VARCHAR,
	ALTER COLUMN date_added SET DATA TYPE DATE USING date_added::DATE,
	ALTER COLUMN "uuid" SET DATA TYPE UUID USING "uuid"::UUID,
	ALTER COLUMN still_available SET DATA TYPE BOOLEAN USING still_available::BOOLEAN,
	ALTER COLUMN weight_class SET DATA TYPE VARCHAR(255) USING weight_class::VARCHAR;

