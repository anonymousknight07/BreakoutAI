from google.oauth2 import service_account
from googleapiclient.discovery import build
import pandas as pd
import os

def connect_to_google_sheet(sheet_id):
    # Set up the credentials with read-write access
    creds = service_account.Credentials.from_service_account_file(
        os.getenv("GOOGLE_APPLICATION_CREDENTIALS"),
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    service = build("sheets", "v4", credentials=creds)
    
    # Read data from the Google Sheet
    sheet = service.spreadsheets().values().get(spreadsheetId=sheet_id, range="Sheet1").execute()
    values = sheet.get("values", [])
    data_df = pd.DataFrame(values[1:], columns=values[0])
    
    return data_df, service

def write_to_google_sheet(service, sheet_id, data, range_name="Sheet1"):
    # Convert the data to the required format for Google Sheets API
    values = [data.columns.tolist()] + data.values.tolist()
    body = {
        "values": values
    }
    
    # Write the data back to the specified range in the Google Sheet
    result = service.spreadsheets().values().update(
        spreadsheetId=sheet_id,
        range=range_name,
        valueInputOption="RAW",
        body=body
    ).execute()
    
    print(f"{result.get('updatedCells')} cells updated.")