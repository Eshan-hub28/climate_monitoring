import streamlit as st
import random
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Initial data storage
if 'data' not in st.session_state:
    st.session_state.data = {
        "timestamp": [],
        "temperature": [],
        "humidity": [],
        "air_quality": []
    }

def collect_data():
    """Simulate data collection from sensors."""
    timestamp = datetime.now()
    temperature = random.uniform(-10, 40)  # Simulated temperature
    humidity = random.uniform(0, 100)       # Simulated humidity
    air_quality = random.randint(0, 300)    # Simulated air quality index

    # Append data to the lists
    st.session_state.data["timestamp"].append(timestamp)
    st.session_state.data["temperature"].append(temperature)
    st.session_state.data["humidity"].append(humidity)
    st.session_state.data["air_quality"].append(air_quality)

    st.success(f"Data Collected: {timestamp}, Temp: {temperature:.2f}°C, Humidity: {humidity:.2f}%, AQI: {air_quality}")

def analyze_data():
    """Analyze data and check for alerts."""
    last_temp = st.session_state.data["temperature"][-1]
    last_humidity = st.session_state.data["humidity"][-1]
    last_aqi = st.session_state.data["air_quality"][-1]

    alerts = []

    if last_temp < 0:
        alerts.append("Alert: Temperature is below freezing!")
    elif last_temp > 35:
        alerts.append("Alert: Temperature is above normal levels!")

    if last_humidity < 30:
        alerts.append("Alert: Humidity is too low!")
    elif last_humidity > 70:
        alerts.append("Alert: Humidity is too high!")

    if last_aqi > 150:
        alerts.append("Alert: Air quality is unhealthy!")

    return alerts

def visualize_data():
    """Visualize the collected data."""
    df = pd.DataFrame(st.session_state.data)

    plt.figure(figsize=(12, 8))

    plt.subplot(3, 1, 1)
    plt.plot(df["timestamp"], df["temperature"], label="Temperature (°C)", color='r')
    plt.title('Temperature over Time')
    plt.xlabel('Timestamp')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)

    plt.subplot(3, 1, 2)
    plt.plot(df["timestamp"], df["humidity"], label="Humidity (%)", color='b')
    plt.title('Humidity over Time')
    plt.xlabel('Timestamp')
    plt.ylabel('Humidity (%)')
    plt.xticks(rotation=45)

    plt.subplot(3, 1, 3)
    plt.plot(df["timestamp"], df["air_quality"], label="Air Quality Index", color='g')
    plt.title('Air Quality Index over Time')
    plt.xlabel('Timestamp')
    plt.ylabel('Air Quality Index')
    plt.xticks(rotation=45)

    plt.tight_layout()
    st.pyplot(plt)

# Streamlit UI
st.title("Climate Resilience Monitoring Tool")

if st.button("Collect Data"):
    collect_data()
    alerts = analyze_data()
    if alerts:
        for alert in alerts:
            st.warning(alert)
    else:
        st.success("No alerts! All readings are normal.")

if st.button("Visualize Data"):
    if not st.session_state.data["timestamp"]:
        st.warning("No data to visualize. Please collect data first.")
    else:
        visualize_data()
