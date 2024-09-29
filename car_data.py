import streamlit as st
import pandas as pd
from urllib.request import urlopen
import json


def display_car_data():
    st.header("Car Data")
# showing attributes
    st.write(""" 
                       **Attributes:**
                       - **Brake**: Whether the brake pedal is pressed (100) or not (0).
                       - **Date**: The UTC date and time.
                       - **Driver Number**: Unique F1 driver number.
                       - **Gear**: Current gear selection.
                       - **RPM**: Revolutions per minute of the engine.
                       - **Speed**: Velocity of the car in km/h.
                       - **Throttle**: Percentage of maximum engine power used.
                   """)

# filter for user
    driver_number = st.text_input("Driver Number (e.g., 55):", value="55")
    session_key = st.text_input("Session Key (e.g., 9159):", value="9159")
    min_speed = st.number_input("Minimum Speed (km/h):", value=315)

#function fetching one
    def fetch_car_data(driver_number, session_key, min_speed):
        url = f'https://api.openf1.org/v1/car_data?driver_number={driver_number}&session_key={session_key}&speed>={min_speed}'
        try:
            response = urlopen(url)
            data = json.loads(response.read().decode('utf-8'))
            return data
        except Exception as e:
            st.error(f"Failed to fetch car data: {e}")
            return None

 # Fetch button
    if st.button("Fetch Car Data"):
        car_data = fetch_car_data(driver_number, session_key, min_speed)

        if car_data:
            st.title("F1 Car Data")
            st.markdown("### Attributes and Data Interpretation")

            df = pd.DataFrame(car_data)

            st.dataframe(
                df[['date', 'driver_number', 'speed', 'n_gear', 'rpm', 'brake', 'throttle']])
        else:
            st.write("No car data available at the moment.")


st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<footer style='text-align: center;'>Developed by Team SpeedShift for KAINOS 2024</footer>",
            unsafe_allow_html=True)

if __name__ == "__main__":
    display_car_data()
