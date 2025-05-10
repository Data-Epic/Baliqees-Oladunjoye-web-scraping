import gspread
from google.oauth2.service_account import Credentials

SERVICE_ACCOUNT_FILE = r'C:\Users\baliq\Desktop\webscraping2\creds.json'

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

def connect_to_google_sheet(sheet_name):
    creds = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES
    )
    client = gspread.authorize(creds)
    spreadsheet = client.open(sheet_name)
    return spreadsheet

def upload_df_to_sheet(spreadsheet, worksheet_name, df):
    try:
        worksheet = spreadsheet.worksheet(worksheet_name)
    except gspread.exceptions.WorksheetNotFound:
        worksheet = spreadsheet.add_worksheet(title=worksheet_name, rows="1000", cols="30")
    
    worksheet.clear()  # Clear existing data

    # Insert headers
    worksheet.insert_row(df.columns.tolist(), 1)

    # Insert data rows
    worksheet.insert_rows(df.values.tolist(), 2)

    print(f"Uploaded to '{worksheet_name}' successfully!")
