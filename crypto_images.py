import streamlit as st 

def parse_image(selected_crypto_currency): 
    if selected_crypto_currency == 'bitcoin':
        mystyle = '''
              <div style="text-align: center"> 
              <img src="https://s2.coinmarketcap.com/static/img/coins/64x64/1.png"
              alt="Italian Trulli"> 
              </div>
              '''
        return st.markdown(mystyle, unsafe_allow_html=True)

    if selected_crypto_currency == 'dogecoin':
        mystyle = '''
              <div style="text-align: center"> 
              <img src="https://s2.coinmarketcap.com/static/img/coins/64x64/74.png"
              alt="Italian Trulli"> 
              </div>
              '''
        return st.markdown(mystyle, unsafe_allow_html=True)

    if selected_crypto_currency == 'ethereum':
        mystyle = '''
              <div style="text-align: center"> 
              <img src="https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png"
              alt="Italian Trulli"> 
              </div>
              '''
        return st.markdown(mystyle, unsafe_allow_html=True)

    if selected_crypto_currency == 'binancecoin':
        mystyle = '''
              <div style="text-align: center"> 
              <img src="https://s2.coinmarketcap.com/static/img/coins/64x64/1839.png"
              alt="Italian Trulli"> 
              </div>
              '''
        return st.markdown(mystyle, unsafe_allow_html=True)

    if selected_crypto_currency == 'chainlink':
        mystyle = '''
              <div style="text-align: center"> 
              <img src="https://s2.coinmarketcap.com/static/img/coins/64x64/1975.png"
              alt="Italian Trulli"> 
              </div>
              '''
        return st.markdown(mystyle, unsafe_allow_html=True)

    if selected_crypto_currency == 'cardano':
        mystyle = '''
              <div style="text-align: center"> 
              <img src="https://s2.coinmarketcap.com/static/img/coins/64x64/2010.png"
              alt="Italian Trulli"> 
              </div>
              '''
        return st.markdown(mystyle, unsafe_allow_html=True)

    if selected_crypto_currency == 'litecoin':
        mystyle = '''
              <div style="text-align: center"> 
              <img src="https://s2.coinmarketcap.com/static/img/coins/64x64/2.png"
              alt="Italian Trulli"> 
              </div>
              '''
        return st.markdown(mystyle, unsafe_allow_html=True)

    if selected_crypto_currency == 'solana':
        mystyle = '''
              <div style="text-align: center"> 
              <img src="https://s2.coinmarketcap.com/static/img/coins/64x64/5426.png"
              alt="Italian Trulli"> 
              </div>
              '''
        return st.markdown(mystyle, unsafe_allow_html=True)

    if selected_crypto_currency == 'ripple':
        mystyle = '''
              <div style="text-align: center"> 
              <img src="https://s2.coinmarketcap.com/static/img/coins/64x64/52.png"
              alt="Italian Trulli"> 
              </div>
              '''
        return st.markdown(mystyle, unsafe_allow_html=True)

    return