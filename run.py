import glob
import pandas as pd
import os
import configparser

from pgdb import PGDatabase

dirname = os.path.dirname(__file__)

config = configparser.ConfigParser()
config.read(os.path.join(dirname, 'config.ini'))
SALES_PATH = config['Files']['SALES_PATH']
DATABASE_CREDS = config['Database']

sales_df = pd.DataFrame()
files = glob.glob(SALES_PATH)
if files:
    frames = []
    for file_path in files:
        temp_df = pd.read_csv(file_path)
        frames.append(temp_df)
        #os.remove(file_path)
    sales_df = pd.concat(frames, ignore_index=True)

        
database = PGDatabase(
    host=DATABASE_CREDS['HOST'],
    database=DATABASE_CREDS['DATABASE'],
    user=DATABASE_CREDS['USER'],
    password=DATABASE_CREDS['PASSWORD']
)

for i, row in sales_df.iterrows():
    query = f"insert into sales values ('{row['dt']}', '{row['shop_num']}','{row['cash_num']}','{row['doc_id']}','{row['item']}','{row['category']}',{row['amount']}, {row['price']}, {row['discount']})"
    database.post(query)
