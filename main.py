from threading import Thread
from app.api import app
from app.data_updater import append_new_data
from datetime import datetime
import time

def simulate_real_time_updates():
    while True:
        # Simulate new data
        new_data = {
            "Date": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "Close": 0.95,
            "MarketCap": 2400000000,
            "Volume": 300000000
        }
        append_new_data(new_data, "data/sei-usd-max-updated.csv", "data/anomalies.json")
        time.sleep(60)  # Update every 60 seconds

if __name__ == "__main__":
    # Start real-time updates in a separate thread
    Thread(target=simulate_real_time_updates, daemon=True).start()

    # Run Flask API
    app.run(debug=True, port=5000)