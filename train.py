import pandas as pd
from xgboost import XGBRegressor
import joblib

# load data
df = pd.read_csv("final_dataset.csv")

X = df.drop(columns=["price"])
y = df["price"]

# train model
model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5)
model.fit(X, y)

# save model
joblib.dump(model, "model.pkl")

print("Model trained and saved")
