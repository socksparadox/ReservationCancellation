# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 01:42:47 2023

@author: hp
"""

from flask import Flask, render_template, request
import pandas as pd
import pickle

model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/details')
def pred():
    return render_template('predict.html')

@app.route('/predict',methods = ['GET','POST'])
def predict():
    no_of_adults = request.form['no_of_adults']
    no_of_children = request.form['no_of_children']
    no_of_weekend_nights = request.form['no_of_weekend_nights']
    no_of_week_nights = request.form['no_of_week_nights']
    type_of_meal_plan = request.form['type_of_meal_plan']
    required_car_parking_space = request.form['required_car_parking_space']
    room_type_reserved = request.form['room_type_reserved']
    lead_time = request.form['lead_time']
    arrival_year = request.form['arrival_year']
    arrival_month = request.form['arrival_month']
    arrival_date = request.form['arrival_date']
    market_segment_type = request.form['market_segment_type']
    repeated_guest = request.form['repeated_guest']
    no_of_previous_cancellations = request.form['no_of_previous_cancellations']
    no_of_previous_bookings_not_canceled = request.form['no_of_previous_bookings_not_canceled']
    avg_price_per_room = request.form['avg_price_per_room']
    no_of_special_requests = request.form['no_of_special_requests']
        
    total = [[no_of_adults, no_of_children, no_of_weekend_nights, no_of_week_nights,
              type_of_meal_plan,required_car_parking_space, room_type_reserved,
              lead_time, arrival_year, arrival_month, arrival_date, market_segment_type,
              repeated_guest, no_of_previous_cancellations, no_of_previous_bookings_not_canceled,
              avg_price_per_room, no_of_special_requests]]
    d1 = pd.DataFrame(data = total, columns = ['no_of_adults', 'no_of_children', 'no_of_weekend_nights',
                                               'no_of_week_nights', 'type_of_meal_plan', 'required_car_parking_space',
                                               'room_type_reserved', 'lead_time', 'arrival_year', 'arrival_month',
                                               'arrival_date', 'market_segment_type', 'repeated_guest',
                                               'no_of_previous_cancellations', 'no_of_previous_bookings_not_canceled',
                                               'avg_price_per_room', 'no_of_special_requests'])
    prediction = model.predict(d1)
    prediction = prediction[0]
    if prediction == 0:
        return render_template('results.html', prediction_text = "The Reservation will not be cancelled")
    else:
        return render_template('results.html', prediction_text = "The Reservation will be cancelled")
    
if __name__ == "__main__":
    app.run(debug= True)