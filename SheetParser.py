import pandas as pd

def parse_excel_sheets(file_path):
    # Read the Excel file
    xls = pd.ExcelFile(file_path)
    
    # Dictionary to store dataframes for each sheet
    sheet_dict = {}
    
    # Iterate through each sheet and store the data in the dictionary
    for sheet_name in xls.sheet_names:
        sheet_dict[sheet_name] = pd.read_excel(xls, sheet_name=sheet_name)
    
    return sheet_dict

if __name__ == "__main__":
    # Example usage (Remove or comment out this section in production)
    file_path = 'System Data Authoring_Oct 2023.xlsx'
    sheets = parse_excel_sheets(file_path)
    for sheet_name, df in sheets.items():
        print(f"Sheet name: {sheet_name}")
        print(df.head())