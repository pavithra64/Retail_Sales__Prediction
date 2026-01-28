RETAIL SALES PREDICTION : Predicting sales of a major store chain Rossmann--

Using ML algorithms


Problem Description

Rossmann operates over 3,000 drug stores in 7 European countries. Currently, Rossmann store managers are tasked with predicting their daily sales for up to six weeks in advance. Store sales are influenced by many factors, including promotions, competition, school and state holidays, seasonality, and locality. With thousands of individual managers predicting sales based on their unique circumstances, the accuracy of results can be quite varied. You are provided with historical sales data for 1,115 Rossmann stores. The task is to forecast the "Sales" column for the test set. Note that some stores in the dataset were temporarily closed for refurbishment.

---
title: Retail Sales Prediction
emoji: 🛒
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: "1.53.1"
python_version: "3.10"
app_file: app.py
pinned: false
---

# 🛒 Retail Sales Prediction

This Streamlit app predicts **daily retail store sales** using a trained **Random Forest regression model**.

## 🚀 Features
- Predict sales based on store and promotion details
- Clean interactive UI built with Streamlit
- Machine Learning model trained using Scikit-learn
- Model hosted externally to avoid GitHub size limits

## 🧠 Model Details
- Algorithm: **Random Forest Regressor**
- Trained on historical retail sales data
- Features include:
  - Day of week
  - Customers
  - Promotions
  - Holidays
  - Store type & assortment
  - Competition distance

## 🖥️ How it Works
1. User inputs store and date-related features
2. App downloads the trained model if not available
3. Model predicts expected sales
4. Prediction is displayed instantly

## 📦 Tech Stack
- Python
- Streamlit
- Pandas
- Scikit-learn
- Joblib
- Hugging Face Spaces

## ⚠️ Notes
- Model file is not stored directly in the repository
- The app downloads the model securely at runtime

## 👩‍💻 Author
**Pavithra Palanivel**

---

✨ Deployed using **Hugging Face Spaces**

App URL: https://huggingface.co/spaces/Pavithra64/Retail_sales_prediction
