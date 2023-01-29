import json

import pandas as pd

input_path = 'C:\\Projects\\cuvalley2023\\data\\zad3\\df_30.csv'

# Read data
df = pd.read_csv(input_path).set_index('date')
df.index = pd.DatetimeIndex(df.index)

# Exclude columns
df = df.drop(columns=[c for c in df.columns if 'raciborz+' in c] + ['chunk_id', 'glogow+1'])

# Take first n rows
start_row = 0
end_row = 2

dict_data = df[start_row:end_row].to_dict(orient='rows')

# Prepare dict
dict_data = {
    'Inputs': {
        'data': dict_data
    },
    "GlobalParameters": 0.0
}

# Save as json
output_path = 'C:\\Projects\\cuvalley2023\\data\\zad3\\inference_data.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(dict_data, f, ensure_ascii=False)
