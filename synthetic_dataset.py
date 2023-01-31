from random import randint 
from faker import Faker
import pandas as pd 
 
fake = Faker()
 
def input_data(x):
   
    # pandas dataframe
    data = pd.DataFrame()
    for i in range(0, x):
        data.loc[i,'id']= randint(1, 100)
        data.loc[i,'name']= fake.name()
        data.loc[i,'address']= fake.address()
        data.loc[i,'latitude']= str(fake.latitude())
        data.loc[i,'longitude']= str(fake.longitude())
    return data
   

d = input_data(10)
print(d)