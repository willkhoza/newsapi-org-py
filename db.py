from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
import pandas as pd

def read_sql(sql_filename):
    """ read a query from an sql sql file into a python string object
    
    Arguments:
        sql_filename {str} -- sql file name with query
    
    Returns:
        q {str} -- a string containing the query
    """
    with open(sql_filename, 'r') as sqlfile:
        q = sqlfile.read()
    sqlfile.close()
    return q


def transfer_table(table_name, q, conn_from, conn_to, page_size = 10000, schema_to = None, mode = 'append'):
    """ transfer table from one database to another
    
    Arguments:
        table_name {str} -- the name the table should have in the destination database
        q {str} -- the string query that produces the table in the source database
        conn_from {connection object} -- the connection object that links to the source database
        conn_to {connection object} -- the connection obhect that links to the target database
    
    Keyword Arguments:
        page_size {int} -- the number of rows that should be fetched at a time from the source database (default: {10000})
        schema_to {str} -- the schema the table is should be placed in the target database (default: {None})
        mode {str} -- the action that should occur when the table is already existing in the target database 'replace'/'append'/'fail' (default: {'replace'})
    """
    for i, page in enumerate(pd.read_sql(q, con=conn_from, chunksize=page_size)):
        method = 'append'
        if i == 0:
            method = mode
        page.to_sql(table_name, con = conn_to, if_exists = method, schema = schema_to)
        print(i)


class Postgres:
    """ This class connects python to the local postgres instance"""
    
    def __init__(self):
        self.postgres_db = {
            'drivername': 'postgres',
            'username': 'postgres',
            'password': r'arlito',
            'host': 'localhost',
            'port': 5432,
            'database': 'TrendReport2'
        }
        
    def connect(self):
        engine  = create_engine(URL(**self.postgres_db))
        return engine.connect()

