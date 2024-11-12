import streamlit as st

def load_css():
     st.markdown(
        """
        <style>
        /* Main Container Styling */
        .css-18e3th9 {
            padding-top: 4rem;
            padding-bottom: 4rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }

        /* Button Styling */
        .stButton>button {
            color: white;
            background-color: #1F75FE; /* Similar to the blue in the UI design */
            transition: background-color 0.3s ease;
            border-radius: 10px;
        }
        .stButton>button:hover {
            background-color: #174BA8; /* Slightly darker blue for hover effect */
        }

        /* Background Color for Light Mode */
        .light-mode {
            background-color: #F4F5F7;
            color: #333333;
        }

        /* Background Color for Dark Mode */
        .dark-mode {
            background-color: #1E1E2E;
            color: #EAEAEA;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

