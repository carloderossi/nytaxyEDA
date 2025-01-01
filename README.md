# NYC Taxi Trip Duration EDA

## Overview

This project involves an exploratory data analysis (EDA) of the NYC Taxi Trip Duration dataset. The goal is to analyze various factors affecting taxi trip durations in New York City and uncover insightful patterns and trends.

## Dataset

The dataset used in this analysis contains detailed information about taxi trips in NYC, including:
- Pickup Date and Time
- Dropoff Date and Time
- Passenger Count
- Trip Distance
- Pickup and Dropoff Locations (Latitude and Longitude)
- Store and Forward Flag (whether the trip record was sent to the server during the trip or at the end of the trip)
- Trip Duration (target variable)

## Objective

The objective of this project is to perform a comprehensive exploratory data analysis to understand the factors influencing taxi trip durations in NYC. This includes:
- Identifying trends and patterns in the data
- Visualizing key features
- Analyzing the impact of different variables on trip duration
- Providing actionable insights based on the findings

## Approach

1. **Data Preprocessing**:
   - Handling missing values
   - Converting date and time fields to appropriate formats
   - Creating new features from existing ones (e.g., day of the week, hour of the day)
   - Encoding categorical variables

2. **Exploratory Data Analysis (EDA)**:
   - Descriptive statistics of the dataset
   - Distribution analysis of key features
   - Correlation analysis
   - Visualizations to identify patterns and trends (e.g., heatmaps, bar plots, scatter plots)

3. **Insights and Analysis**:
   - Analyzing trip duration distribution
   - Impact of pickup and dropoff locations on trip duration
   - Effect of time of day and day of the week on trip duration
   - Influence of passenger count on trip duration
   - Relationship between trip distance and trip duration

## Results

The results section includes:
- Visualizations of key findings
- Summary of patterns and trends identified during the analysis
- Key insights derived from the EDA

## Conclusion

## Summary of Data Quality

### Completeness
- The dataset is comprehensive, covering approximately 1.46 million records, providing a robust foundation for analysis.
- Key features such as `vendor_id`, `pickup_datetime`, `dropoff_datetime`, `passenger_count`, `pickup_longitude`, `pickup_latitude`, `dropoff_longitude`, `dropoff_latitude`, and `trip_duration` are well-documented.
- The data only contains the date range from January 1, 2016, to June 30, 2016, which limits the analysis of month, season, and weather impact.

### Consistency
- The data appears consistent, with no obvious discrepancies in key features.
- Coordinates for pickups and dropoffs are restricted within ranges of New York City.
- Observations for trips with passenger count = 0 and > 6 were removed.
- Trip durations were restricted to plausible values.

### Timeliness
- The dataset spans from January 1, 2016, to June 30, 2016, providing a six-month snapshot.
- Additional years of data could help in understanding long-term trends and seasonality.

### Accuracy
- Geographical data (longitude and latitude) centers around New York City.
- Trip durations are varied and align with expected ranges, though some outliers could be handled using the IQR method.

### Relevance
- The data is highly relevant for analyzing taxi trip patterns, customer behavior, and operational efficiency within New York City.

## Request for Additional Data

To enhance the depth and breadth of the analysis, it would be beneficial to gather additional data:

### Extended Timeframe
- Data from multiple years to identify long-term trends and year-over-year variations.

### Weather Data
- Historical weather data for New York City, including temperature, precipitation, and other conditions, to analyze the impact of weather on trip durations and demand.

### Traffic Data
- Real-time and historical traffic data to understand the influence of traffic conditions on trip times and optimize routing.

### Economic and Event Data
- Information on local events, holidays, and economic indicators to correlate with fluctuations in taxi demand.

### Customer Feedback
- Collecting and analyzing customer feedback and ratings to improve service quality and address satisfaction issues.

### Operational Data
- Details on vehicle availability, maintenance schedules, and driver performance for better fleet management and operational efficiency.


## References

- [NYC Taxi Trip Duration Dataset](https://www.kaggle.com/c/nyc-taxi-trip-duration/data)
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)

## Author

Carlo De Rossi
