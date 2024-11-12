import streamlit as st
from dotenv import load_dotenv
import os
from ui.dashboard import display_dashboard

load_dotenv()
st.set_page_config(
    page_title="AI-Powered Data Retrieval Agent",
    page_icon="🔍",
    layout="centered",
)

def main():
    st.sidebar.title("Navigation")
    st.sidebar.markdown("Use the sidebar to upload data, enter queries, and retrieve information.")
    display_dashboard()

if __name__ == "__main__":
    main()
