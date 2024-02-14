import pandas as pd

df = pd.read_csv('sales.csv')

grouped_data = df.groupby('Category').agg(
    Total_Sales=('OrderID', 'count'),
    Total_Revenue=('Price', 'sum'),
    Average_Price=('Price', 'mean')
).reset_index()


print(grouped_data)
