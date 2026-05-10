import os
import pandas as pd


"""
Module for Excel file conversions.

This module provides functions to convert Excel files (XLSX) to CSV and vice versa.
"""

def convert_excel(input_file, output_file):
    """
    Convert an Excel file to CSV or a CSV file to Excel.

    Args:
        input_file (str): Path to the input file (XLSX or CSV).
        output_file (str): Path to the output file (CSV or XLSX).

    Raises:
        RuntimeError: If the conversion fails.
    """
    try:
        if output_file.lower().endswith(".csv"):
            df = pd.read_excel(input_file)
            df.to_csv(output_file, index=False)
        if output_file.lower().endswith(".xlsx"):
            df = pd.read_csv(input_file)
            df.to_excel(output_file, index=False)
        if output_file.lower().endswith(".pdf"):
            pass
    except Exception as e:
        raise RuntimeError(f"Error converting Excel file: {str(e)}")


# Usage example for convert_excel:
# convert_excel('input.xlsx', 'output.csv')
# Converts the input Excel file (XLSX) to a CSV file and saves it as output.csv.

# convert_excel('input.csv', 'output.xlsx')
# Converts the input CSV file to an Excel file (XLSX) and saves it as output.xlsx.





