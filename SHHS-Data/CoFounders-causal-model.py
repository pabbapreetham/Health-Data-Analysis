import pandas as pd
import dowhy
from dowhy import CausalModel

# Load health data
data = pd.read_csv('cleaned_data.csv')  # Replace 'cleaned_data.csv' with your data file path

# Define causal model
model = CausalModel(
    data=data,
    treatment='bmi_s1',  # Apnea-Hypopnea Index
    outcome='avg_sao2_s1',   # Oxygen Saturation
    common_causes=['age_at_s1', 'gender', 'hypertension_s1', 'smoking_status_s1']  # Potential confounders
)

# Plot causal graph
model.view_model()

# Identify causal effect
identified_estimand = model.identify_effect()

# Estimate causal effect
estimate = model.estimate_effect(identified_estimand,
                                  method_name="backdoor.linear_regression")

# Print causal effect
print(estimate)
