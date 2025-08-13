import pandas
import pandas as pd

df0 = pandas.read_csv('data/daily_sales_data_0.csv', header=None)
df1 = pandas.read_csv('data/daily_sales_data_1.csv', header=None)
df2 = pandas.read_csv('data/daily_sales_data_2.csv', header=None)

df = pd.concat([df0, df1, df2], ignore_index=True)

productName = 'pink morsel'
pink_df = df[df[0] == productName].copy()


pink_df['sales'] = pink_df[1].replace('[\$,]', '', regex=True).astype(float) * pink_df[2].astype(float)

final_df = pink_df[['sales',3,4]]
final_df.columns = ['Sales','Date','Region']
final_df.to_csv('sales_data.csv', index=False)