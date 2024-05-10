import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Load data from CSV file into a DataFrame
df_filtered = pd.read_csv('All_patients.csv')

# Example of filtering data based on specific conditions
# df_filtered = df.loc[((df['hypertension'] == 1) & (df['cardiac_surgery'] == 1)) & ((df['smoking_status'] == 0) | (df['smoking_status'] == 2)) , :]
# df_filtered = df.loc[((df['hypertension'] == 1)) & ((df['smoking_status'] == 0) | (df['smoking_status'] == 2)) , :]
# df_filtered = df.loc[((df['smoking_status_s1'] == 0) | (df['smoking_status_s1'] == 2)) , :]
# df_filtered = df.loc[(df['stroke_s1'] == 1) , :]

# Extracting data for analysis
x = df_filtered['avg_HR(nrem)_s1'].values.reshape(-1, 1)
y = df_filtered['bmi_s1'].values

# Polynomial regression
poly_features = PolynomialFeatures(degree=2)  # You can change the degree as needed
x_poly = poly_features.fit_transform(x)
model = LinearRegression()
model.fit(x_poly, y)

# Predictions
x_range = np.linspace(min(x), max(x), 100).reshape(-1, 1)
x_range_poly = poly_features.transform(x_range)
y_pred = model.predict(x_range_poly)

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x_range, y_pred, color='red', label='Curve fit')
plt.title('bmi_s1 vs. avg_HR(nrem)_s1')
plt.xlabel('avg_HR(nrem)_s1')
plt.ylabel('bmi_s1')
plt.legend()
plt.grid()
plt.show()

# Calculate correlation coefficient
correlation_coefficient = df_filtered['avg_HR(nrem)_s1'].corr(df_filtered['bmi_s1'])

# Print correlation coefficient
print("Correlation coefficient:", correlation_coefficient)
