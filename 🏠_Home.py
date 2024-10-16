import streamlit as st
from dotenv import load_dotenv
from src.logger.base import BaseLogger

# Load environment variables
load_dotenv()
logger = BaseLogger()

# Set up Streamlit interface
st.header("🤖 Smart Data Chat Application")
st.write(
        "### Welcome to our data analysis tool. This tool can assist your daily data analysis tasks. Please enjoy!"
    )
#myenv\Scripts\activate
