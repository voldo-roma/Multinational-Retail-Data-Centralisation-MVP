#%% 
import psycopg2
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy import inspect

DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
HOST = 'localhost'
USER = 'postgres'
PASSWORD = 'Jenkins09'
DATABASE = 'Pagila'
PORT = 5436
engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

#method 1 
with psycopg2.connect(host='localhost', user='postgres', password='Jenkins09', dbname='Pagila', port=5436) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM actor")
        for table in cur.fetchall():
            print(table)
#method 2 
engine.connect()
inspector = inspect(engine)
inspector.get_table_names()
#find workaround later. Bye 14:38 27/01/2024
# with engine.connect() as connection:
#    result = connection.execute("SELECT * FROM actor")
#    for row in result:
#       print(row) 
