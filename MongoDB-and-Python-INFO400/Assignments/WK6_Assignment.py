"""
Week 6 Assignment: Association Rule Mining
Author: Sean Coggeshall

Processes the Online Retail transaction dataset from Kaggle using one-hot
encoding via TransactionEncoder, generates frequent itemsets with the
Apriori algorithm, and derives association rules to identify relationships
between purchased items.

Requirements: Python 3.x, pandas, numpy, mlxtend
Dataset: https://www.kaggle.com/datasets/tunguz/online-retail
"""

# ---------------------------
# Import Required Libraries
# ---------------------------
import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# ---------------------------
# Optional: Download dataset using kagglehub
# Uncomment the following lines if you wish to download automatically from Kaggle.
# import kagglehub
# path = kagglehub.dataset_download("tunguz/online-retail")
# print("Path to dataset files:", path)

# ---------------------------
# Data Loading and Basic Exploration
# ---------------------------
# Load the dataset using appropriate encoding
df_retail = pd.read_csv('Online_Retail.csv', encoding='ISO-8859-1')

# Print basic information about the dataset
print("The number of instances:", len(df_retail))
print("First 5 rows of the dataset:")
print(df_retail.head())

# ---------------------------
# Data Cleaning and Preprocessing
# ---------------------------
# Remove rows with missing item descriptions
df_retail = df_retail.dropna(subset=['Description'])
print("Rows after removing missing 'Description':", len(df_retail))

# Ensure the 'Description' column is treated as string
df_retail = df_retail.astype({"Description": str})

# Group transactions by InvoiceNo to create a list of itemsets (each transaction is a list of items)
transactions = df_retail.groupby('InvoiceNo')['Description'].apply(list).to_list()
print("Total number of transactions:", len(transactions))

# ---------------------------
# Data Transformation
# ---------------------------
# One-hot encode the transaction data using TransactionEncoder
encoder = TransactionEncoder()
encoded_array = encoder.fit(transactions).transform(transactions)
df_itemsets = pd.DataFrame(encoded_array, columns=encoder.columns_)
print("Transaction data successfully encoded into one-hot format.")
print("Shape of encoded dataset:", df_itemsets.shape)

# ---------------------------
# Frequent Itemset Generation
# ---------------------------
# Use the Apriori algorithm to generate frequent itemsets; set minimum support threshold to 0.025
min_support = 0.025  
frequent_itemsets = apriori(df_itemsets, min_support=min_support, use_colnames=True)
print("Number of frequent itemsets found:", len(frequent_itemsets))
print("\nTop 5 frequent itemsets sorted by support:")
print(frequent_itemsets.sort_values(by='support', ascending=False).head())

# ---------------------------
# Association Rules Generation
# ---------------------------
# Generate association rules with a confidence threshold of 0.3
min_confidence = 0.3
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)
print("Number of association rules generated:", len(rules))
print("\nTop Association Rules (first 10 rows):")
print(rules.iloc[:10, :7])  # Display columns: antecedents, consequents, support, confidence, lift, etc.

# Optionally, print additional rule metrics for further insight
print("\nAdditional Rule Metrics (Support, Confidence, Lift):")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head(10))

print("\nEnd of Analysis.")
