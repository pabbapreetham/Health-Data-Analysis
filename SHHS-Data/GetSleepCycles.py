import csv
import os
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np

# Function to generate CSV file containing cycle information
def generateOutputCsv():
    outFile = pd.DataFrame([(patient_ids[i], cycles[i], avgCycleLengthList[i] * 30, LongestCycleList[i]* 30, shortestCycleList[i]* 30, standardDeviationList[i]* 30) for i in range(0, len(patient_ids))],columns=['Patient Id','No of Cycles','Average Cycle Length','Longest Cycle length', 'Shortest Cycle Length','Standar Deviation'])
    outFile.to_csv('./extra/outputcycles.csv', index=False)
    return outFile

# Function to generate CSV file containing sleep stage sequences
def generateOutputCsvForSleepStageSequence():
    outputFile = pd.DataFrame([(patient_ids[i], j+1, sleepStagesAllPatientsList[i][j], len(sleepStagesAllPatientsList[i][j])) for i in range(0, len(patient_ids)) for j in range(0, len(sleepStagesAllPatientsList[i]))], columns=['Patient Id', 'Cycle','Sequence', 'Number of Stages'])
    outputFile.to_csv('./rhealthy/Result/Group1-cycles-avgStages.csv', index=False)
    return outputFile

# Function to calculate average number of sleep stages for each patient
def getAverageNumberOfSleepStagesForEachPatient():
    for stages in sleepStagesAllPatientsList:
        totCount = 0
        for eachCycle in stages:
            totCount += len(eachCycle)
        avg = totCount/len(stages)
        averageSleepStagesList.append(avg)

# Function to generate sleep stage sequence
def generate_sequence(result_list):
    sequence = []
    current_str = ""
    prev = -1
    count = 0
    for el in result_list:
        count += 1
        if el !=  5:
            if prev == 5:
                sequence.append([current_str,count])
                current_str = ""
                count = 0
        if el != prev:
            current_str += str(el)
        prev = el
    if prev == 5:
        sequence.append([current_str,count])
        current_str = ""
        count = 0
    if len(sequence) == 0:
        sequence.append([0,0])
    return sequence

# Function to get the number of sleep cycles from a CSV file
def get_number_of_sleep_cycles(file_path, column_name):
    target_value = 5
    try:
        df = pd.read_csv(file_path)
        if column_name not in df.columns:
            print(f"Column '{column_name}' not found in the CSV file.")
            return
        mask = (df[column_name] == target_value) & ~(df[column_name].shift(1) == target_value)
        count = mask.sum()
        cycles.append(count)
        data_column = df[column_name].tolist()
        result_list = [data_column[0]]
        for num in data_column[1:]:
            if num != result_list[-1]:
                result_list.append(num)
        result_sequence = generate_sequence(data_column)
        temp = []
        if len(result_sequence) == 0:
            print("empty")
            print(file_path)
            return result_sequence
        maxV = result_sequence[0][1]
        minV = result_sequence[0][1]
        for list in result_sequence:
            temp.append(list[1])
            maxV = max(maxV, list[1])
            minV = min(minV, list[1])
        avglength = sum(temp)/len(temp)
        st = np.std(temp)
        avgCycleLengthList.append(avglength)
        LongestCycleList.append(maxV)
        shortestCycleList.append(minV)
        standardDeviationList.append(st)
        return result_sequence
    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Get patient IDs from CSV files
csv_folder = 'extracsv'
patient_ids = get_ids(csv_folder)
print(patient_ids)

# Initialize lists
cycles = []
totalCycles = 0
numberOfIds = 19
sleepStagesAllPatientsList = []
avgCycleLengthList = []
LongestCycleList = []
shortestCycleList = []
standardDeviationList = []
averageSleepStagesList = []

# Loop through CSV files
for filename in os.listdir(csv_folder):
    if filename.endswith('.csv') :
        file_path = os.path.join(csv_folder, filename)
        res = get_number_of_sleep_cycles(file_path, column_name)

# Generate output CSV files
i = 0
for filename in os.listdir(csv_folder):
    if str(patient_ids[i]) not in filename:
        print('yes')
    i+=1
    if filename.endswith('.csv') :
        generateOutputCsv()
        # generateOutputCsvForSleepStageSequence()

# Calculate total cycles
totalCycles = sum(cycles) / len(cycles)
print(f"The average number of sleep cycles for group of patients is: {totalCycles}")
