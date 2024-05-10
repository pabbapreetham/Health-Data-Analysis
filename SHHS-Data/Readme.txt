# Health Data Analysis using DoWhy

## Overview

This repository contains code for performing causal inference analysis on health data using the DoWhy library in Python. Causal inference allows us to understand the causal relationships between variables in observational data.

## Installation

To run the code in this repository, you'll need to install the required libraries. You can install them using pip:


## Usage

1. **Data Preparation**: 
    - Prepare your health data in a CSV format. Ensure that your data contains columns for variables such as 'bmi_s1' (treatment), 'avg_sao2_s1' (outcome), 'age_at_s1', 'gender', 'hypertension_s1', 'smoking_status_s1' (common causes).
    - Save the CSV file as 'cleaned_data.csv' in the same directory as the code files.

2. **Causal Inference Analysis**:
    - Run the `causal_analysis.py` script to perform causal inference analysis on the health data.
    - The script loads the data, defines the causal model, identifies causal effects, estimates the effects using linear regression, and prints the results.
    - Adjust the treatment, outcome, and common causes variables in the `CausalModel` constructor according to your data.

3. **Interpreting Results**:
    - After running the script, you'll get the estimated causal effect printed in the console.
    - Additionally, the script generates a causal graph visualization (`causal_graph.png`) to depict the causal relationships between variables.

## File Structure

- `causal_analysis.py`: Main script for performing causal inference analysis.
- `cleaned_data.csv`: Sample health data in CSV format.
- `README.md`: Documentation file providing an overview of the repository.

## Requirements

- Python 3.x
- pandas
- dowhy

