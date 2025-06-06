import numpy as np
import pandas as pd
import os

df = pd.read_csv('https://raw.githubusercontent.com/araj2/customer-database/refs/heads/master/Ecommerce%20Customers.csv')

df = df.iloc[:,3:]
df = df[df['Length of Membership']>5]

df.drop(columns=['Avg. Session Length','Time on Website'],inplace=True)

df.to_csv(os.path.join('data','customer_data.csv'), index=False)


