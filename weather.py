import streamlit as st
import pandas as pd
from urllib.request import urlopen
import json

def display_weather_data():
    st.header("Weather Data")

    def fetch_weather_data():
        url = 'https://api.openf1.org/v1/weather?meeting_key=1208&wind_direction>=130&track_temperature>=52'
        try:
            response = urlopen(url)
            data = json.loads(response.read().decode('utf-8'))
            return data
        except Exception as e:
            st.error(f"Failed to fetch weather data: {e}")
            return None

    weather_data = fetch_weather_data()

    if weather_data:
        st.title("F1 Weather Data")
        st.markdown("### Attributes and Data Interpretation")

        df = pd.DataFrame(weather_data)

        st.write("""
            **Attributes:**
            - **date**: UTC date and time of the weather report.
            - **air_temperature**: Air temperature (°C).
            - **track_temperature**: Track temperature (°C).
            - **humidity**: Relative humidity (%).
            - **wind_direction**: Wind direction (°).
            - **wind_speed**: Wind speed (m/s).
            - **pressure**: Air pressure (mbar).
            - **rainfall**: Amount of rainfall.
        """)

        st.dataframe(df[['date', 'air_temperature', 'track_temperature', 'humidity', 'wind_direction', 'wind_speed', 'pressure', 'rainfall']])

        st.markdown("### Insights")
        st.write("""
            Weather conditions can significantly affect race strategies and driver performance.
        """)


