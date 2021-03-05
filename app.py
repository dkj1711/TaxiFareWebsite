import streamlit as st
import requests
import pandas as pd
import datetime

'''
# TaxiFareModel front
'''

st.markdown("PICK UP AND DROP OFF")


pickup_datetime = st.text_input("date and time", value = '')
pickup_longitude = st.text_input("pickup_longitude", value = '')
pickup_latitude = st.text_input("pickup_latitude", value = '')
dropoff_longitude = st.text_input("dropoff_longitude", value = '')
dropoff_latitude= st.text_input("dropoff_latitude", value = '')
passenger_count = st.text_input("passenger_count", value = '')

if st.checkbox('Show content'):
    if pickup_datetime == '' or pickup_longitude == '' or pickup_latitude == '' or dropoff_longitude == '' or  dropoff_latitude == ''  or  passenger_count == '':
        st.write('missing values')
    
    else:
        url = 'http://taxifare.lewagon.ai/predict_fare/'
        params = {
            'key': 1,
            'pickup_datetime': pickup_datetime,
            'pickup_longitude': pickup_longitude,
            'pickup_latitude': pickup_latitude,
            'dropoff_longitude':dropoff_longitude,
            'dropoff_latitude': dropoff_latitude,
            'passenger_count': passenger_count
            }

        response = requests.get(url, params=params)

        st.write(response.json()['prediction'])

'''
## Once we have these, let's  retrieve a prediction
'''


