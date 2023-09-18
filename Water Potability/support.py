import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
pd.options.mode.chained_assignment = None  # default='warn'

water_data = pd.read_csv("./water_prediction.csv")

water_data_left = water_data.dropna()

cor = water_data_left.corr()

cor_target = abs(cor["Potability"])
r_f = cor_target[cor_target>0.1] 

input_cols = list(water_data_left.columns)[:-1]

output_cols = ["Potability"]

input_df = water_data_left[input_cols].copy()
output_df = water_data_left[output_cols].copy()
scaler = MinMaxScaler().fit(input_df[input_cols])
input_df[input_cols] = scaler.transform(input_df[input_cols])

def input(finalarray):
    final = {
    "ph" : finalarray[0][0],
    "Hardness"  : finalarray[0][1],
    "Solids" : finalarray[0][2],
    "Chloramines" : finalarray[0][3],
    "Sulfate" : finalarray[0][4],
    "Conductivity" : finalarray[0][5],
    "Organic_carbon": finalarray[0][6],
    "Trihalomethanes":finalarray[0][7],
    "Turbidity": finalarray[0][8]
    }

    new_input_df = pd.DataFrame([final])
    new_input_df[input_cols] = scaler.transform(new_input_df[input_cols])
    return new_input_df