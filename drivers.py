import streamlit as st
import pandas as pd
from urllib.request import urlopen
import json

def display_drivers_data():
    st.header("Drivers Data")

#filters
    #
    driver_number = st.text_input("Driver Number (e.g., 1):", value="1")
    session_key = st.text_input("Session Key (e.g., 9158):", value="9158")
    team_name = st.text_input("Team Name (e.g., Ferrari):", value="")
    country_code = st.text_input("Country Code (e.g., ITA):", value="")
    meeting_key = st.text_input("Meeting Key (e.g., 1219):", value="")

    def fetch_driver_data(driver_number, session_key, team_name, country_code, meeting_key):
        url = f'https://api.openf1.org/v1/drivers?driver_number={driver_number}&session_key={session_key}'

        if team_name:
            url += f"&team_name={team_name}"
        if country_code:
            url += f"&country_code={country_code}"
        if meeting_key:
            url += f"&meeting_key={meeting_key}"

        try:
            response = urlopen(url)
            data = json.loads(response.read().decode('utf-8'))  # Decode the response
            return data
        except Exception as e:
            st.error(f"Failed to fetch driver data: {e}")
            return None

    if st.button("Fetch Driver Data"):
        driver_data = fetch_driver_data(driver_number, session_key, team_name, country_code, meeting_key)

        if driver_data:
            st.title("F1 Driver Data")
            st.markdown("### Attributes and Data Interpretation")

            df = pd.DataFrame(driver_data)



            for index, row in df.iterrows():
                st.image(row['headshot_url'], width=150)
                st.write(f"**Full Name:** {row['full_name']}")
                st.write(f"**Team Name:** {row['team_name']}")
                st.write(f"**Country Code:** {row['country_code']}")
                st.write(f"**Driver Number:** {row['driver_number']}")
                st.write(f"**Acronym:** {row['name_acronym']}")
                st.write(f"**Meeting Key:** {row['meeting_key']}")
                st.write(f"**Team Colour:** {row['team_colour']}")
                st.write("---")
        else:
            st.write("No driver data available at the moment.")

if __name__ == "__main__":
    display_drivers_data()
