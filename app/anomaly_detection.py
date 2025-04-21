import pandas as pd
import json


class AnomalyDetectionModel:
    def __init__(self, threshold=2):
        self.threshold = threshold

    def detect_anomalies(self, df):
        mean_price = df['Close'].mean()
        std_price = df['Close'].std()

        # Calculate Z-score
        df['Z_score'] = (df['Close'] - mean_price) / std_price
        df['Anomaly'] = df['Z_score'].apply(lambda x: 'Yes' if abs(x) > self.threshold else 'No')
        anomalies = df[df['Anomaly'] == 'Yes']
        return anomalies

    def save_to_json(self, anomalies, json_path):
        anomalies_dict = anomalies.to_dict(orient='records')
        with open(json_path, "w") as file:
            json.dump(anomalies_dict, file, indent=4, default=str)