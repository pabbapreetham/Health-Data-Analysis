import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the cleaned data into a pandas DataFrame
df_cleaned = pd.read_csv('cleaned_data.csv')

# Select the features (independent variables) and the target variable
# X = df_cleaned[['age_at_s1', 'health_scale_s1', 'avg_HR(nrem)_s1', 'avg_HR(rem)_s1',
#                 'sys_bp_s1', 'dia_bp_s1', 'bmi_s1', 'avg_sao2_s1']]
X = df_cleaned[['avg_HR(nrem)_s1', 'avg_HR(rem)_s1', 'sys_bp_s1', 'dia_bp_s1', 'bmi_s1',  'avg_sao2_s1', 'age_at_s1']]
y = df_cleaned['AHI_s1']  # Change 'subject_id' to your target variable if needed

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the degree of polynomial
degree = 2  # Change this value as desired

# Create polynomial features
poly = PolynomialFeatures(degree=degree)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Train the polynomial regression model
model = LinearRegression()
model.fit(X_train_poly, y_train)

# Predict on the test set
y_pred = model.predict(X_test_poly)

# Calculate mean squared error
mse = mean_squared_error(y_test, y_pred)

r_squared = r2_score(y_test, y_pred)

# Select another variable for the x-axis
x_variable = 'avg_HR(nrem)_s1'  # Change this to the desired variable

# Plot original values
plt.figure(figsize=(8, 6))
plt.bar(X_test[x_variable], y_test, color='red', label='Original', alpha=0.5)

# Plot expected values
plt.bar(X_test[x_variable], y_pred, color='blue', label='Expected', alpha=0.5)

# Add labels and title
plt.title('Original vs. Expected Values with Mean Squared Error')
plt.xlabel(x_variable)
plt.ylabel('AHI_s1')
plt.legend()

# Add mean squared error as text on the plot
plt.text(0.1, 0.9, 'Mean Squared Error: {:.2e}'.format(mse),
         horizontalalignment='left',
         verticalalignment='center',
         transform=plt.gca().transAxes,
         fontsize=12)

# Show plot
plt.grid(True)
plt.show()

print("R-squared:", r_squared)