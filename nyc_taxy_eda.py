import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

import graph_utils as gu
import data_utils as du

# Load the dataset
data = pd.read_csv('nyc_light.csv')

# Display the first few rows of the dataset
print(data.head())

# Step 2: Summary Statistics
print("Summary Statistics:\n", data.describe())
# Summary of attributes
print(data.info())

# Step 3: Missing Values Check
print("\nMissing Values:\n", data.isnull().sum())

# Convert datetime columns to datetime type for better analysis
data['pickup_datetime'] = pd.to_datetime(data['pickup_datetime'])
data['dropoff_datetime'] = pd.to_datetime(data['dropoff_datetime'])

# Create a new feature for trip duration in minutes
data['trip_duration_minutes'] = data['trip_duration'] / 60

gu.ranges_histo_passenger_trip_duration(data)

############ PASSENGERS 
# Clean values for passenger_count that are equal to 0 or greater than 6
data = data[(data['passenger_count'] > 0) & (data['passenger_count'] <= 6)]

# Display cleaned data summary for passenger_count
print("Cleaned summary for passenger_count:")
print(data['passenger_count'].describe())


#### TRIP DURATION
gu.plot_duration(data)
# Clean values for trip_duration that are less than 1 minute or greater than 12 hours (720 minutes)
data = du.clean_duration(data)


############# GEO DATA
gu.geo_plot(data)
#gu.city_map(data)

############ Pickup_HOUR
#Calculate and assign new columns to the dataframe such as weekday,
#month and pickup_hour which will help us to gain more insights from the data.
data['weekday'] = data.pickup_datetime.dt.day_name()
data['month'] = data.pickup_datetime.dt.month
data['weekday_num'] = data.pickup_datetime.dt.weekday
data['pickup_hour'] = data.pickup_datetime.dt.hour

gu.trips_per_hour(data)

print(data.info())
print(data.describe())

############## DISTANCE

# Apply the function to each row in the dataset
data['distance_km'] = data.apply(du.calculate_geodesic_distance, axis=1)

## there should be a linear relationship
gu.trip_duration_vs_distance(data)

print(data.info())
print(data.describe())

# Select relevant columns for correlation analysis
correlation_data = data[['passenger_count', 'pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'trip_duration', 'pickup_hour',  'month', 'weekday_num',  'distance_km']]

# Calculate the correlation matrix
correlation_matrix = correlation_data.corr()

# Print the correlation matrix as a table
print("Correlation Values:")
print(correlation_matrix)

# Create a correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap')
plt.show()

