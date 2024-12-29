import streamlit as st
import pandas as pd

# Financial data for tech companies
# Add chat functionality
search_term = st.text_input("Chat with your data:")

if search_term:
    st.write("User:", search_term)
    # Placeholder for future chat functionality
    st.write("Assistant: This is where the chat response will go")
company_data = {
    'Company': ['Palantir', 'Google', 'Amazon'],
    'Revenue (B)': [1.91, 282.84, 513.98],
    'Net Income (B)': [0.0236, 59.97, 11.32],
    'Market Cap (B)': [15.82, 1510, 1080],
    'PE Ratio': [43.2, 25.1, 95.7],
    'YoY Growth (%)': [24, 9.8, 9.1]
}

# Display company financials
st.header("Tech Companies Financial Overview")
companies_df = pd.DataFrame(company_data)
st.dataframe(companies_df)

# Visualization of key metrics
st.bar_chart(companies_df.set_index('Company')[['Revenue (B)', 'Net Income (B)']])