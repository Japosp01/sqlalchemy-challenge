{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import and get engine going\n",
    "%matplotlib inline\n",
    "from matplotlib import style\n",
    "style.use('fivethirtyeight')\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib as mp\n",
    "import datetime as dt\n",
    "from datetime import datetime, timedelta\n",
    "\n",
    "\n",
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func\n",
    "\n",
    "#flask stuff\n",
    "from flask import Flask, jsonify\n",
    "\n",
    "engine = create_engine(\"sqlite:///hawaii.sqlite\")\n",
    "Base = automap_base()\n",
    "Base.prepare(engine, reflect=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#setting class references\n",
    "Measurement = Base.classes.measurement\n",
    "Station = Base.classes.station\n",
    "\n",
    "session = Session(engine)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "#getting flask going\n",
    "app = Flask(__name__)\n",
    "#whoops, need to go back to step 1 for flask stuff\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "#setting routes\n",
    "@app.route(\"/\")\n",
    "def homepage():\n",
    "    \"\"\"API routes\"\"\"\n",
    "    return(\n",
    "        f\"Dates range is 23 Aug 2016 - 23 Aug 2017). <br><br>\"\n",
    "        f\"Available Routes: <br>\"\n",
    "\n",
    "        f\"/api/v1.0/precipitation<br/>\"\n",
    "        f\"Dates and Temps <br><br>\"\n",
    "\n",
    "        f\"/api/v1.0/stations<br/>\"\n",
    "        f\"Stations <br><br>\"\n",
    "\n",
    "        f\"/api/v1.0/tobs<br/>\"\n",
    "        f\"Observations(tobs). <br><br>\"\n",
    "\n",
    "        f\"/api/v1.0/yyyy-mm-dd/<br/>\"\n",
    "        f\"Basic temp descriptives (mean, max, min) for a given start date<br><br>\"\n",
    "\n",
    "        f\"/api/v1.0/yyyy-mm-dd/yyyy-mm-dd/<br/>\"\n",
    "        f\"Basic descriptives (mean, max, min) for a given date range\"\n",
    "    )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Restarting with stat\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\The Doctor\\Anaconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py:3333: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "\n",
    "@app.route(\"/api/v1.0/precipitation\")\n",
    "def precipitation():\n",
    "        results = session.query(Measurement.date, Measurement.tobs).\\\n",
    "        filter(Measurement.date >= \"2016-08-23\", Measurement.date <= \"2017-08-23\").\\\n",
    "        all()\n",
    "\n",
    "    # jsonified list maker\n",
    "    precipitation_list = [results]\n",
    "\n",
    "    return jsonify(precipitation_list)\n",
    "\n",
    "@app.route(\"/api/v1.0/stations\")\n",
    "def stations():\n",
    "        results = session.query(Station.name, Station.station, Station.elevation).all()\n",
    "# create dictionary\n",
    "    station_list = []\n",
    "    for result in results:\n",
    "        row = {}\n",
    "        row['name'] = result[0]\n",
    "        row['station'] = result[1]\n",
    "        row['elevation'] = result[2]\n",
    "        station_list.append(row)\n",
    "    return jsonify(station_list)\n",
    "\n",
    "@app.route(\"/api/v1.0/tobs\")\n",
    "def temp_obs():\n",
    "        results = session.query(Station.name, Measurement.date, Measurement.tobs).\n",
    "        filter(Measurement.date >= \"2016-08-23\", Measurement.date <= \"2017-08-23\").\n",
    "        all()\n",
    "#dictionary\n",
    "        tobs_list = []\n",
    "    for result in results:\n",
    "        row = {}\n",
    "        row[\"Station\"] = result[0]\n",
    "        row[\"Date\"] = result[1]\n",
    "        row[\"Temperature\"] = int(result[2])\n",
    "        tobs_list.append(row)\n",
    "\n",
    "    return jsonify(tobs_list)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)\n",
    "    \n",
    "    #Hmm, can't access the IP address. Might be a problem with my internet/router settings at home or I screwed this up."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
