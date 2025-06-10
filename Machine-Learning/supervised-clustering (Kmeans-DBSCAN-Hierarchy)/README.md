
# 🧠 Customer Segmentation Using Clustering Algorithms

This project demonstrates how unsupervised machine learning techniques can be used to segment customers based on demographic and behavioral attributes. The analysis is based on a synthetic dataset of 800 customers, and includes a full pipeline from data preprocessing to model evaluation.

## 📊 Project Overview

The aim of this project is to explore and compare different clustering methods to discover meaningful customer segments. This can help businesses design more targeted marketing strategies.

### ✅ Goals:

- Clean and preprocess the data (handle missing values, encode categorical features, standardize numerical ones)
- Perform exploratory data analysis (EDA)
- Apply three clustering algorithms:
  - K-Means
  - Hierarchical Clustering
  - DBSCAN
- Compare models using **Silhouette Score** and visualizations
- Interpret the resulting segments in a marketing context

## 🧷 Dataset

The dataset contains 800 customer records with the following features:

- `Gender` (categorical)
- `Age`
- `Annual Income`
- `Spending Score`

> Note: Gender is label-encoded in preprocessing.

## 🛠️ Tools & Libraries

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- SciPy (for hierarchical clustering)

## 🚀 Result Summary 

|Algorithm  | Clusters | Best Silhouette Score | Result|
|-----------| -------- | --------------------- | ------ |
|K-Means|2, 4, 10| **0.46 (k=2)**| Chose **k=4** for best trade-off between performance & usability
|Hierarchical |2, 4, 6 | ~0.33 | Easy to interpret but lower performance
|DBSCAN| varies | Up to **0.46** | Detected noise & outliers, but produced too many segments (20+)

## 💡 Business Insights

| Segment | Characteristics | Category Suggestion |
|---------| --------------- | ------------------- |
|0 | Low income, high spending | Price-sensitive promos |
| 1 | Mixed profiles | Needs deeper behavioral analysis |
| 2 | High income, moderate spending | VIP/up-sell opportunity |
| 3 | Low income, low spending | Basic value-driven campaigns |

## 📌 Future Work

- Incorporate behavioral data (e.g., purchase frequency, recency)

- Test additional clustering models like Gaussian Mixture Models

- Automate parameter tuning for DBSCAN