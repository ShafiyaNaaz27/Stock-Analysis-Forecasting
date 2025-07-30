import streamlit as st

st.set_page_config(
    page_title="Trading App",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)
st.title("Trading Guide App :bar_chart:")

st.header("Welcome to the Trading App")
st.write("This app provides a trading guide for stocks and cryptocurrencies.")

st.image("pexels-anna-nekrashevich-6801639.jpg")

st.markdown("## We provide the following services:")

st.markdown("- Stock Information")
st.write("Through the app, you can find information about stocks, such as their prices, volumes, and other metrics.")

st.markdown("- Stock Predictions")
st.write("You can explore predicted closing prices for the next 30 days based on historical stock data and advanced forecasting models. Use this feature to make informed trading decisions.")

st.markdown("- CAPM Return")
st.write("Discover how the Capital Assest Pricing Model (CAPM) works and how it can help you calculate the expected return of different assest based on its risk and market performance.")

st.markdown("- CAPM Beta")
st.write("Calculates Beta and Expected Return for individual stocks")
