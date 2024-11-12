import streamlit as st
from api.google_sheets import connect_to_google_sheet
from api.llm_api import extract_info_with_llm
from api.search_api import perform_web_search
import pandas as pd

def display_dashboard():
    st.title("AI-Powered Data Retrieval Agent")
    st.write("An automated tool to retrieve specific data from the web using LLMs.")

    # Instructions accordion
    with st.expander("How to Use This Application"):
        st.subheader("Instructions")
        
        st.write("**Data Source Selection:** Choose between uploading a CSV file or connecting to a Google Sheet.")
        
        st.markdown("""
        - **CSV File**: 
            1. Select the 'CSV File' option.
            2. Click on 'Upload a CSV file' and choose your CSV file (must be in `.csv` format).
            3. Once uploaded, the data from the file will be displayed, and you can proceed to select a column for further actions.
        
        - **Google Sheet**:
            1. Select the 'Google Sheet' option.
            2. Enter the **Google Sheet ID** (the unique part of the Google Sheet's URL).
            3. Ensure your Google Sheet has granted the service account permission to access it.
            4. The data will load, and you can then select a column to run queries on.
        """)

        st.subheader("Running a Query")
        st.write("""
        - After choosing a data source, preview the data and select the column that contains the entities you want to query.
        - Choose or enter a query template that describes the type of information you're seeking.
        - Click 'Run Search' to start the automated retrieval process. Results will be displayed, and you can download them as a CSV file.
        """)

    # Data Source Selection
    data_source = st.radio("Data Source", ("CSV File", "Google Sheet"))
    data = None

    # CSV Upload
    if data_source == "CSV File":
        uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
        if uploaded_file:
            data = pd.read_csv(uploaded_file)
    
    # Google Sheet Option
    elif data_source == "Google Sheet":
        sheet_id = st.text_input("Enter Google Sheet ID")
        if sheet_id:
            data = connect_to_google_sheet(sheet_id)

    # Display Data Preview
    if data is not None:
        st.write("Preview of Data:")
        st.write(data.head())
        st.subheader("Suggested Key Entities:")
        suggested_entities = data.columns.tolist()
        st.write(suggested_entities)

        selected_column = st.selectbox("Select column for entities", data.columns)
        
        # Suggested Queries
        st.subheader("Suggested Query Templates:")
        suggested_queries = [
            "Get the email address of {entity}",
            "Find the phone number of {entity}",
            "Retrieve the address of {entity}",
            "Get the social media profiles of {entity}",
            "Find the CEO/Founder of {entity}",
        ]
        st.write(suggested_queries)

        query_template = st.text_input("Enter query prompt", suggested_queries[0])

        # Run Search
        if st.button("Run Search"):
            with st.spinner("Searching and extracting..."):
                results = []
                for entity in data[selected_column].dropna().unique():
                    search_query = query_template.replace("{entity}", entity)
                    search_results = perform_web_search(search_query)
                    extracted_info = extract_info_with_llm(entity, search_results, query_template)
                    results.append({"Entity": entity, "Extracted Info": extracted_info})

                result_df = pd.DataFrame(results)
                st.write(result_df)
                
                # Download Button for CSV
                st.download_button("Download CSV", result_df.to_csv(index=False), file_name="results.csv")


if __name__ == "__main__":
    display_dashboard()
