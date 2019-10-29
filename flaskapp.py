#!/usr/bin/env python
# coding: utf-8

# In[4]:


#import and get engine going
#get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mp
import datetime as dt
from datetime import datetime, timedelta


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#flask stuff
from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)


# In[5]:


#setting class references
Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)


# In[6]:


#getting flask going
app = Flask(__name__)
#whoops, need to go back to step 1 for flask stuff


# In[7]:


#setting routes
@app.route("/")
def homepage():
    """API routes"""
    return(
        f"Dates range is 23 Aug 2016 - 23 Aug 2017). <br><br>"
        f"Available Routes: <br>"

        f"/api/v1.0/precipitation<br/>"
        f"Dates and Temps <br><br>"

        f"/api/v1.0/stations<br/>"
        f"Stations <br><br>"

        f"/api/v1.0/tobs<br/>"
        f"Observations(tobs). <br><br>"

        f"/api/v1.0/yyyy-mm-dd/<br/>"
        f"Basic temp descriptives (mean, max, min) for a given start date<br><br>"

        f"/api/v1.0/yyyy-mm-dd/yyyy-mm-dd/<br/>"
        f"Basic descriptives (mean, max, min) for a given date range"
    )


# In[5]:



@app.route("/api/v1.0/precipitation")
def precipitation():
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= "2016-08-23", Measurement.date <= "2017-08-23").all()

    # jsonified list maker
    precipitation_list = [results]

    return jsonify(precipitation_list)

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.name, Station.station, Station.elevation).all()
# create dictionary
    station_list = []
    for result in results:
        row = {}
        row['name'] = result[0]
        row['station'] = result[1]
        row['elevation'] = result[2]
        station_list.append(row)
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def temp_obs():
    results = session.query(Station.name, Measurement.date, Measurement.tobs).filter(Measurement.date >= "2016-08-23", Measurement.date <= "2017-08-23").all()
#dictionary
    tobs_list = []
    for result in results:
        row = {}
        row["Station"] = result[0]
        row["Date"] = result[1]
        row["Temperature"] = int(result[2])
        tobs_list.append(row)

    return jsonify(tobs_list)

if __name__ == '__main__':
    app.run(debug=True)
    
    #Hmm, can't access the IP address. Might be a problem with my internet/router settings at home or I screwed this up.

