# read_data.py - Module for reading temperature data from CSV files

import os
import csv

def get_all_data():
    """
    Retrieve all temperature data from CSV files in the 'temperatures' directory.

    Returns:
        List of dictionaries containing temperature data from all files.
    """
    temperature_data = []
    
    # Check if the 'temperatures' folder exists
    if not os.path.exists("temperatures"):
        print("Error: The 'temperatures' folder was not found!")
        return temperature_data
    
    # Get all CSV files in the 'temperatures' directory
    csv_files = [f for f in os.listdir("temperatures") if f.endswith('.csv')]
    if not csv_files:
        print("Error: No CSV files found in the 'temperatures' folder!")
        return temperature_data
    
    print(f"Reading {len(csv_files)} CSV files...")

    # Read data from each CSV file
    for csv_file in csv_files:
        file_path = os.path.join("temperatures", csv_file)
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                temperature_data.append(row)
        print(f"Successfully read: {csv_file}")
    
    print(f"Total rows of data read: {len(temperature_data)}")
    return temperature_data