import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import folium
from folium.plugins import HeatMap

def ranges_histo_passenger_trip_duration(data):
    # Visualize the range of values for passenger_count and trip_duration_minutes using histograms
    # Set the palette 
    palette = sns.color_palette("viridis", as_cmap=True)
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    #sns.histplot(data['passenger_count'], kde=True, bins=20)
    sns.histplot(data['passenger_count'], kde=True, bins=20, color=palette(0.5))
    plt.title('Distribution of Passenger Count')
    plt.xlabel('Passenger Count')
    plt.ylabel('Frequency')

    plt.subplot(1, 2, 2)
    sns.histplot(data['trip_duration_minutes'], kde=True, bins=50, color=palette(0.8))
    plt.title('Distribution of Trip Duration in Minutes')
    plt.xlabel('Trip Duration (minutes)')
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()
    
def city_map(data):
    # Create a map centered around New York City
    map_nyc = folium.Map(location=[40.7128, -74.0060], zoom_start=12)

    # Add heatmap for pickup locations
    pickup_heat_data = list(zip(data['pickup_latitude'], data['pickup_longitude']))
    HeatMap(pickup_heat_data, radius=10, blur=15, max_zoom=1).add_to(map_nyc)

    # Add heatmap for dropoff locations
    dropoff_heat_data = list(zip(data['dropoff_latitude'], data['dropoff_longitude']))
    HeatMap(dropoff_heat_data, radius=10, blur=15, max_zoom=1, gradient={0.4: 'blue', 0.65: 'lime', 1: 'red'}).add_to(map_nyc)

    # Save the map to an HTML file
    map_nyc.show_in_browser()
    #map_nyc.save('nyc_taxi_pickup_dropoff_heatmap.html')

def plot_duration(data):
    data.trip_duration.groupby(pd.cut(data.trip_duration, np.arange(1,7200,600))).count().plot(kind='barh',figsize = (18,5))
    plt.title('Trip Duration')
    plt.xlabel('Trip Counts')
    plt.ylabel('Trip Duration (seconds)')
    plt.show()
    
def geo_plot(data):
    city_long_border = (-74.03, -73.75)
    city_lat_border = (40.63, 40.85)
    fig, ax = plt.subplots(ncols=2, sharex=True, sharey=True,figsize = (12,5))
    ax[0].scatter(data['pickup_longitude'].values, data['pickup_latitude'].values,
    color='blue', s=1, label='train', alpha=0.1)
    ax[1].scatter(data['dropoff_longitude'].values, data['dropoff_latitude'].values,
    color='green', s=1, label='train', alpha=0.1)
    ax[1].set_title('Drop-off Co-ordinates')
    ax[0].set_title('Pick-up Co-ordinates')
    ax[0].set_ylabel('Latitude')
    ax[0].set_xlabel('Longitude')
    ax[1].set_ylabel('Latitude')
    ax[1].set_xlabel('Longitude')
    plt.ylim(city_lat_border)
    plt.xlim(city_long_border)
    plt.show()
    
def clock(ax, radii, title, color):
    N = 24
    bottom = 2

    # create theta for 24 hours
    theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)

    # width of each bin on the plot
    width = (2*np.pi) / N
    
    bars = ax.bar(theta, radii, width=width, bottom=bottom, color=color, edgecolor="#999999")

    # set the label to go clockwise and start from the top
    ax.set_theta_zero_location("N")
    # clockwise
    ax.set_theta_direction(-1)

    # set the label
    ax.set_xticks(theta)
    ticks = ["{}:00".format(x) for x in range(24)]
    ax.set_xticklabels(ticks)
    ax.set_title(title)

def trips_per_hour(data):
    plt.figure(figsize=(10,10))
    #ax = plt.subplot(2,2,1, polar=True)
    ax = plt.subplot(1, 1, 1, polar=True) # Use only one subplot for better centering
    # make the histogram that binned on 24 hour
    radii = np.array(data['pickup_hour'].value_counts(sort=False).tolist(), dtype="int64")
    title = "Trips per Hour of the Day"
    clock(ax, radii, title, "#66ffb2")
    plt.tight_layout() # Ensure everything fits well within the figure
    plt.show()

def trip_duration_vs_distance(data):
    plt.figure(figsize = (10,5))
    dur_dist = data.loc[(data.distance_km < 30) & (data.trip_duration < 1000), ['distance_km','trip_duration']]
    plt.scatter(dur_dist.trip_duration, dur_dist.distance_km , s=1, alpha=0.5)
    plt.ylabel('Distance (KM)')
    plt.xlabel('Trip Duration')
    plt.title('Distance v/s Trip Duration')
    plt.show()

    