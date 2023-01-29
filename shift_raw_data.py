import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

hydro_data_path = 'C:\\Projects\\cuvalley2023\\data\\zad3\\hydro.xlsx'
meteo_data_path = 'C:\\Projects\\cuvalley2023\\data\\zad3\\meteo.xlsx'

hydro_df = pd.read_excel(hydro_data_path, header=2,
                         names=['date', 'GŁOGÓW (151160060)', 'RACIBÓRZ-MIEDONIA (150180060)'],
                         converters={'data': pd.to_datetime})

meteo_df = pd.read_excel(meteo_data_path, header=1, converters={'data': pd.to_datetime}, sheet_name='dane')

hydro_df.shape
meteo_df.shape

# Hydro df clean
hydro_df = hydro_df.set_index('date')
hydro_df = hydro_df.rename(columns={'GŁOGÓW (151160060)': 'glogow', 'RACIBÓRZ-MIEDONIA (150180060)': 'raciborz'})

hydro_df.isna().sum()

# Meteo df clean
meteo_df = meteo_df.rename(columns={'Data': 'date'}).set_index('date')

# Drop status columns
to_drop = [c for c in meteo_df.columns if 'Status' in c]
meteo_df = meteo_df.drop(columns=to_drop)

meteo_df.shape

# Check nan
meteo_df.isna().sum()
meteo_df.isna().sum().sum()

# Fill na values
meteo_df = meteo_df.fillna(.0)

shifted_dfs = []
for i in range(1, 31):
    shifted_df = meteo_df.shift(i)
    shifted_df.columns = [c + f'-{i}' for c in shifted_df.columns]
    shifted_dfs.append(shifted_df)

meteo_df.shape
meteo_df.shape[1] * 31
shifted_dfs[0].shape

meteo_shifted_df = pd.concat([meteo_df] + shifted_dfs, axis=1)

shifted_dfs = []
for i in range(1, 31):
    shifted_df = hydro_df.shift(i)
    shifted_df.columns = [c + f'-{i}' for c in shifted_df.columns]
    shifted_dfs.append(shifted_df)

shifted_dfs.append(hydro_df)

for i in range(1, 31):
    shifted_df = hydro_df.shift(-i)
    shifted_df.columns = [c + f'+{i}' for c in shifted_df.columns]
    shifted_dfs.append(shifted_df)

len(shifted_dfs)

hydro_shifted_df = pd.concat(shifted_dfs, axis=1)

hydro_shifted_df.shape
meteo_shifted_df.shape

hydro_shifted_df.index = pd.DatetimeIndex(hydro_shifted_df.index)
meteo_shifted_df.index = pd.DatetimeIndex(meteo_shifted_df.index)

len(set(hydro_shifted_df.index).symmetric_difference(meteo_shifted_df.index))

# Concat hydro and meteo
df = pd.concat([meteo_shifted_df, hydro_shifted_df], axis=1)

df_ = df.copy()

df = df.dropna()

df = df.sample(n=df.shape[0], random_state=42)

df['year_sin'] = np.sin(2 * np.pi * df.index.dayofyear / 365)
df['year_cos'] = np.cos(2 * np.pi * df.index.dayofyear / 365)

# Check
plt.plot(range(len(df)), df['year_sin'].sort_index())
plt.plot(range(len(df)), df['year_cos'].sort_index())

# Chunks
chunk_size = math.ceil(df.shape[0] / 10)
chunk_ids = np.floor(np.array(range(len(df))) / chunk_size)

df['chunk_id'] = chunk_ids

df['chunk_id'].value_counts()

# Save
output_path = 'C:\\Projects\\cuvalley2023\\data\\zad3\\df_30.csv'
df.to_csv(output_path)

# Check saved file
df_check = pd.read_csv(output_path).set_index('date')
df_check.index = pd.DatetimeIndex(df_check.index)
df_check.drop(columns=['year_sin', 'year_cos']).equals(df.drop(columns=['year_sin', 'year_cos']))
