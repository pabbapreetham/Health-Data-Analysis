import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('cleaned_data.csv')  # Replace 'your_data.csv' with your actual data file

# Select the columns of interest
columns_of_interest = ['age_at_s1', 'health_scale_s1', 'AHI_s1', 'avg_HR(nrem)_s1', 'avg_HR(rem)_s1',
                      'sys_bp_s1', 'dia_bp_s1', 'bmi_s1', 'avg_sao2_s1', 'smoking_status_s1']
df_filtered = df.loc[((df['smoking_status_s1'] == 0) | (df['smoking_status_s1'] == 2)) , :]
# df.loc[(df['smoking_status_s1'] == 1) , :]

# Calculate conditional probability P(Y|X)
def conditional_probability(df, X, Y, condition):
    filtered_data = df_filtered
    prob_Y_given_X = filtered_data[Y].mean()
    return prob_Y_given_X

# Define the variables
X = 'bmi_s1'  # Change this to your desired variable X
Y = 'avg_sao2_s1'           # Change this to your desired variable Y
condition = 'Non - Smokers '  # Specify the condition for filtering

# Calculate conditional probability P(Y|X)
prob_Y_given_X = conditional_probability(df, X, Y, condition)
print(f"Conditional average P({Y}|{X}) when {condition}: {prob_Y_given_X:.4f}")

# Plot distributions
plt.figure(figsize=(10, 5))

# Distribution of variable X
plt.subplot(1, 2, 1)
plt.hist(df[X], bins=20, color='skyblue', edgecolor='black')
plt.title(f'Distribution of {X}')
plt.xlabel(X)
plt.ylabel('Frequency')

# Distribution of variable Y given condition X
plt.subplot(1, 2, 2)
plt.hist(df_filtered[Y], bins=20, color='salmon', edgecolor='black')
plt.title(f'Distribution of {Y} given condition {X}')
plt.xlabel(Y)
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()