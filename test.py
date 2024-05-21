# import pandas as pd
# import openpyxl
# from io import BytesIO

# def read_excel_file(path):

#     response = request.get(url) 
#     response.raise_for_status()

#     workbook = pd.ExcelFile(BytesIO(response.content))

#     excel_data = {}

#     for sheet in workbook.sheet_names:
#         df = workbook.parse(sheet_name = sheet)

#         metadata = {
#             'sheet_name': sheet,
#             'num_rows': df.shape[0],
#             'num_columns': df.shape[1]
#         }

#         content = df.to_dict(orient='records')
#         excel_data[sheet] = {
#             'metadata': metadata,
#             'content': content
#         }

#     return excel_data

# if __name__ == "__main__":
#     url = 'https://docs.google.com/spreadsheets/d/1o8NjfYWiQTzU78IjoGepu133yx2lxFex/edit#gid=1916977110'  # Replace this with the actual URL to your Excel file
#     excel_data = read_excel_file(url)
#     print(excel_data)



# import pandas as pd
# import openpyxl

# def read_excel_file(file_path):
#     """
#     Reads an Excel file and extracts metadata and content from each sheet.
    
#     Args:
#         file_path (str): The path to the Excel file.
    
#     Returns:
#         dict: A dictionary where each key is a sheet name and the value is another dictionary containing
#               both metadata and the content as a pandas DataFrame serialized to a dictionary.
#     """
#     # Load the workbook and get all sheet names
#     workbook = openpyxl.load_workbook(file_path, data_only=True)
#     sheet_names = workbook.sheetnames

#     # Initialize the result dictionary
#     excel_data = {}

#     for sheet in sheet_names:
#         # Read the sheet data into a pandas DataFrame
#         df = pd.read_excel(file_path, sheet_name=sheet)

#         # Extract metadata from the sheet
#         metadata = {
#             'sheet_name': sheet,
#             'num_rows': df.shape[0],
#             'num_columns': df.shape[1]
#         }

#         # Serialize DataFrame to a dictionary for API output
#         content = df.to_dict(orient='records')

#         # Add to result dictionary
#         excel_data[sheet] = {
#             'metadata': metadata,
#             'content': content
#         }

#     return excel_data

# # Example usage:
# if __name__ == "__main__":
#     file_path = '/Users/munishshah/CS/Atomiton/shared/System Data Authoring_Oct 2023.xlsx'  # Replace this with the path to your Excel file
#     excel_data = read_excel_file(file_path)
#     print(excel_data)



import gspread
from google.oauth2.service_account import Credentials

def authenticate_gspread():
    """
    Authenticate with Google Sheets using Google Auth.
    """
    scope = [
        "https://www.googleapis.com/auth/spreadsheets.readonly",
        "https://www.googleapis.com/auth/drive.file"
    ]
    creds = Credentials.from_service_account_file('path_to_your_service_account_file.json', scopes=scope)
    client = gspread.authorize(creds)
    return client

def read_google_sheet(sheet_url):
    """
    Read data from a Google Sheet given a shareable link and return as a list of dictionaries for each sheet.
    
    Args:
        sheet_url (str): URL to the shared Google Sheet.
    
    Returns:
        dict: A dictionary where each key is a sheet name and the value is the list of records.
    """
    client = authenticate_gspread()
    
    # Open the Google Sheet using its URL
    sheet = client.open_by_url(sheet_url)

    sheets_data = {}
    # Loop through each worksheet in the spreadsheet
    for worksheet in sheet.worksheets():
        records = worksheet.get_all_records()
        sheets_data[worksheet.title] = records

    return sheets_data

# Example usage
if __name__ == "__main__":
    sheet_url = "https://docs.google.com/spreadsheets/d/1o8NjfYWiQTzU78IjoGepu133yx2lxFex/edit?usp=sharing&ouid=107245739744795459088&rtpof=true&sd=true"  # Replace with your actual URL
    data = read_google_sheet(sheet_url)
    print(data)


# https://docs.google.com/spreadsheets/d/1o8NjfYWiQTzU78IjoGepu133yx2lxFex/edit?usp=sharing&ouid=107245739744795459088&rtpof=true&sd=true


# CLI
# <BOT/POD/EAT...> 