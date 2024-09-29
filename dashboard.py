import streamlit as st
st.set_page_config(page_title="F1 Pulse Dashboard", layout="wide")

import pandas as pd
import plotly.express as px
import requests
import drivers
import intervals
import locations
import meetings
import pit
import position
import race_control_data
import sessions
import stints
import team_radio_data
import weather
import car_data
import laps


st.sidebar.title("F1 Data Navigation")

# navbar categories
categories = [
    "Dashboard", "Car Data", "Drivers", "Intervals", "Laps", "Locations", "Meetings", "Pit Stops",
    "Positions", "Race Control", "Sessions", "Stints", "Team Radio", "Weather"
]

selected_category = st.sidebar.radio("Select Data to View:", categories)

st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='color: red; font-size: 3em; margin-bottom: 0;'>
        🏎️ F1 Pulse  
        </h1>
        <h2 style='color: grey; margin-top: 0;'>
        Real-Time Race Insights
        </h2>
        <p style='color: blue; font-size: 1.2em;'>
        Get the pulse of the race with real-time data and analysis!
        </p>
        <hr style='border: 1px solid #ccc; width: 50%; margin: auto;'>
    </div>
    """, unsafe_allow_html=True
)

# show selection
st.title(f"F1 Data: {selected_category}")
st.write(f"Fetching and displaying data for: {selected_category}")

# options to select if else
if selected_category == "Dashboard":
    st.write("Welcome to the F1 Pulse Dashboard!")
elif selected_category == "Car Data":
    car_data.display_car_data()  # This will call the function in car_data.py to display car data
elif selected_category == "Laps":
    laps.display_laps_data()
elif selected_category == "Intervals":
    intervals.display_intervals_data()
elif selected_category == "Drivers":
    drivers.display_drivers_data()
elif selected_category == "Locations":
    locations.display_locations_data()
elif selected_category == "Meetings":
    meetings.display_meetings_data()
elif selected_category == "Pit Stops":
    pit.display_pit_data()
elif selected_category == "Positions":
    position.display_position_data()
elif selected_category == "Race Control":
    race_control_data.display_race_control_data()
elif selected_category == "Sessions":
    sessions.display_sessions_data()
elif selected_category == "Stints":
    stints.display_stints_data()
elif selected_category == "Team Radio":
    team_radio_data.display_team_radio_data()
elif selected_category == "Weather":
    weather.display_weather_data()

# demo data years and GPs
st.sidebar.title("Race Selection")
season = st.sidebar.selectbox("Select Season", ["2023", "2022", "2021", "2020"])
race = st.sidebar.selectbox("Select Race", ["Monaco GP", "Silverstone GP", "Spa GP"])

st.sidebar.markdown("### Live Race Updates", unsafe_allow_html=True)

st.sidebar.markdown("<div style='border: 1px solid grey; padding: 10px; border-radius: 5px;'>"
                    "<strong>Driver in Lead:</strong> Lewis Hamilton<br>"
                    "<strong>Fastest Lap:</strong> Max Verstappen - 1:35:08</div>", unsafe_allow_html=True)


# demo data not from api
lap_times = {
    "Driver": ["Lewis Hamilton", "Max Verstappen", "Charles Leclerc", "Lando Norris", "Sergio Perez"],
    "Lap 1": [78.3, 79.1, 79.5, 80.2, 80.7],
    "Lap 2": [78.0, 78.9, 79.3, 80.1, 80.4],
    "Lap 3": [77.8, 78.6, 79.0, 80.0, 80.3]
           }

df_laps = pd.DataFrame(lap_times)

# demo graph of plotly
df_melted = pd.melt(df_laps, id_vars="Driver", var_name="Lap", value_name="Time")
fig = px.line(df_melted, x="Lap", y="Time", color="Driver", title="Lap Time Analysis", markers=True)


col1, col2 = st.columns(2)
with col1:
    st.subheader("Lap Time Table")
    st.write(df_laps)

with col2:
    st.subheader("Lap Time Comparison Chart")
    st.plotly_chart(fig)

# future updates
st.markdown("### Upcoming Features")
st.info("Stay tuned for real-time data integration, driver performance metrics, and much more!")


# FF
def feedback_form():
    st.header("Feedback")
    feedback = st.text_area("Please provide your feedback or suggestions:")
    if st.button("Submit"):
        # Here you can implement functionality to save the feedback
        st.success("Thank you for your feedback!")
feedback_form()


#footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<footer style='text-align: center;'>Developed by Team SpeedShift for KAINOS 2024</footer>",
            unsafe_allow_html=True)