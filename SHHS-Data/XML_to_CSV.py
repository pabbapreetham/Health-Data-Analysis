import csv
import os
import xml.etree.ElementTree as ET

# Define a function to convert XML data to CSV format
def convert_xml_to_csv(xml_file, csv_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Open the CSV file for writing
    with open(csv_file, 'w', newline='') as csv_data:
        csv_writer = csv.writer(csv_data)

        # Define the header for the CSV file
        header = ['SleepStage']
        rows = []

        # Extract SleepStages/SleepStage elements from XML
        sleep_stages = []
        for sleep_stage in root.findall('SleepStages/SleepStage'):
            stage = sleep_stage.text
            sleep_stages.append(stage)

        # Add sleep stages to the rows list
        rows.append(sleep_stages)

        # Write the header and rows to the CSV file
        csv_writer.writerow(header)
        csv_writer.writerows(zip(*rows))

# Specify the folder containing XML files
xml_folder = 'extra'
csv_folder = 'extracsv'

# Create the output folder if it doesn't exist
os.makedirs(csv_folder, exist_ok=True)

# Iterate over XML files in the folder
for filename in os.listdir(xml_folder):
    if filename.endswith('.xml'):
        # Construct paths to XML and CSV files
        xml_file = os.path.join(xml_folder, filename)
        csv_file = os.path.join(csv_folder, os.path.splitext(filename)[0] + '.csv')
        
        # Convert XML to CSV
        convert_xml_to_csv(xml_file, csv_file)