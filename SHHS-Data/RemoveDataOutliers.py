import pandas as pd
import numpy as np

# Load your data into a pandas DataFrame
# Assuming 'data.xlsx' is the name of your Excel file
df = pd.read_csv('All_patients.csv')

# Define a function to detect outliers using z-score
def remove_outliers(df, columns, threshold=3):
    """
    Remove outliers from a DataFrame using z-score method.

    Parameters:
    - df: DataFrame
        The DataFrame containing the data.
    - columns: list
        List of column names to check for outliers.
    - threshold: int or float
        The z-score threshold for identifying outliers.

    Returns:
    - DataFrame
        DataFrame with outliers removed.
    """
    # Iterate over each column
    for col in columns:
        # Calculate z-score for each value in the column
        z_scores = np.abs((df[col] - df[col].mean()) / df[col].std())
        # Identify outliers using z-score threshold
        outliers = df[z_scores > threshold]
        # Remove outliers from the DataFrame
        df = df.drop(outliers.index)
    return df

# Specify columns to check for outliers
columns_to_check = ['age_at_s1', 'AHI_s1', 'avg_HR(nrem)_s1', 'avg_HR(rem)_s1',
                    'sys_bp_s1', 'dia_bp_s1', 'bmi_s1', 'avg_sao2_s1']

# Remove outliers from the DataFrame
df_cleaned = remove_outliers(df, columns_to_check)

# Save the cleaned DataFrame to a new Excel file
df_cleaned.to_csv('cleaned_data.csv', index=False)