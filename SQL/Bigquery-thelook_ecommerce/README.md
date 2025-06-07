# 🛍️ Profit Analysis in an E-Commerce Dataset with BigQuery & Python

## 💡 Project Overview

I explored Google BigQuery's public datasets to uncover business insights from real-world data. One of the datasets that caught my attention was from an e-commerce business in the apparel and accessories industry.

The first business question that came to my mind was:  
**"Where does the profit come from?"**  
Which **month** generates the most profit?  
Which **product categories** are the most and least profitable?

To answer these, I used **SQL (with CTEs)** to query the data in BigQuery and **Python (with pandas and matplotlib)** to visualize the results.

---

## 📊 What I Did

- Queried the `thelook_ecommerce` dataset from BigQuery using CTEs
- Calculated monthly revenue and cost by product category
- Computed profit by subtracting total cost from total revenue
- Visualized the results using a **stacked bar chart** in **matplotlib**
- Created a pivot table to organize profit by month and category

Although I usually find **Looker Studio** more intuitive and enjoyable for dashboards, I challenged myself to use `matplotlib` in Python for this post.

---

## 🧠 Key Insights

- **May (Month 5)** is the most profitable month overall.
- **Maternity** and **Outerwear** are the most profitable categories.
- **Suit Sets** are the least profitable product category.
- **August (Month 8)** shows the lowest overall profit.

Based on column names and product types, this dataset clearly belongs to a **fashion e-commerce** company.

---

## 📁 Project Structure

- `notebooks/`: Contains the Jupyter Notebook with queries and visualizations
- `images/`: Exported charts from matplotlib (optional)
- `README.md`: Project overview and insights

---

## 🚀 How to Run

1. Clone this repository
2. Open the notebook in Google Colab or your preferred environment
3. Ensure you have access to Google BigQuery (with the correct project ID)
4. Install dependencies (if local):
   - `pandas`
   - `matplotlib`
   - `google-cloud-bigquery` or use `pandas_gbq`

---

## 🔗 Dataset

This project uses the **[The Look E-commerce](https://console.cloud.google.com/marketplace/product/bigquery-public-data/thelook-ecommerce)** dataset from Google Cloud Public Datasets, available via BigQuery.
