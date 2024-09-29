import streamlit as st
import pandas as pd
from urllib.request import urlopen
import json

def display_team_radio_data():
    st.header("Team Radio Data")

    def fetch_team_radio_data():
        url = 'https://api.openf1.org/v1/team_radio?session_key=9158&driver_number=11'
        try:
            response = urlopen(url)
            data = json.loads(response.read().decode('utf-8'))
            return data
        except Exception as e:
            st.error(f"Failed to fetch team radio data: {e}")
            return None

    team_radio_data = fetch_team_radio_data()

    if team_radio_data:
        st.title("F1 Team Radio Data")
        st.markdown("### Attributes and Data Interpretation")

        df = pd.DataFrame(team_radio_data)

        st.write("""
            **Attributes:**
            - **date**: UTC date and time of the radio exchange.
            - **driver_number**: Unique number assigned to an F1 driver.
            - **recording_url**: URL of the radio recording.
        """)

        st.dataframe(df[['driver_number', 'date', 'recording_url']])

        st.markdown("### Insights")
        st.write("""
            This data provides a glimpse into the communications between drivers and their teams during sessions.
        """)

