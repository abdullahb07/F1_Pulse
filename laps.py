import streamlit as st
import pandas as pd
from urllib.request import urlopen
import json

def display_laps_data():
    st.header("Lap Data")

#filetrs
    session_key = st.text_input("Session Key (e.g., 9161):", value="9161")
    driver_number = st.text_input("Driver Number (e.g., 63):", value="")
    lap_number = st.number_input("Lap Number (e.g., 8):", min_value=1, step=1)
    lap_duration_greater_than = st.number_input("Lap Duration greater than (seconds):", min_value=0.0, step=1.0)
    lap_duration_less_than = st.number_input("Lap Duration less than (seconds):", min_value=0.0, step=1.0)


    def fetch_lap_data(session_key, driver_number, lap_number, duration_min, duration_max):
        url = f'https://api.openf1.org/v1/laps?session_key={session_key}&lap_number={lap_number}'
        if driver_number:
            url += f"&driver_number={driver_number}"
        if duration_min > 0:
            url += f"&lap_duration>={duration_min}"
        if duration_max > 0:
            url += f"&lap_duration<={duration_max}"
        try:
            response = urlopen(url)
            data = json.loads(response.read().decode('utf-8'))
            return data
        except Exception as e:
            st.error(f"Failed to fetch lap data: {e}")
            return None

    if st.button("Fetch Lap Data"):
        lap_data = fetch_lap_data(session_key, driver_number, lap_number, lap_duration_greater_than, lap_duration_less_than)

        if lap_data:
            st.title("F1 Lap Data")
            st.markdown("### Attributes and Data Interpretation")

            df = pd.DataFrame(lap_data)

            st.write("""
                **Attributes:**
                - **date_start**: The UTC starting date and time, in ISO 8601 format.
                - **driver_number**: Unique number assigned to an F1 driver.
                - **duration_sector_1**: Time taken, in seconds, to complete the first sector.
                - **duration_sector_2**: Time taken, in seconds, to complete the second sector.
                - **duration_sector_3**: Time taken, in seconds, to complete the third sector.
                - **i1_speed**: Speed of the car, in km/h, at the first intermediate point.
                - **i2_speed**: Speed of the car, in km/h, at the second intermediate point.
                - **is_pit_out_lap**: Indicates whether the lap is an "out lap" from the pit.
                - **lap_duration**: Total time taken, in seconds, to complete the lap.
                - **lap_number**: Sequential number of the lap within the session.
                - **meeting_key**: Unique identifier for the meeting.
                - **segments_sector_1, 2, 3**: List of values representing "mini-sectors".
                - **session_key**: Unique identifier for the session.
                - **st_speed**: Speed of the car, in km/h, at the speed trap.
            """)

            st.dataframe(df)

            st.markdown("### Segment Values Interpretation")
            st.write("""
            | Segment Value | Meaning                      |
            |---------------|-------------------------------|
            | 0             | Not available                 |
            | 2048          | Yellow sector                 |
            | 2049          | Green sector                  |
            | 2050          | ?                             |
            | 2051          | Purple sector                 |
            | 2052          | ?                             |
            | 2064          | Pitlane                       |
            | 2068          | ?                             |
            """)
        else:
            st.write("No lap data available at the moment.")


if __name__ == "__main__":
    display_laps_data()
