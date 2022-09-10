import pandas as pd
from sqlalchemy import create_engine
import openpyxl
conn="mysql+pymysql://{user}:{pw}@{host}/{db}?charset=utf8mb4".format(user='root',pw='madhuri',host='localhost',db='my_db')
engine=create_engine(conn,echo=False)
print(engine)

sql_query='Select * from employee'
df=pd.read_sql(sql_query,con=engine)   ### open in table format
#df.to_excel("C:\\Users\\Admin\\Desktop\\Employee_table.xlsx")  ## open file in excel sheet.
print(df)


import sqlalchemy
from sqlalchemy import exc
import configparser
import os
import logging
#logging.basicConfig(filename='log10.log',format='%(levelname)s:%(asctime)s:%(message)s%(lineno)s',datefmt='%d-%m-%y %H:%M:%S %p',level=logging.DEBUG)
#logger=logging.getLogger(__name__)
path='/'.join((os.path.abspath(__file__).replace('\\','//')).split('/')[:-1])
print(path)
conn=os.path.join(path,'madhuri.ini')
print(conn)


obj=configparser.ConfigParser()
obj.read(conn)

user=obj.get('detail','user')
pw=obj.get('detail','pw')
host=obj.get('detail','host')
port=obj.get('detail','port')
db=obj.get('detail','db')

# def main():
#     logger.info("Process is running")
#     logger.info("Started script")
#     try:

engine=sqlalchemy.create_engine(f'mysql+pymysql://{user}:{pw}@{host}:{port}/{db}',echo=False)
res=engine.execute('show tables')
print(res.fetchall())
#         conn="mysql+pymysql://{user}:{pw}@{host}/{db}?charset=utf8mb4".format(user='root',pw='madhuri',host='localhost',db='my_db')
#         engine=create_engine(conn,echo=False)
#         print(engine)
#     except exc.SQLAlchemyError as e:
#         logger.error("Not connect,Somthing went wrong")
    
#     try:
#         sql_query="select * employee"
#         df=pd.read_sql(sql_query,con=engine)   ### open in table format
#         print(df)
#         # df.to_excel("C:\\Users\\Admin\\Desktop\\Employee_table.xlsx")  ## open file in excel sheet.
       
#     except Exception as e:
#         logger.info(e,exc_info=True)
# if __name__==' __main__' :
#     main()