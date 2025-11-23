import os
import pickle
import pandas as pd

BASE_DIR = os.path.dirname(__file__)
df = pd.read_csv(os.path.join(BASE_DIR, "smartphone_cleaned_v1.csv"))
model = pickle.load(open(os.path.join(BASE_DIR, "smartphone_price_model.pkl"), "rb"))
