import streamlit as st
import pandas as pd
from urllib.request import urlopen
import json


def display_sessions_data():
    st.header("Sessions Data")

#filters
    session_key = st.text_input("Session Key (e.g., 9158):", value="9158")
    meeting_key = st.text_input("Meeting Key (e.g., 1219):", value="")
    date_start = st.date_input("Start Date:", value=pd.to_datetime("2023-09-01"))
    date_end = st.date_input("End Date:", value=pd.to_datetime("2023-09-30"))

    def fetch_sessions_data(session_key, meeting_key, date_start, date_end):
        url = f'https://api.openf1.org/v1/sessions?session_key={session_key}'

        if meeting_key:
            url += f"&meeting_key={meeting_key}"
        if date_start:
            url += f"&date_start={date_start.strftime('%Y-%m-%d')}"
        if date_end:
            url += f"&date_end={date_end.strftime('%Y-%m-%d')}"

        try:
            response = urlopen(url)
            data = json.loads(response.read().decode('utf-8'))
            return data
        except Exception as e:
            st.error(f"Failed to fetch session data: {e}")
            return None


    if st.button("Fetch Session Data"):
        session_data = fetch_sessions_data(session_key, meeting_key, date_start, date_end)


        if session_data:
            st.title("F1 Session Data")
            st.markdown("### Attributes and Data Interpretation")


            df = pd.DataFrame(session_data)


            st.write("""
                **Attributes:**
                - **date**: The date of the session.
                - **meeting_key**: Unique identifier for the meeting.
                - **session_key**: Unique identifier for the session.
                - **session_name**: Name of the session (e.g., Practice, Qualifying).
                - **session_type**: Type of the session (e.g., Race, Practice).
                - **track**: Name of the track where the session takes place.
                - **weather**: Weather conditions during the session.
            """)


            st.dataframe(df[['date', 'meeting_key', 'session_key', 'session_name', 'session_type', 'track', 'weather']])
        else:
            st.write("No session data available at the moment.")



if __name__ == "__main__":
    display_sessions_data()
