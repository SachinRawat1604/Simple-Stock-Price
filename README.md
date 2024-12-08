# Simple Stock Price App

This is a **Streamlit** application that displays the historical closing prices and trading volume of Google stock using the **Yahoo Finance** API.

## Features

- Visualizes the historical **closing price** of Google stock in a line chart.
- Visualizes the historical **trading volume** of Google stock in a line chart.
- Uses **yfinance** to fetch stock data and **Streamlit** for an interactive web interface.

## Prerequisites

Make sure you have the following installed:

- Python 3.8 or later
- pip (Python package manager)

## Installation

1. Clone the repository or download the script.

2. Install the required Python libraries:
   ```bash
   pip install yfinance streamlit pandas
Run the application:
  streamlit run app.py
  Replace app.py with the filename if you saved the script under a different name.

Usage:
  After running the app, open the provided local URL in your web browser (e.g., http://localhost:8501).

The app will display:
  A line chart of Google's historical closing prices.
  A line chart of Google's historical trading volume.

## Code Overview
1. Libraries Used:
  yfinance: Fetches historical stock data from Yahoo Finance.
  Streamlit: Creates the interactive web app.
  Pandas: Handles data manipulation and analysis.

2. Key Components:
  Ticker Symbol: Predefined as 'GOOGL' (Google stock).
  Date Range: Historical data is fetched from May 31, 2010, to December 31, 2024.

3. Charts:
  Closing Price: Displays the closing prices over time.
  Volume: Displays the trading volume over time.

License
This project is open-source and available under the MIT License.# Simple-Stock-Price
