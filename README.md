# Time Zone App

# Overview
This Streamlit-based application allows you to view the current time across multiple time zones and also convert a specific time from one time zone to another.

# Features
Multiple Time Zone Display:
Select multiple time zones from a predefined list to see the current time in each.

# Time Zone Converter:
Convert a given time from a source time zone to a destination time zone.

# Real-Time Information:
The app displays the current time using the system's time and updates based on your selections.

# Technologies Used
Python

Streamlit

datetime module

zoneinfo module

# Installation

# Install Python:
Ensure that Python is installed on your system.

# Install Streamlit:
Install Streamlit using pip:

bash
Copy
Edit
pip install streamlit
Download the Code:
Save the provided code into a file (e.g., app.py).

# How to Run
Open your terminal or command prompt and run the following command:

bash
Copy
Edit
streamlit run app.py
This command will launch the app in your default web browser.

# Usage
Viewing Current Time in Multiple Time Zones:

Use the multi-select widget to select the time zones you wish to see (e.g., UTC, Asia/Karachi, etc.).

The app displays the current time for each selected time zone.

Converting Time Between Time Zones:

Use the time input widget to choose a time.

Select the source time zone using the "From TimeZone" dropdown.

Select the destination time zone using the "TO TimeZone" dropdown.

Click the "Convert Time" button to see the time converted into the target time zone.

# Customization
To modify the available time zones, update the Time_Zones list in the code.

Further styling or functionality can be added by editing the script as needed.

# License
This project is open-source and available under the MIT License.

# Acknowledgements
Built with Streamlit.

Uses Python's built-in datetime and zoneinfo modules for handling date and time operations.

