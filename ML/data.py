import pandas as pd
import numpy as np
import matplotlib as plt

data = pd.read_csv('data/Energy_and_Water_Data_Disclosure_for_Local_Law_84_2017__Data_for_Calendar_Year_2016_.csv')

data = data.replace({'Not Available': np.nan})

for col in list(data.columns):
    if 'ft²' in col or 'Kbtu' in col or 'Metric Tons CO2e' in col or 'kWh' in col or 'therms' in col or 'gal' in col or 'Score' in col:
        data['col'] = data[col].astype(float)
        print(data['col'])