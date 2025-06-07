# This code generates a connection to google colab and runs a SQL query on the BigQuery dataset `thelook_ecommerce`.
from google.colab import auth
auth.authenticate_user()
!pip install --upgrade pandas-gbq


# use pandas data frame to put query result in a data frame
import pandas as pd
query= """
with
revenue_per_monthcategory as(
  SELECT sum(oi.sale_price) as total_price,
  EXTRACT(MONTH FROM oi.created_at) AS month,p.category, sum(o.num_of_item) as total_item_sold
  FROM `bigquery-public-data.thelook_ecommerce.order_items` as oi
  JOIN `bigquery-public-data.thelook_ecommerce.products` as p
  ON oi.product_id = p.id
  JOIN `bigquery-public-data.thelook_ecommerce.orders` as o
  ON oi.order_id = o.order_id
  WHERE oi.status LIKE '%Shipped%' or  oi.status LIKE '%Complete%'
  Group by  month, p.category
  ORDER by month ASC

),
cost_per_monthcategry as(
  SELECT sum(cost) as total_cost, p.category, EXTRACT(MONTH FROM oi.created_at) AS MONTH
  FROM `bigquery-public-data.thelook_ecommerce.products` AS p
  INNER JOIN `bigquery-public-data.thelook_ecommerce.order_items` AS oi
  on p.id=oi.product_id
  where  oi.status LIKE '%Shipped%' or  oi.status LIKE '%Complete%'
  group by p.category, month
  order by month ASC
)
select
r.month, r.category , r.total_price, c.total_cost,
(r.total_price - c.total_cost) AS profit
FROM revenue_per_monthcategory as r
JOIN cost_per_monthcategry as c
ON r.MONTH=c.MONTH AND r.category=c.category
order by profit ASC

"""
df2 = pd.read_gbq(query, project_id='radiant-psyche-461915-k8', dialect='standard')
df2.head()



# This code generates a bar chart showing the monthly profit by category using the data frame `df2`.
import pandas as pd
import matplotlib.pyplot as plt



pivot_df = df2.pivot_table(
    index='month',
    columns='category',
    values='profit',
    aggfunc='sum'
).fillna(0)


pivot_df.plot(
    kind='bar',
    stacked=True,
    figsize=(12, 6),
    colormap='tab20c'
)
plt.title('Monthly Profit by Category')
plt.xlabel('Month')
plt.ylabel('Profit ($)')
plt.xticks(rotation=45)
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()





