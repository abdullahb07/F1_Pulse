import streamlit as st
import pandas as pd
from urllib.request import urlopen
import json


#apis calling
def display_pit_data():
    st.header("F1 Pit Data")

    driver_number = st.text_input("Driver Number (e.g., 63):", value="63")
    pit_duration_max = st.number_input("Max Pit Duration (seconds):", min_value=0, value=31)

    def fetch_pit_data(driver_number, pit_duration_max):
        url = f'https://api.openf1.org/v1/pit?session_key=9158&driver_number={driver_number}&pit_duration<{pit_duration_max}'

        try:
            response = urlopen(url)
            data = json.loads(response.read().decode('utf-8'))
            return data
        except Exception as e:
            st.error(f"Failed to fetch pit data: {e}")
            return None

    if st.button("Fetch Pit Data"):
        pit_data = fetch_pit_data(driver_number, pit_duration_max)

        if pit_data:
            st.title(f"F1 Pit Data for Driver {driver_number}")
            st.markdown("### Attributes and Data Interpretation")

            df = pd.DataFrame(pit_data)

            st.write("""
                **Attributes:**
                - **date**: UTC date and time in ISO 8601 format.
                - **driver_number**: Unique number assigned to the F1 driver.
                - **lap_number**: Sequential number of the lap within the session (starts at 1).
                - **meeting_key**: Unique identifier for the meeting.
                - **pit_duration**: Time spent in the pit, from entering to leaving the pit lane, in seconds.
                - **session_key**: Unique identifier for the session.
            """)

            st.dataframe(df[['date', 'driver_number', 'lap_number', 'pit_duration']])

            st.markdown("### Insights")
            st.write("""
                This data provides insights into pit stop strategies and performance, including which drivers had the fastest pit stops.
            """)



if __name__ == "__main__":
    display_pit_data()
