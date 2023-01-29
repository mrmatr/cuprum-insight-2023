import pandas as pd
from sklearn.decomposition import PCA
from sklearn.linear_model import ElasticNet, Lasso
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler

output_path = 'C:\\Projects\\cuvalley2023\\data\\zad3\\df_30.csv'

# Read data
df = pd.read_csv(output_path).set_index('date')
df.index = pd.DatetimeIndex(df.index)

# Remove raciborz+ cols
len([c for c in df.columns if 'raciborz+' in c])
df = df.drop(columns=[c for c in df.columns if 'raciborz+' in c])

# Train test split
val_chunk = 0

train_df = df[df['chunk_id'] != val_chunk].drop(columns='chunk_id')
val_df = df[df['chunk_id'] == val_chunk].drop(columns='chunk_id')

df.shape
train_df.shape
val_df.shape


# Choose target
# Pred day: (+1, 2, ... 30)
pred_day = 1

train_x = train_df.drop(columns=[c for c in df.columns if 'glogow+' in c])
train_y = train_df[f'glogow+{pred_day}']

val_x = val_df.drop(columns=[c for c in df.columns if 'glogow+' in c])
val_y = val_df[f'glogow+{pred_day}']

train_x.shape
train_y.shape

val_x.shape
val_y.shape

# Scaler
scaler_x = MinMaxScaler()
scaler_y = MinMaxScaler()

train_x_scaled = scaler_x.fit_transform(train_x)
train_y_scaled = scaler_y.fit_transform(train_y.to_numpy().reshape(-1, 1))

val_x_scaled = scaler_x.transform(val_x)
val_y_scaled = scaler_y.transform(val_y.to_numpy().reshape(-1, 1))

# PCA
# pca = PCA(n_components=200)
#
# train_x_pca = pca.fit_transform(train_x_scaled)
# val_x_pca = pca.transform(val_x_scaled)
#
# train_x_pca.shape
# val_x_pca.shape
#
# pca.explained_variance_ratio_.cumsum()

# Model
alpha = 0.001
l1_ratio = 0.84

model = ElasticNet(alpha, l1_ratio)
# model = Lasso(alpha)

model.fit(train_x_scaled, train_y_scaled)
preds_scaled = model.predict(val_x_scaled)
preds = scaler_y.inverse_transform(preds_scaled.reshape(-1, 1))

mean_squared_error(val_y, preds)**(1/2)
# 12.677912233165253
