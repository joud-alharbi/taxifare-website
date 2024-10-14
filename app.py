import streamlit as st
import requests
from datetime import datetime

# Title for the web app
st.title('TaxiFare Model Frontend🚗')

st.markdown('''
### Welcome to the Taxi Fare Prediction app!
Use the form below to input ride details and get an estimated fare.
''')

# 1. Date and time
pickup_datetime = st.text_input(
    'Enter pickup date and time (YYYY-MM-DD HH:MM:SS)',
    value=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)

# 2. Pickup longitude
pickup_longitude = st.number_input(
    'Enter pickup longitude',
    format="%.6f",
    value=-73.985428  # Default longitude
)

# 3. Pickup latitude
pickup_latitude = st.number_input(
    'Enter pickup latitude',
    format="%.6f",
    value=40.748817  # Default latitude
)

# 4. Dropoff longitude
dropoff_longitude = st.number_input(
    'Enter dropoff longitude',
    format="%.6f",
    value=-73.985428  # Default longitude
)

# 5. Dropoff latitude
dropoff_latitude = st.number_input(
    'Enter dropoff latitude',
    format="%.6f",
    value=40.748817  # Default latitude
)

# 6. Passenger count
passenger_count = st.number_input(
    'Enter number of passengers',
    min_value=1, max_value=8, value=1
)
api_url = st.secrets['api_url']

# Predict button
if st.button('Get Fare Prediction'):
    # Build a dictionary with input values
    params = {
        'pickup_datetime': pickup_datetime,
        'pickup_longitude': float(pickup_longitude),
        'pickup_latitude': float(pickup_latitude),
        'dropoff_longitude': float(dropoff_longitude),
        'dropoff_latitude': float(dropoff_latitude),
        'passenger_count': passenger_count
    }

    # Try to send the request to the API
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an exception for 4XX/5XX errors



        # Process and display the prediction
        prediction = response.json().get('fare', None)
        if prediction:
            st.success(f"The predicted fare is: ${prediction:.2f}")
        else:
            st.error("No fare returned. Check input parameters.")

    except requests.exceptions.RequestException as e:
        st.error(f"Error with API request: {e}")
