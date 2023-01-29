import pandas as pd

output_path = 'C:\\Projects\\cuvalley2023\\data\\zad3\\df_30.csv'

# Read data
df = pd.read_csv(output_path).set_index('date')
df.index = pd.DatetimeIndex(df.index)

# Remove raciborz+ cols
len([c for c in df.columns if 'raciborz+' in c])
df = df.drop(columns=[c for c in df.columns if 'raciborz+' in c])

# Correlation - remove cols
gp_cols = [c for c in df.columns if 'glogow+' in c]
gm_cols = [c for c in df.columns if 'glogow-' in c]
_to_drop = list(df.columns[-3:]) + gp_cols + gm_cols

len(_to_drop)

df_corr = df.drop(columns=_to_drop)

corr_matrix = df_corr.corr()

glogow_corr = corr_matrix['glogow'].sort_values(ascending=False)

so_col_name = 'Suma opadów [mm]'

# Column name groups
groups = []
groups.append([c for c in glogow_corr.index if so_col_name in c and '.' not in c])

max([int(c.split('.')[1].split('-')[0]) for c in glogow_corr.index if so_col_name in c and '-' in c and '.' in c])

for i in range(1, 86):
    groups.append([c for c in glogow_corr.index if so_col_name in c and f'.{i}-' in c] + [so_col_name + f'.{i}'])

len(groups)
[len(g) for g in groups]

glogow_corr_dfs = []
for group in groups:
    glogow_corr_dfs.append(glogow_corr[group])

meteo_corr = []
for index, df in enumerate(glogow_corr_dfs):
    highest_corr = int(df.index[0].split('-')[1])
    meteo_corr.append((index, highest_corr))

for m in meteo_corr:
    print(m)
