import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

output_path = 'C:\\Projects\\cuvalley2023\\data\\zad3\\df_30.csv'

# Read data
df = pd.read_csv(output_path).set_index('date')
df.index = pd.DatetimeIndex(df.index)

# Remove raciborz+ cols
len([c for c in df.columns if 'raciborz+' in c])
df = df.drop(columns=[c for c in df.columns if 'raciborz+' in c])

# Exclude Glogow and Raciborz history
df = df.rename(columns={'glogow+1': 'target'})

df = df.drop(columns=[c for c in df.columns if 'glogow' in c or 'raciborz' in c])

df.shape

# Max lag - 10
max_lag = 10
additional_cols = ['target', 'year_sin', 'year_cos', 'chunk_id']
all_meteo_cols = [c for c in df.columns if c not in additional_cols]

filtered_meteo_cols = []
for c in all_meteo_cols:
    if '-' not in c:
        continue
    else:
        lag = int(c.split('-')[1])
        if lag <= max_lag:
            filtered_meteo_cols.append(c)

df = df[filtered_meteo_cols + additional_cols]

df.shape

# Train test split
val_chunk = 0

train_df = df[df['chunk_id'] != val_chunk].drop(columns='chunk_id')
val_df = df[df['chunk_id'] == val_chunk].drop(columns='chunk_id')

df.shape
train_df.shape
val_df.shape

#
train_x = train_df.drop(columns='target')
train_y = train_df['target']

val_x = val_df.drop(columns='target')
val_y = val_df['target']

train_x.shape
train_y.shape

val_x.shape
val_y.shape

# Random Forest
rf = RandomForestRegressor(n_estimators=100)

rf.fit(train_x, train_y)

preds = rf.predict(val_x)

mean_squared_error(val_y, preds)**(1/2)


fi = pd.Series(rf.feature_importances_, index=train_x.columns)

fi = fi.sort_values(ascending=False)


so_col_name = 'Suma opadów [mm]'

# Column name groups
groups = []
groups.append([c for c in fi.index if so_col_name in c and '.' not in c])

max([int(c.split('.')[1].split('-')[0]) for c in fi.index if so_col_name in c and '-' in c and '.' in c])

for i in range(1, 86):
    groups.append([c for c in fi.index if so_col_name in c and f'.{i}-' in c] + [so_col_name + f'.{i}'])

len(groups)
[len(g) for g in groups]

importance_dfs = []
for group in groups:
    importance_dfs.append(fi[group])

importances = []
for index, df in enumerate(importance_dfs):
    highest_corr = int(df.index[0].split('-')[1])
    importances.append((index, highest_corr, df[0]))

for m in importances:
    print(m)
