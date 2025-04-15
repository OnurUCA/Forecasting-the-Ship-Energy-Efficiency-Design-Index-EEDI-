
import pandas as pd
from statsmodels.tsa.stattools import adfuller

# Load the Excel file (without specifying sheet name, it will read the first sheet)
file_path = "/Users/onuruca/Desktop/eedi meü denizcilik/Analiz/TANKER/Tanker_Phase_5.xlsx"  # Change this to your actual file path

# Read the first sheet of the Excel file
df = pd.read_excel(file_path)

# Ensure the 'Year' and 'EEDI' columns exist in the dataset
if "Year" in df.columns and "EEDI" in df.columns:
    # Calculate the average EEDI values per year
    df_time_series = df.groupby("Year")["EEDI"].mean()

    # Apply the ADF test
    adf_result = adfuller(df_time_series)

    # Format the results
    adf_output = {
        "ADF Test Statistic": adf_result[0],
        "p-value": adf_result[1],
        "Critical Values": adf_result[4],
        "Stationarity Result": "Stationary" if adf_result[1] < 0.05 else "Not Stationary"
    }

    print(adf_output)
else:
    print("Error: The required columns 'Year' and 'EEDI' were not found in the dataset.")
