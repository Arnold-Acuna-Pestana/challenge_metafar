import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

pg_conn = psycopg2.connect(
            user=os.getenv("USER_POSTGRES"),
            password=os.getenv("PASS_POSTGRES"),
            host=os.getenv("HOST"),
            port=os.getenv("PORT"),
            database=os.getenv("DB")
        )
        
pg_conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) 
pgcursor = pg_conn.cursor()


pgcursor.execute('DROP TABLE IF EXISTS crypto_table')

# Crea tabla schema en postgresql
pgcursor.execute("""

CREATE TABLE IF NOT EXISTS crypto_table
(   
    name VARCHAR(50) NOT NULL, 
    symbol VARCHAR(20) NOT NULL , 
    cmc_rank INT, 
    usd_price FLOAT, 
    usd_volume_24h FLOAT, 
    perc_change_1h FLOAT, 
    perc_change_24h FLOAT, 
    perc_change_7d FLOAT, 
    perc_change_30d FLOAT, 
    perc_change_60d FLOAT, 
    perc_change_90d FLOAT, 
    circulating_supply FLOAT, 
    max_supply FLOAT, 
    market_cap FLOAT, 
    market_cap_dominance FLOAT, 
    feauture_1 VARCHAR(50), 
    feauture_2 VARCHAR(50), 
    date_added VARCHAR(30) NOT NULL, 
    last_updated VARCHAR(30) NOT NULL, 
    timestamp VARCHAR(30) NOT NULL,
    process_dt timestamp NOT NULL DEFAULT now(),
    PRIMARY KEY(symbol, process_dt)
);
""")

pg_conn.commit()
pgcursor.close()
pg_conn.close()