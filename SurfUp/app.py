# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

# reflect an existing database into a new model
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect the tables
Base = automap_base()
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

#display available routes on landing page
@app.route("/")
def home():
    """List all available route."""
    return(
        "Available Routes:<br/>"
        "/api/v1.0/precipitation<br/>"
        "/api/v1.0/stations<br/>"
        "/api/v1.0/tobs<br/>"
        "/api/v1.0/start/<start><br/>"
        "/api/v1.0/start/<start>/end/<end><br/>"
    )

#route for precipitation - returns Json with Date as the KEY and the Value as precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the precipitation for the last year"""
    most_recent_date = session.query(func.max(Measurement.date)).first()
    one_year_ago = most_recent_date - dt.timedelta(days=365)

    # Query the precipitation data
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()

    # Create a dictionary with the date as the key and precipitation as the value
    precipitation_dict = {date: prcp for date, prcp in results}

    return jsonify(precipitation_dict)
    

#Stations route that returns Jsonified data of all the stations in the database
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station, Station.name).all()
    stations_list = [{station: name} for station, name in results]
    return jsonify(stations_list)

# tobs route return jsonified data for most active station USC00519281 - Only returns jsonified data for the last year of data
@app.route("/api/v1.0/tobs")
def tobs():
    active_station = "USC00519281"

    most_recent_date = session.query(func.max(Measurement.date)).first()
    one_year_ago = most_recent_date - dt.timedelta(days=365)

    tobs_data = session.query(Measurement.date, Measurement.tobs).filter(
        Measurement.station == active_station).filter(
        Measurement.date >= one_year_ago).all()
   
    tobs_list = [{date:tobs} for date, tobs in tobs_data]
    return jsonify(tobs_list)

#start route that accepts the start date as the parameter from teh URl
#return a min, max and AVG temp calculated from teh given start date to end date
@app.route("/api/v1.0/start/<start>")
def start(start):
    temps = session.query(
        func.min(Measurement.tobs), 
        func.max(Measurement.tobs),
        func.avg(Measurement.tobs)
    ).filter(Measurement.station >= start ).all()

    temp_stats = {
    'Start Date':start,
    'TMIN': results[0][0],
    'TAVG':results[0][1],
    'TMAX': reults[0][2]
    }

    return jsonify(temp_stats)

#Start/end route accepts that start and end dates as paramets from the URL
#returns min, max and avearge temps calcuate from teh given start date and end date
@app.route("/api/v1.0/start_end")
def start_end(start, end):
    temps = session.query(
        func.min(Measurement.tobs), 
        func.max(Measurement.tobs),
        func.avg(Measurement.tobs)
    ).filter(Measurement.station >= start ).filter(Measurement.date <= end).all()

    temp_stats = {
    'Start Date':start,
    'End Date': end,
    'TMIN': results[0][0],
    'TAVG':results[0][1],
    'TMAX': reults[0][2]
}

    return jsonify(temp_stats)

if __name__ == "__main__":
    app.run(debug=True)

session.close()