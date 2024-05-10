import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Load original data
data = pd.read_csv('surgery_data.csv')
data0 = pd.read_csv('Surgery0.csv')
data1 = pd.read_csv('Surgery1.csv')
data2 = pd.read_csv('Surgery2.csv')

# Define a quadratic function for curve fitting
def func(x, a, b, c):
    return a * x**2 + b * x + c

# Function to generate synthetic data for a specific column using curve fitting
def generate_synthetic_data(column_data, num_samples, lower_limit=None, upper_limit=None):
    # Curve fitting using the defined function
    popt, _ = curve_fit(func, np.arange(len(column_data)), column_data)
    
    # Generate x values for synthetic data
    x_values = np.linspace(0, len(column_data), num_samples)
    
    # Generate synthetic samples using the curve fit
    synthetic_samples = [func(x, *popt) for x in x_values]

    # If lower_limit or upper_limit is not provided, set them to the min or max of column_data
    if lower_limit is None:
        lower_limit = np.min(column_data)
    if upper_limit is None:
        upper_limit = np.max(column_data)

    # Clip synthetic_samples to ensure they fall within the specified limits
    synthetic_samples = np.clip(synthetic_samples, lower_limit, upper_limit)

    # Additional constraints for specific columns
    if 'AHI_after_surgery' in column_data:
        synthetic_samples = np.clip(synthetic_samples, 2, 65)

    return synthetic_samples

# Number of synthetic samples to generate for each class
num_samples = 100

# Generate synthetic data for each column for class 0 (smoking_status = 0)
synthetic_data0 = {}
for col in data.columns:
    if col == 'smoking_status':
        synthetic_data0[col] = np.zeros(num_samples)
    elif col == 'hypertension' or col == 'cardiac_surgery':
        synthetic_data0[col] = np.where(generate_synthetic_data(data2[col], num_samples) > 0, 1, 0)
    elif col == 'age_at_surgery':
        synthetic_data0[col] = np.clip(generate_synthetic_data(data0[col], num_samples, 40, 75), 40, 75).astype(int)
    else:
        synthetic_data0[col] = generate_synthetic_data(data0[col], num_samples)

# Generate synthetic data for each column for class 1 (smoking_status = 1)
synthetic_data1 = {}
for col in data.columns:
    if col == 'smoking_status':
        synthetic_data1[col] = np.ones(num_samples)
    elif col == 'hypertension' or col == 'cardiac_surgery':
        synthetic_data1[col] = np.where(generate_synthetic_data(data2[col], num_samples) > 0, 1, 0)
    elif col == 'age_at_surgery':
        synthetic_data1[col] = np.clip(generate_synthetic_data(data1[col], num_samples, 40, 75), 40, 75).astype(int)
    else:
        synthetic_data1[col] = generate_synthetic_data(data1[col], num_samples)

# Generate synthetic data for each column for class 2 (smoking_status = 2)
synthetic_data2 = {}
for col in data.columns:
    if col == 'smoking_status':
        synthetic_data2[col] = np.ones(num_samples) * 2
    elif col == 'hypertension' or col == 'cardiac_surgery':
        synthetic_data2[col] = np.where(generate_synthetic_data(data2[col], num_samples) > 0, 1, 0)
    elif col == 'age_at_surgery':
        synthetic_data2[col] = np.clip(generate_synthetic_data(data2[col], num_samples, 40, 75), 40, 75).astype(int)
    else:
        synthetic_data2[col] = generate_synthetic_data(data2[col], num_samples)

# Combine original and synthetic samples
resampled_data2 = pd.concat([
    data,
    pd.DataFrame(synthetic_data0),
    pd.DataFrame(synthetic_data1),
    pd.DataFrame(synthetic_data2)
], ignore_index=True)

# Export DataFrame to CSV file
resampled_data2.to_csv('Surgery_resampled_data.csv', index=False)
