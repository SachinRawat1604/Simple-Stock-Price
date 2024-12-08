import yfinance as yf
import streamlit as st 
import pandas as pd

st.write("""
# Simple stock Price APP

Shown are the stock closing price and volume of Google!
          
""")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(start='2010-5-31', end='2024-12-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
