import os
import pickle
import pandas as pd

# Define the base directory and file paths
BASE_DIR = '/mnt/data'
csv_path = os.path.join(BASE_DIR, "smartphone_cleaned_v1.csv")
pkl_path = os.path.join(BASE_DIR, "smartphone_price_model.pkl")

# Load CSV
df = pd.read_csv(csv_path)

# Load Pickle model
with open(pkl_path, "rb") as f:
    model = pickle.load(f)

# Show outputs
df.head(), type(model)
