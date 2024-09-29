import streamlit as st
import pandas as pd
from urllib.request import urlopen
import json

def display_stints_data():
    st.header("F1 Stint Data")

    driver_number = st.text_input("Driver Number (e.g., 63):", value="63")
    tyre_age_min = st.number_input("Minimum Tyre Age at Start (laps):", min_value=0, value=3)

    def fetch_stints_data(driver_number, tyre_age_min):
        url = f'https://api.openf1.org/v1/stints?session_key=9165&driver_number={driver_number}&tyre_age_at_start>={tyre_age_min}'
        try:
            response = urlopen(url)
            data = json.loads(response.read().decode('utf-8'))
            return data
        except Exception as e:
            st.error(f"Failed to fetch stints data: {e}")
            return None

    if st.button("Fetch Stint Data"):
        stints_data = fetch_stints_data(driver_number, tyre_age_min)

        if stints_data:
            st.title(f"F1 Stint Data for Driver {driver_number}")
            st.markdown("### Attributes and Data Interpretation")

            df = pd.DataFrame(stints_data)

          #att
            st.write("""
                **Attributes:**
                - **compound**: Type of tyre compound used (SOFT, MEDIUM, HARD, ...).
                - **driver_number**: Unique number assigned to an F1 driver.
                - **lap_start**: Initial lap number of the stint.
                - **lap_end**: Last completed lap number of the stint.
                - **stint_number**: Sequential number of the stint in the session.
                - **tyre_age_at_start**: Age of the tyres at the start of the stint in laps.
            """)


            st.dataframe(df[['driver_number', 'stint_number', 'compound', 'lap_start', 'lap_end', 'tyre_age_at_start']])


            st.markdown("### Insights")
            st.write("""
                This data provides insights into the tyre strategy employed by drivers during their stints.
            """)


if __name__ == "__main__":
    display_stints_data()
