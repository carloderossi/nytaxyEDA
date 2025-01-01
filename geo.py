import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

import graph_utils as gu
import data_utils as du

# Load the dataset
data = pd.read_csv('nyc.csv')

#gu.city_map(data)

# Define the bounding box for New York City
nyc_bounding_box = {
    'min_latitude': 40.4774,
    'max_latitude': 40.9176,
    'min_longitude': -74.2591,
    'max_longitude': -73.7004
}

# Filter data based on bounding box for both pickup and dropoff locations
data_cleaned = data[
    (data['pickup_latitude'] >= nyc_bounding_box['min_latitude']) &
    (data['pickup_latitude'] <= nyc_bounding_box['max_latitude']) &
    (data['pickup_longitude'] >= nyc_bounding_box['min_longitude']) &
    (data['pickup_longitude'] <= nyc_bounding_box['max_longitude']) &
    (data['dropoff_latitude'] >= nyc_bounding_box['min_latitude']) &
    (data['dropoff_latitude'] <= nyc_bounding_box['max_latitude']) &
    (data['dropoff_longitude'] >= nyc_bounding_box['min_longitude']) &
    (data['dropoff_longitude'] <= nyc_bounding_box['max_longitude'])
]

# Display the number of rows before and after cleaning
print(f"Original number of rows: {len(data)}")
print(f"Number of rows after cleaning: {len(data_cleaned)}")

# Save the cleaned dataset to a new CSV file
data_cleaned.to_csv('nyc_taxi_trip_duration_cleaned_nyc_only.csv', index=False)

print("The cleaned dataset with only NYC locations has been saved as nyc_taxi_trip_duration_cleaned_nyc_only.csv")

gu.city_map(data_cleaned)
