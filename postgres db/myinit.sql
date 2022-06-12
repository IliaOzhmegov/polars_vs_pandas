-- Create Table
CREATE TABLE transactions (
    transaction_id          UUID,
    date                    DATE,
    transaction_amount      REAL,
    transaction_category_id INTEGER,
    is_blocked              BOOL,
    user_id                 UUID 
    
);

CREATE TABLE users (
    user_id    UUID,
    is_blocked BOOLEAN
);

-- Upload Genereated Data
COPY users        FROM '/csv/data/users.csv'        DELIMITER ',' CSV HEADER;
COPY transactions FROM '/csv/data/transactions.csv' DELIMITER ',' CSV HEADER;




