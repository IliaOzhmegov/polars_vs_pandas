-- Create Table
CREATE TABLE transactions (
    transaction_id          UUID,
    date                    DATE,
    user_id                 UUID,
    is_blocked              BOOL,
    transaction_amount      REAL, -- it used to be INTEGER, but python script generate value of float type
    transaction_category_id INTEGER
    
);

CREATE TABLE users (
    user_id   UUID,
    is_active BOOLEAN
);

-- Upload Genereated Data
COPY users        FROM '/csv/data/users.csv'        DELIMITER ',' CSV HEADER;
COPY transactions FROM '/csv/data/transactions.csv' DELIMITER ',' CSV HEADER;




