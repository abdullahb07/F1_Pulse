import streamlit as st
import pandas as pd
from urllib.request import urlopen
import json

def display_meetings_data():
    st.header("F1 Meetings Data")


    year = st.text_input("Year (e.g., 2023):", value="2023")
    country_name = st.text_input("Country Name (e.g., Singapore):", value="Singapore")

#apis
    def fetch_meetings_data(year, country_name):
        url = f'https://api.openf1.org/v1/meetings?year={year}&country_name={country_name}'  # Dynamic URL
        try:
            response = urlopen(url)
            data = json.loads(response.read().decode('utf-8'))  # Decode the response
            return data
        except Exception as e:
            st.error(f"Failed to fetch meetings data: {e}")
            return None


    if st.button("Fetch Meetings Data"):
        meetings_data = fetch_meetings_data(year, country_name)

        if meetings_data:
            st.title(f"F1 Meetings Data for {country_name} ({year})")
            st.markdown("### Attributes and Data Interpretation")

            df = pd.DataFrame(meetings_data)

            st.write("""
                **Attributes:**
                - **circuit_key**: Unique identifier for the circuit.
                - **circuit_short_name**: Short name of the circuit.
                - **country_name**: Full name of the country.
                - **date_start**: Starting date and time in UTC.
                - **meeting_key**: Unique identifier for the meeting.
                - **meeting_name**: Name of the meeting.
                - **meeting_official_name**: Official name of the meeting.
                - **location**: City or location of the event.
                - **year**: Year of the event.
            """)

            st.dataframe(df[['meeting_name', 'meeting_official_name', 'circuit_short_name', 'location', 'date_start', 'year']])

#ai text add
            st.markdown("### Insights")
            st.write("""
                This data provides key details about F1 events such as Grand Prix or testing weekends.
                     """)



if __name__ == "__main__":
    display_meetings_data()
