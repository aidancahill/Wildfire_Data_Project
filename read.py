
from googleapiclient.discovery import build
from google.oauth2 import service_account


SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1GmECahFvCcPIbbm3Pw7FSHyhYcbmlUukurEJCTl3_Go'



service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="California_Fire_Perimeters_(all)!A1:R21319").execute()
#values = result.get('values', [])

print(result)


