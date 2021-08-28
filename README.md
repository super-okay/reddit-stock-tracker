# Reddit Stock Tracker

## Overview
Tracks prices of stocks mentioned on r/wallstreetbets against how often they are mentioned. Built with Angular and Flask.

## Frontend
Angular.

```
cd frontend
cd rst-frontend
npm install
npm start
```

## Backend
Python Flask.


For first time environment setup, create a new Python virtual environment and install all packages specified in `requirements.txt`.
```
cd backend
python3 -m venv rst-env
source rst-env/bin/activate
python3 -m pip install -r requirements.txt
python3 -m flask run
```

If the virtual environment already exists and all packages are installed, simply start the environment and run.
```
cd backend
source rst-env/bin/activate
python3 -m flask run
```