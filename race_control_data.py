import streamlit as st
import pandas as pd
from urllib.request import urlopen
import json

def display_race_control_data():
    st.header("Race Control Data")

#fetching not available of api
    def fetch_race_control_data():
        url = 'https://api.openf1.org/v1/race_control?flag=BLACK AND WHITE&driver_number=1&date>=2023-01-01&date<2023-09-01'  # Update as needed
        try:
            response = urlopen(url)
            data = json.loads(response.read().decode('utf-8'))  # Decode the response
            return data
        except Exception as e:
            st.error(f"Failed to fetch race control data: {e}")
            return None

    race_control_data = fetch_race_control_data()


    if race_control_data:
        st.title("F1 Race Control Data")
        st.markdown("### Attributes and Data Interpretation")


        df = pd.DataFrame(race_control_data)

        st.write("""
            **Attributes:**
            - **category**: The category of the event (e.g., Flag, SafetyCar).
            - **date**: UTC date and time in ISO 8601 format.
            - **driver_number**: Unique number assigned to the F1 driver.
            - **flag**: Type of flag displayed (e.g., GREEN, YELLOW).
            - **lap_number**: Sequential number of the lap within the session.
            - **meeting_key**: Unique identifier for the meeting.
            - **message**: Description of the event or action.
            - **scope**: The scope of the event (e.g., Track, Driver).
            - **sector**: Segment of the track where the event occurred.
            - **session_key**: Unique identifier for the session.
        """)

        st.dataframe(df[['date', 'driver_number', 'flag', 'lap_number', 'message']])


        st.markdown("### Insights")
        st.write("""
            This data provides information about racing incidents, flags, and safety car events during the race.
        """)

