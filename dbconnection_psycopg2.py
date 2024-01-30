#%% 
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import text
DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
HOST = 'localhost'
USER = 'postgres'
PASSWORD = 'Jenkins09'
DATABASE = 'Pagila'
PORT = 5436
engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
with engine.execution_options(isolation_level='AUTOCOMMIT').connect() as conn:
    conn.execute("SELECT * FROM actor")
#inspector object is a wrapper around the database, it allows us to retrieve info about the tables and columns inside the database
inspector = inspect(engine)
inspector.get_table_names()
#'ORM in SQLAlchemy: create a table in database and insert data: use pandas. Read tables using pandas and the engine'
actors = pd.read_sql_table('actor', engine)
actors.head(10)

#%%
with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM actor"))
    for row in result:
        print(row)
with engine.execution_options(isolation_level='AUTOCOMMIT').connect() as conn:
    