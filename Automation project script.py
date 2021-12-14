# import libraries
import pandas as pd
from sqlalchemy import create_engine

db_config = {'user': 'practicum_student',         # user name
             'pwd': 's65BlTKV3faNIGhmvJVzOqhs', # password
             'host': 'rc1b-wcoijxj3yxfsf3fs.mdb.yandexcloud.net',
             'port': 6432,              # connection port
             'db': 'data-analyst-youtube-data'}          # the name of the database

connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_config['user'], 
                                                         db_config['pwd'], 
                                                         db_config['host'], 
                                                         db_config['port'], 
                                                         db_config['db'])

engine = create_engine(connection_string)

query = '''
           SELECT *
           FROM trending_by_time
        '''

trending_by_time = pd.io.sql.read_sql(query, con = engine)

trending_by_time.to_csv('trending_by_time.csv', index = False)

trending_by_time.head(5)