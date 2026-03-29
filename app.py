import streamlit as st
import pandas as pd
import joblib
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

#load data
df = pd.read_csv("final_dataset.csv")

X = df.drop(columns=["price"])
y = df["price"]

#model
model = joblib.load("model.pkl")


st.title("House Price Prediction")

# inputs
bedrooms = st.slider("Bedrooms", 1, 10, 3)
sqft = st.number_input("Sqft Living", 500, 10000, 1500)
lat = st.number_input("Latitude", 47.0, 48.0, 47.5)
long = st.number_input("Longitude", -123.0, -121.0, -122.2)
crime = st.number_input("Crime Rate", 0, 1000, 100)

# session state for prediction
if "prediction" not in st.session_state:
    st.session_state.prediction = None

# predict button
if st.button("Predict"):
    input_data = pd.DataFrame(
        [[bedrooms, sqft, lat, long, crime]],
        columns=X.columns
    )
    pred = model.predict(input_data)[0]
    st.session_state.prediction = pred

# show result (persistent)
if st.session_state.prediction is not None:
    st.success(f"Predicted Price: {st.session_state.prediction:.2f}")

# heat map
st.subheader("Price Heatmap")

m = folium.Map(location=[df["lat"].mean(), df["long"].mean()], zoom_start=10)

heat_data = [[row["lat"], row["long"], row["price"]] for _, row in df.iterrows()]
HeatMap(heat_data).add_to(m)

st_folium(m, width=700, height=500)

# crime map
st.subheader("Crime Heatmap")

m2 = folium.Map(location=[df["lat"].mean(), df["long"].mean()], zoom_start=10)

crime_data = [[row["lat"], row["long"], row["crime_rate"]] for _, row in df.iterrows()]
HeatMap(crime_data).add_to(m2)

st_folium(m2, width=700, height=500)
