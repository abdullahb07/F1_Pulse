import streamlit as st
import pandas as pd
from urllib.request import urlopen
import json


def display_locations_data():
    st.header("Car Locations Data")

#api
    session_key = st.text_input("Session Key (e.g., 9161):", value="9161")
    driver_number = st.text_input("Driver Number (e.g., 81):", value="")

#sliders for location
    x_range = st.slider("X-coordinate range:", min_value=-1000.0, max_value=1000.0, value=(-500.0, 500.0), step=10.0)
    y_range = st.slider("Y-coordinate range:", min_value=-1000.0, max_value=1000.0, value=(-500.0, 500.0), step=10.0)
    z_range = st.slider("Z-coordinate range:", min_value=-100.0, max_value=100.0, value=(-50.0, 50.0), step=1.0)

#api
    def fetch_location_data(session_key, driver_number, x_min, x_max, y_min, y_max, z_min, z_max):
        url = f'https://api.openf1.org/v1/location?session_key={session_key}'
        if driver_number:
            url += f"&driver_number={driver_number}"
        url += f"&x>={x_min}&x<={x_max}&y>={y_min}&y<={y_max}&z>={z_min}&z<={z_max}"
        try:
            response = urlopen(url)
            data = json.loads(response.read().decode('utf-8'))  # Decode the response
            return data
        except Exception as e:
            st.error(f"Failed to fetch location data: {e}")
            return None

    if st.button("Fetch Car Location Data"):
        location_data = fetch_location_data(session_key, driver_number, *x_range, *y_range, *z_range)

        if location_data:
            st.title("F1 Car Locations Data")
            st.markdown("### Attributes and Data Interpretation")

            df = pd.DataFrame(location_data)

            st.write("""
                **Attributes:**
                - **date**: The UTC date and time in ISO 8601 format.
                - **driver_number**: Unique number assigned to an F1 driver.
                - **meeting_key**: Unique identifier for the meeting.
                - **session_key**: Unique identifier for the session.
                - **x**: 'x' value in a 3D Cartesian coordinate system representing the current approximate location of the car on the track.
                - **y**: 'y' value in a 3D Cartesian coordinate system representing the current approximate location of the car on the track.
                - **z**: 'z' value in a 3D Cartesian coordinate system representing the current approximate location of the car on the track.
            """)

            st.dataframe(df[['date', 'driver_number', 'meeting_key', 'session_key', 'x', 'y', 'z']])

        else:
            st.write("No location data available at the moment.")


if __name__ == "__main__":
    display_locations_data()
