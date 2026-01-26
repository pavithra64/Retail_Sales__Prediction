import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(page_title="Retail Sales Prediction", layout="centered")

st.title("🛒 Retail Sales Prediction App")
st.write("Predict daily store sales")

import urllib.request

MODEL_URL = "https://huggingface.co/Pavithra64/Retail_sales_prediction/blob/main/random_forest_model.pkl"
MODEL_PATH = "random_forest_model.pkl"

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        with st.spinner("Downloading model..."):
            urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
    return joblib.load(MODEL_PATH)

model = load_model()

print(model.feature_names_in_)

# -------- Inputs --------
dayofweek = st.selectbox("Day Of Week", [1,2,3,4,5,6,7])

customers = st.number_input("Number of Customers", min_value=0, step=10)

promo = st.selectbox("Promo", [0, 1])
stateholiday = st.selectbox("State Holiday", [0, 1])
schoolholiday = st.selectbox("School Holiday", [0, 1])

month = st.selectbox("Month", list(range(1,13)))
day = st.selectbox("Day", list(range(1,32)))

storetype = st.selectbox("Store Type", [0, 1, 2])
assortment = st.selectbox("Assortment", [0, 1, 2])

competitiondistance = st.number_input("Competition Distance", min_value=0.0)
competitionopensincemonth = st.number_input(
    "Competition Open Since Month", min_value=1, max_value=12
)
competitionopensinceyear = st.number_input(
    "Competition Open Since Year", min_value=1990, max_value=2025
)

promo2 = st.selectbox("Promo2", [0, 1])

storetype_map = {
    'A': 0,
    'B': 1,
    'C': 2
}

storetype_ui = st.selectbox(
    "Store Type",
    options=['A', 'B', 'C']
)


# Binary encoding
promo = 1 if promo == "Yes" else 0
schoolholiday = 1 if schoolholiday == "Yes" else 0
stateholiday = 1 if stateholiday == "Yes" else 0
Promo2 = 1 if promo2 == "Yes" else 0

# -------- Input DataFrame (MUST match training columns) --------
input_data = pd.DataFrame({
    'DayOfWeek': [dayofweek],
    'Customers': [customers],
    'Promo': [promo],
    'StateHoliday': [stateholiday],
    'SchoolHoliday': [schoolholiday],
    'Month': [month],
    'Day': [day],
    'StoreType': [storetype],
    'Assortment': [assortment],
    'CompetitionDistance': [competitiondistance],
    'CompetitionOpenSinceMonth': [competitionopensincemonth],
    'CompetitionOpenSinceYear': [competitionopensinceyear],
    'Promo2': [promo2]
})


# -------- Prediction --------
if st.button("Predict Sales"):
    prediction = model.predict(input_data)[0]
    st.success(f"📈 Predicted Sales: {int(prediction):,}")
