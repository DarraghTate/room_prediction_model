import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import requests
import sys

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  
from tensorflow import keras
import pandas as pd
pd.set_option('display.max_columns', None)

model = keras.models.load_model('model.h5')

app = Flask(__name__)
CORS(app)

def time_convert(time):
    from datetime import datetime

    try:
        time_reformat = datetime.strptime(time, '%d-%m-%Y %H:%M')
    except ValueError:
        print(f'Incorrect Format')
        return

    day_of_week = time_reformat.weekday()
    hour = time_reformat.hour
    month = time_reformat.month

    if day_of_week == 5 or day_of_week == 6:
        is_weekend = 1
    else:
        is_weekend = 0

    mon, tue, wed, thur, fri, sat, sun = 0, 0, 0, 0, 0, 0, 0
    if day_of_week == 0:
        mon = 1
    elif day_of_week == 1:
        tue = 1
    elif day_of_week == 2:
        wed = 1
    elif day_of_week == 3:
        thur = 1
    elif day_of_week == 4:
        fri = 1
    elif day_of_week == 5:
        sat = 1
    elif day_of_week == 6:
        sun = 1

    spring, summer, autumn, winter = 0,0,0,0
    i = month
    if i == 1 or i == 2 or i == 12:
        winter = 1
    elif i == 5  or i == 3 or i == 4:
        spring = 1
    elif i == 8 or i == 6 or i == 7:
        summer = 1
    else:
        autumn = 1

    is_during_semester = 1

    # If it's December, June, July, August or Saturday or Sunday it's not during semester
    if month == 12 or month == 6 or month == 7 or month == 8 or day_of_week == 5 or day_of_week == 6:
        is_during_semester = 0

    jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    if month == 1:
        jan = 1
    elif month == 2:
        feb = 2
    elif month == 3:
        mar = 1
    elif month == 4:
        apr = 1
    elif month == 5:
        may = 1
    elif month == 6:
        jum = 1
    elif month == 7:
        jul = 1
    elif month == 8:
        aug = 1
    elif month == 9:
        sep = 1
    elif month == 10:
        oct = 1
    elif month == 11:
        nov = 1
    elif month == 12:
        dec = 1


    data = {'day_of_week': [day_of_week], 'hour': [hour], 'month':[month], 'is_weekend': [is_weekend], 
    'monday':[mon],'tuesday':[tue],'wednesday':[wed],'thursday':[thur],'friday':[fri],'saturday':[sat],'sunday':[sun],
    'spring':[spring], 'summer':[summer],'autumn':[autumn], 'winter':[winter],
    'jan':[jan], 'feb':[feb],'mar':[mar],'apr':[apr], 'may':[may], 'jun':[jun], 'jul':[jul], 'aug':[aug], 'sep':[sep], 'oct':[oct], 'nov':[nov], 'dec':[dec],
    'is_during_semester':[is_during_semester]
    }

    data = pd.DataFrame(data)
    return(data)


@app.route('/', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    data = data['data']
    data = time_convert(data)
    data = data[['is_weekend', 'friday', 'saturday', 'tuesday', 'thursday', 'hour', 'sunday', 'wednesday', 'monday','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec', 'is_during_semester','spring','summer','autumn','winter']]
    result = model.predict(data)
    output = {'results': int(result[0])}
    result = output.get('results')
    response = jsonify(results=output)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get', methods = ['GET'])    
def get():
    params = {'data':'20-03-2021 13:00'}
    url = 'http://localhost:5000/'
    params = json.dumps(params)
    response = requests.post(url, params)

    print(f'RESPONSE: {response.json()}')
    return str(response.json)
    
if __name__ == '__main__':
    app.logger.warning('testing warning log')
    app.run(port = 5000, debug=True)
