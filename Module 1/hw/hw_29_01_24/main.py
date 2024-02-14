import pandas as pd

sales_2021 = pd.read_csv('sales_2021.csv')
sales_2022 = pd.read_csv('sales_2022.csv')

concat_sales = pd.concat([sales_2021, sales_2022])

result_df = concat_sales.groupby('product_id').agg(
    Total_Revenue=('revenue', 'sum')
).reset_index()

result_df.to_csv('result.csv', index=False)
