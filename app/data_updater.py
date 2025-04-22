import pandas as pd

def append_new_data(new_data, csv_path, json_path):
    # Load existing data
    df = pd.read_csv(csv_path)

    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'], format='ISO8601', errors='coerce')

    # Append new data
    new_df = pd.DataFrame([new_data])
    df = pd.concat([df, new_df], ignore_index=True)

    # Save updated CSV
    df.to_csv(csv_path, index=False)