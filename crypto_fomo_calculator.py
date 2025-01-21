import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta, timezone
import time

# Cache setup: store data and expiration time
CACHE_EXPIRY = 5 * 60  # 5 minutes in seconds
cache_timestamp = None
cached_crypto_price = {}

# Function to get crypto price with caching
def get_cached_crypto_price(symbol):
    global cache_timestamp, cached_crypto_price
    
    current_time = time.time()

    # If cache is expired or data is not available, fetch new data
    if cache_timestamp is None or current_time - cache_timestamp > CACHE_EXPIRY or symbol not in cached_crypto_price:
        crypto_data = yf.Ticker(symbol).history(period="1d")
        cached_crypto_price[symbol] = crypto_data['Close'].iloc[-1] if not crypto_data.empty else None
        cache_timestamp = current_time

    return cached_crypto_price.get(symbol, None)

# Write greeting message/header
st.markdown('''
    # Crypto FOMO Calculator
''')

st.image('./Images/cryptocurrencies.png', use_column_width=True)

st.markdown('''
    ##### Steps to calculate the amount you might have gained by investing in crypto at an earlier date.

    Select a Crypto Currency you wish you would have bought
    Select the Date you wish you would have bought the selected crypto currency
    Select the Currency type of your choice
    Select Amount you wish you would have invested
''')

st.write('---')

# Select cryptocurrency
st.sidebar.write('## Choose Crypto Currency')
selected_crypto_currency = st.sidebar.radio('Select Crypto Currency', ['BTC-USD', 'DOGE-USD', 'ETH-USD', 'BNB-USD', 'LINK-USD', 'ADA-USD', 'LTC-USD', 'SOL-USD', 'XRP-USD'])
st.sidebar.write('You have selected', selected_crypto_currency)

# Date the user wishes they purchased selected crypto
st.sidebar.write('## Choose Date and Amount')

today = datetime.now(timezone.utc).date()
previous_day = today - timedelta(days=1)

selected_historical_date = st.sidebar.date_input("Date: ", value=previous_day, min_value=datetime(2015, 1, 1).date(), max_value=previous_day)
st.sidebar.write('You have selected', selected_historical_date)

# Amount you wish you would have invested
selected_amount = st.sidebar.number_input("USD Amount: ", min_value=1, max_value=999999999)

# Load Data
crypto_current = get_cached_crypto_price(selected_crypto_currency)

# Reformat Historical Date for next function
selected_historical_date_reformat = selected_historical_date.strftime("%Y-%m-%d")
selected_historical_date_datetime = datetime.strptime(selected_historical_date_reformat, "%Y-%m-%d")

# Try to fetch historical price for the selected date
try:
    historical_data = yf.download(selected_crypto_currency, start=selected_historical_date_reformat, end=selected_historical_date_reformat)
    if historical_data.empty:
        raise ValueError("No data found for the selected date.")
    selected_crypto_currency_historic = historical_data['Close'].iloc[0]
except Exception as e:
    # If no data is found for the selected date, fetch the closest available date
    st.write(f"Error fetching historical data for {selected_historical_date_reformat}: {e}")
    st.write("Fetching the most recent available data...")
    historical_data = yf.download(selected_crypto_currency, period="5d")  # Fetch the last 5 days
    selected_crypto_currency_historic = historical_data['Close'].iloc[-1]  # Take the last available price

# Display Results - Historical Value
st.write('''# Results''')

# Display image of selected crypto-currency (handle custom images or use a default image)
try:
    from crypto_images import parse_image
    parse_image(selected_crypto_currency)
except ImportError:
    st.image('default_image.png')  # Replace with a default image if parse_image isn't available

mystyle = '''
          <div style="text-align: left"> <p> <font size = "4"> <b><u>Historical Analysis</u></b> </font> </p> </div>
          '''
st.markdown(mystyle, unsafe_allow_html=True)

if selected_crypto_currency_historic == 0:
    st.write("You would have originally bought: 0", selected_crypto_currency)
else:
    coins_bought = round((selected_amount / selected_crypto_currency_historic), 5)
    st.write("You would have originally bought: ", coins_bought, selected_crypto_currency)

st.write("At a price of $", selected_crypto_currency_historic, ' per', selected_crypto_currency)

# Display Results - Present Value
st.write('\n')
mystyle = '''
          <div style="text-align: left"> <p> <font size = "4"> <b><u>Present Effects</u></b> </font> </p> </div>
          '''
st.markdown(mystyle, unsafe_allow_html=True)

# Calculate the total number of coins based on the historical price
if selected_crypto_currency_historic == 0:
    total_coins = 0
else:
    total_coins = coins_bought

# Present value based on the current price
current_selected_currency_type = total_coins * crypto_current

# Calculate percentage change
perc_change = (current_selected_currency_type - selected_amount) / (selected_amount) * 100
selected_currency_type_diff = current_selected_currency_type - selected_amount

st.write("That is currently worth: $", round(current_selected_currency_type, 2))
st.write("Which is a percentage change of ", round(perc_change, 2), "%")

# Displaying if the user broke even or missed out
if selected_currency_type_diff == 0:
    st.write('''# You Broke Even''')
elif selected_currency_type_diff < 0:
    st.write('''# You Would Have Lost''')
else:
    st.write('''# You Missed Out On''')
st.write('$', abs(round(selected_currency_type_diff, 2)), "!!!")

# Fetch historical prices for chart
historical_prices = yf.download(selected_crypto_currency, start=selected_historical_date_reformat, end=today.strftime("%Y-%m-%d"))

# Prepare data for charting
dates = historical_prices.index
prices = historical_prices['Close']

df = pd.DataFrame({"Prices": prices, "Dates": dates})
df['Dates'] = pd.to_datetime(df['Dates'])

st.area_chart(df.rename(columns={"Dates": "index"}).set_index("index"))

# Add reference to Yahoo Finance
mystyle = '''
          <div style="text-align: center"> <b>Powered by Yahoo Finance API</b> </div>
          '''
st.markdown(mystyle, unsafe_allow_html=True)
st.write('---')
