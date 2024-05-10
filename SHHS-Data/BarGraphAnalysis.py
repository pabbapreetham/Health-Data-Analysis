import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Load data from CSV file into a DataFrame
df = pd.read_csv('All_patients.csv')  

# Filter data based on specific conditions
# Example of filtered data based on specific conditions
# df_filtered = df.loc[((df['hypertension'] == 1) & (df['cardiac_surgery'] == 1)) & ((df['smoking_status'] == 0) | (df['smoking_status'] == 2)) , :]
# df_filtered = df.loc[((df['hypertension'] == 1)) & ((df['smoking_status'] == 0) | (df['smoking_status'] == 2)) , :]
# df_filtered = df.loc[((df['smoking_status_s1'] == 0) | (df['smoking_status_s1'] == 2)) , :]
# df_filtered = df.loc[(df['stroke_s1'] == 1) , :]

# Example of extracting specific columns for analysis
x = df_filtered['bmi_s1'].values.reshape(-1, 1)
y = df_filtered['avg_sao2_s1'].values

# Plotting
# Example of plotting data
plt.xticks(np.arange(11), np.arange(11))
plt.figure(figsize=(10, 6))
plt.bar(df['hypertension_s1'], df['avg_HR(nrem)_s1'], color='skyblue')
plt.title('hypertension_s1 vs. avg_HR(nrem)')
plt.xlabel('hypertension_s1')
plt.ylabel('avg_HR(nrem)_s1')
plt.grid(axis='y')
plt.show()

# Calculate correlation coefficient
correlation_coefficient = df['avg_HR(nrem)_s1'].corr(df['hypertension_s1'])

# Print correlation coefficient
print("Correlation coefficient:", correlation_coefficient)
