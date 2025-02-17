ALTER TABLE dim_card_details
	ALTER COLUMN card_number SET DATA TYPE VARCHAR(50) USING card_number::VARCHAR,
	ALTER COLUMN expiry_date SET DATA TYPE VARCHAR(50) USING expiry_date::VARCHAR,
	ALTER COLUMN date_payment_confirmed SET DATA TYPE DATE USING date_payment_confirmed::DATE;