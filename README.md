# sqlalchemy-chellenge


Instructions
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

Part 1: Analyze and Explore the Climate Data
In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib.

Part 2: Design Your Climate App
Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed.

This project performs exploratory data analysis on climate data from Hawaii using a SQLite database. It includes a Flask API that provides weather data routes such as precipitation, stations, and temperature observations.

Requirements:
Python 3.x

Libraries:
sqlalchemy
pandas
flask
matplotlib
numpy

Overview
Data Source:
hawaii.sqlite database
containing weather station data.

Analysis:
Retrieves and visualizes the last 12 months of precipitation data.
Identifies the most active weather station.
Analyzes temperature data for the most active station.

## API: A Flask-based API that serves climate data through various endpoints.
# API Endpoints
Home Page: /
Lists all available routes. Precipitation Data: /api/v1.0/precipitation

Returns the last 12 months of precipitation data.

Stations Data: /api/v1.0/stations
Returns a list of all weather stations.

Temperature Observations: /api/v1.0/tobs
Returns temperature observations for the most active station in the last 12 months.

Temperature Statistics for Start Date: /api/v1.0/<start_date>
Returns minimum, average, and maximum temperatures starting from a given date.

Temperature Statistics for Date Range: /api/v1.0/<start_date>/<end_date>
Returns minimum, average, and maximum temperatures for a specific date range.
