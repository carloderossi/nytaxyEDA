import pandas as pd
import numpy as np
from geopy.distance import geodesic

def clean_duration(data):
    print(data.trip_duration.groupby(pd.cut(data.trip_duration, np.arange(1,max(data.trip_duration),3600))).count())

    # Convert trip duration to minutes for easier comparison
    data['trip_duration_minutes'] = data['trip_duration'] / 60

    # Display initial data summary for trip_duration_minutes
    print("Initial summary for trip_duration_minutes:")
    print(data['trip_duration_minutes'].describe())

    # Clean values for trip_duration that are less than 1 minute or greater than 12 hours (720 minutes)
    data_cleaned = data[(data['trip_duration_minutes'] >= 1) & (data['trip_duration_minutes'] <= 720)]

    # Display cleaned data summary for trip_duration_minutes
    print("Cleaned summary for trip_duration_minutes:")
    print(data_cleaned['trip_duration_minutes'].describe())

    # Drop the temporary 'trip_duration_minutes' column if not needed anymore
    return data_cleaned.drop(columns=['trip_duration_minutes'])

""" # Remove outliers using IQR method
Q1 = df_filtered['trip_duration'].quantile(0.25)
Q3 = df_filtered['trip_duration'].quantile(0.75)
IQR = Q3 - Q1

data = df_filtered[
    (df_filtered['trip_duration'] >= (Q1 - 1.5 * IQR)) &
    (df_filtered['trip_duration'] <= (Q3 + 1.5 * IQR))
]
 """

# Function to calculate geodesic distance
def calculate_geodesic_distance(row):
    pickup_coords = (row['pickup_latitude'], row['pickup_longitude'])
    dropoff_coords = (row['dropoff_latitude'], row['dropoff_longitude'])
    return geodesic(pickup_coords, dropoff_coords).kilometers