import streamlit as st
import pandas as pd
from urllib.request import urlopen
import json

def display_position_data():
    st.header("Driver Position Data")

    def fetch_position_data():
        url = 'https://api.openf1.org/v1/position?meeting_key=1217&driver_number=40&position<=3'
        try:
            response = urlopen(url)
            data = json.loads(response.read().decode('utf-8'))
            return data
        except Exception as e:
            st.error(f"Failed to fetch position data: {e}")
            return None

    position_data = fetch_position_data()


    if position_data:
        st.title("F1 Driver Position Data")
        st.markdown("### Attributes and Data Interpretation")


        df = pd.DataFrame(position_data)

        st.write("""
            **Attributes:**
            - **date**: UTC date and time in ISO 8601 format.
            - **driver_number**: Unique number assigned to the F1 driver.
            - **meeting_key**: Unique identifier for the meeting.
            - **position**: Current position of the driver (starts at 1).
            - **session_key**: Unique identifier for the session.
        """)

        st.dataframe(df[['date', 'driver_number', 'position']])


        st.markdown("### Insights")
        st.write("""
            This data provides information about driver positions throughout a session,
            including initial placement and subsequent changes.
        """)

