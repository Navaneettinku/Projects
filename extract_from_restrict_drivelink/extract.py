import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

# Define OAuth Scopes
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Path to Service Account JSON file
CREDENTIALS_FILE = ".json"   [ your credentials]

# Authenticate using Service Account
creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
client = gspread.authorize(creds)

# ✅ Use Spreadsheet ID instead of Name
SPREADSHEET_ID = "[your sheet ID]"
spreadsheet = client.open_by_key(SPREADSHEET_ID)

# ✅ Select Sheet 1
sheet1 = spreadsheet.get_worksheet(0)  # First sheet (Index starts at 0)
data1 = sheet1.get_all_values()
df1 = pd.DataFrame(data1[1:], columns=data1[0])  # First row as headers

# ✅ Select Sheet 2
sheet2 = spreadsheet.get_worksheet(1)  # Second sheet
data2 = sheet2.get_all_values()
df2 = pd.DataFrame(data2[1:], columns=data2[0])  # First row as headers

# Save both sheets separately
df1.to_csv("sheet1_output.csv", index=False)
df2.to_csv("sheet2_output.csv", index=False)
df1.to_excel("sheet1_output.xlsx", index=False, engine="openpyxl")
df2.to_excel("sheet2_output.xlsx", index=False, engine="openpyxl")

print("✅ Data extracted and saved for both sheets!")
