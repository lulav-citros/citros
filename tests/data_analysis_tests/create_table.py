'''
Download table test_table.csv and push it to postgres database
'''

import ast
import pandas as pd
import json
import psycopg2.extras
import psycopg2.extensions
from decouple import config

psycopg2.extensions.register_adapter(dict, psycopg2.extras.Json)



table_name = "test_table"

if config('TEST_ENV') == 'local':
    from citros.database import CitrosDB as CitrosDB_base
    citros_base = CitrosDB_base()
    connection = psycopg2.connect(host=citros_base.db_host,
                            user=citros_base.db_user,
                            password=citros_base.db_password,
                            database=citros_base.db_name,
                            options="-c search_path=" +'public', 
                            port = citros_base.db_port)

elif config('TEST_ENV') == 'github':
    connection = psycopg2.connect(host=config('POSTGRES_HOST'),
                              user=config('POSTGRES_USER'),
                              password=config('POSTGRES_PASSWORD'),
                              database=config('POSTGRES_DB'),
                              options="-c search_path=" +'public', 
                              port = config('POSTGRES_PORT'))
    

cursor = connection.cursor()

path = r'test_table.csv'
F = pd.read_csv(path, converters = {'data': ast.literal_eval})

query_create = "CREATE TABLE " + table_name + " (sid bigint, time bigint, topic varchar, type varchar, rid bigint, data jsonb)"
cursor.execute(query_create)
connection.commit()

for i in range(len(F)):
    sid = int(F.iloc[i]['sid'])
    time = int(F.iloc[i]['time'])
    topic = F.iloc[i]['topic']
    type_val =F.iloc[i]['type']
    rid = int(F.iloc[i]['rid'])
    json_data =  json.dumps(F.iloc[i]['data'])
    query = "INSERT INTO " + table_name + "(sid, time, topic, type, rid, data) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query,(sid, time, topic, type_val, rid, json_data))
    connection.commit()

res = cursor.execute("SELECT rid from "+ table_name + " where rid = 1 limit 1")
print("success")