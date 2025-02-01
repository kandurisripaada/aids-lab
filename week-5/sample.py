import pandas as pd
from sqlalchemy import create_engine

username = 'root'  # Your MySQL username
password = '1234'  # Your MySQL password
host = 'localhost'  # Your MySQL host, e.g., 'localhost' or an IP address
database = 'sripaada'  # Your MySQL database name

connection_string = f'mysql+mysqlconnector://{username}:{password}@{host}/{database}'

engine = create_engine(connection_string)

df1 = pd.read_sql('SELECT * FROM transactions', engine)

print(df1)
print("\n\n")

df2=pd.read_csv('C:/Users/CVR/Downloads/customers.csv')
print(df2)
print("\n\n")

merge=pd.merge(df1,df2,on='Cust_id',how='outer')
print(merge)
print("\n\n")

# print(merge['Amount'].dtype)
print(f"memory usage: {df1.memory_usage(deep=True)}")

