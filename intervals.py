import streamlit as st
import pandas as pd
from urllib.request import urlopen
import json

def display_intervals_data():
    st.header("Intervals Data")

#filters
    session_key = st.text_input("Session Key (e.g., 9165):", value="9165")
    driver_number = st.text_input("Driver Number (e.g., 33):", value="")
    interval_less_than = st.number_input("Interval less than (e.g., 0.005):", min_value=0.0, step=0.001, value=0.005)
    gap_to_leader_less_than = st.number_input("Gap to Leader less than (e.g., 5.0):", min_value=0.0, step=0.1)

#api
    def fetch_intervals_data(session_key, driver_number, interval, gap_to_leader):
        url = f'https://api.openf1.org/v1/intervals?session_key={session_key}&interval<{interval}'
        if driver_number:
            url += f"&driver_number={driver_number}"
        if gap_to_leader:
            url += f"&gap_to_leader<{gap_to_leader}"
        try:
            response = urlopen(url)
            data = json.loads(response.read().decode('utf-8'))  # Decode the response
            return data
        except Exception as e:
            st.error(f"Failed to fetch intervals data: {e}")
            return None

if st.button("Fetch Interval Data"):
        intervals_data = fetch_intervals_data(session_key, driver_number, interval_less_than, gap_to_leader_less_than)


        if intervals_data:
            st.title("F1 Intervals Data")
            st.markdown("### Attributes and Data Interpretation")

            df = pd.DataFrame(intervals_data)

            st.write("""
                **Attributes:**
                - **date**: The UTC date and time in ISO 8601 format.
                - **driver_number**: Unique number assigned to an F1 driver.
                - **gap_to_leader**: Time gap to the race leader in seconds (+1 LAP if lapped, or null for the race leader).
                - **interval**: Time gap to the car ahead in seconds (+1 LAP if lapped, or null for the car ahead).
                - **meeting_key**: Unique identifier for the meeting.
                - **session_key**: Unique identifier for the session.
            """)

            st.dataframe(df[['date', 'driver_number', 'gap_to_leader', 'interval', 'meeting_key', 'session_key']])

#add some info from ai**
            st.markdown("### Insights")
            st.write("""
                This data can help analyze driver performance and strategy by comparing their time gaps during the race. 
                Understanding these intervals can give insights into overtaking opportunities and pit stop strategies.
            """)
        else:
            st.write("No interval data available at the moment.")




if __name__ == "__main__":
    display_intervals_data()
