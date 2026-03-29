

# GeoSpatial Crime-Aware House Price Prediction

## Problem Statement

Traditional house price prediction models often ignore important real-world factors such as crime rates and spatial location, leading to inaccurate estimates. This project builds a machine learning system that incorporates geolocation and crime data to improve prediction accuracy.

## Features

* Predict house prices using XGBoost regression
* Incorporates crime rate and geospatial features (latitude, longitude)
* Interactive web application using Streamlit
* Price heatmap visualization
* Crime heatmap visualization

## Model Performance

* Train R²: 0.8679
* Test R²: 0.8044
* Train RMSE: 131,358
* Test RMSE: 171,966

## Tech Stack

* Python
* XGBoost
* Streamlit
* Folium
* Pandas
* NumPy
* Joblib

## Project Structure

```
project/
│
├── app.py
├── train.py
├── model.pkl
├── final_dataset.csv
├── requirements.txt
└── README.md
```

## How to Run

```
git clone <your-repo-link>
cd project

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt

python train.py
streamlit run app.py
```

## Screenshots

(Add images here: UI, price heatmap, crime heatmap)


