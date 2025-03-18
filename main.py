import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

Time_Zones = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Asia/Dubai",
    "Africa/Cairo",
    "Europe/Paris",
    "Asia/Shanghai",
    "America/Chicago",
    "America/Toronto",
    "Asia/Singapore",
    "Pacific/Auckland",
    "America/Sao_Paulo",
    "Asia/Kolkata",
    "Europe/Berlin",
    "Africa/Johannesburg"
]

st.title("Time Zone App")

selected_timezone = st.multiselect("Select Timezones", Time_Zones, default=["UTC", "Asia/Karachi"])

st.success("Selected Time")
for tz in selected_timezone:
    current_Time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.write(f"**{tz}**: {current_Time}")

st.subheader("Convert Time Between TimeZones")

current_time = st.time_input("Current Time", value=datetime.now().time())

from_timezone = st.selectbox("From TimeZone", Time_Zones, index=0)
to_timezones = st.selectbox("TO TimeZone", Time_Zones, index=1)

if st.button("Convert Time"):
    # Get the current date in the 'from' timezone
    from_date = datetime.now(ZoneInfo(from_timezone)).date()
    # Combine with the input time and set the timezone
    dt = datetime.combine(from_date, current_time).replace(tzinfo=ZoneInfo(from_timezone))
    # Convert to the target timezone
    converted_time = dt.astimezone(ZoneInfo(to_timezones)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.success(f"Converted Time in {to_timezones}: {converted_time}")