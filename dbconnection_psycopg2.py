#%% 
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import text
from sklearn.datasets import load_iris
DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
HOST = 'localhost'
USER = 'postgres'
PASSWORD = 'Jenkins09'
DATABASE = 'Pagila'
PORT = 5436
engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM actor"))
    for row in result:
        print(row)
#%% 
#You can also use pandas to create tables in your database using the `to_sql` method
data = load_iris()
iris = pd.DataFrame(data['data'], columns=data['feature_names'])
iris.head()
iris.to_sql('iris_dataset', engine, if_exists='replace')
#%%
actors = pd.read_sql_table('actor', engine)
actors.head(10)
print(actors.head(25))
#
#    conn.execute("SELECT * FROM actor")
#inspector object is a wrapper around the database, it allows us to retrieve info about the tables and columns inside the database
#inspector = inspect(engine)
#inspector.get_table_names()
#%%
