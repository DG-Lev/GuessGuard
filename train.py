import pandas as pd

df = pd.read_csv('dataset.csv')
print(df.head())

x = df[['uppercase', 'lowercase', 'digits', 'symbols', 'length']]   
y = df['label']

print(x.shape)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print(x_train.shape, x_test.shape)

from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(x_train, y_train)

print("Training completed.")

from sklearn.metrics import mean_absolute_error

predictions = model.predict(x_test)
mae = mean_absolute_error(y_test, predictions)
print("MAE:", round(mae, 3))

import joblib
joblib.dump(model, 'model.pkl')
print("Model saved as model.pkl")