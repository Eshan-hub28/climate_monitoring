# Climate Monitoring Tool using Python and Streamlit

## Overview

The Climate Monitoring Tool is a web application developed using Python and Streamlit, designed to track and analyze climate data in real-time. It retrieves data such as temperature, humidity, and atmospheric pressure from external APIs (e.g., OpenWeatherMap) or IoT sensors, allowing users to visualize climate trends, set alerts, and export data for further analysis.

## Features
- Real-time Monitoring: Fetches and displays real-time climate data.

- Historical Data Visualization: View climate trends over time with dynamic graphs and charts.

- Alerts: Configure alerts for specific climate thresholds.

- Data Export: Download climate data as CSV for offline analysis.

- User-friendly Interface: Simple and interactive Streamlit-based dashboard.

## Technologies Used

- Python: Core programming language.

- Streamlit: Framework for building interactive web applications.

- APIs: Integrates with public APIs like OpenWeatherMap for data retrieval.

- Pandas & Matplotlib/Plotly: For data processing and visualization.

- NumPy: For numerical data handling.

## Installation
Prerequisites
Python 3.x
Streamlit
API key from OpenWeatherMap (or another weather data provider)

### Setup Instructions

#### Clone the repository:

```bash
git clone https://github.com/yourusername/climate-monitoring-tool.git
cd climate-monitoring-tool
```
## Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate  # For Linux/MacOS
```
### or
```
env\Scripts\activate  # For Windows
```

### Install the required dependencies:

```bash
pip install -r requirements.txt
```
### Add your API key:

Obtain an API key from OpenWeatherMap or any other climate data provider.
Create a .env file in the root directory and add the following line:
makefile
```
API_KEY=your_openweathermap_api_key
Run the Streamlit app
```

```bash
streamlit run app.py
Access the app: Open your browser and navigate to http://localhost:8501 to start using the tool.
```

## Usage
- Real-time Data: On the dashboard, view real-time temperature, humidity, and atmospheric pressure from the chosen location.

- Historical Data: View past trends by selecting date ranges for historical climate data.

- Alerts: Set threshold values for climate parameters (e.g., high temperature) to receive notifications when those conditions are met.

- Data Export: Click on the export button to download climate data as a CSV file.
Screenshots

## Customization

You can modify the following:

- API Source: To use different weather data providers, adjust the API endpoint in app.py.

- Graph Settings: Customize visualizations by tweaking the matplotlib or plotly configuration in the code.

- Alerts: Modify or extend the alert system to trigger different actions when thresholds are met.


### Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request with improvements, bug fixes, or new features.
