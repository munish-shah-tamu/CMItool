import pandas as pd
import openpyxl

def read_excel_with_metadata(file_path):
    # Load the workbook and the first sheet
    workbook = openpyxl.load_workbook(file_path, data_only=True)
    sheet_names = workbook.sheetnames
    
    # Extract metadata and content
    excel_data = {}
    
    for sheet in sheet_names:
        # Using pandas to read the content
        df = pd.read_excel(file_path, sheet_name=sheet)
        
        # Metadata about the sheet
        metadata = {
            'sheet_name': sheet,
            'num_rows': df.shape[0],
            'num_columns': df.shape[1]
        }
        
        # Store metadata and content in dictionary
        excel_data[sheet] = {
            'metadata': metadata,
            'content': df
        }
    
    return excel_data

# Usage
file_path = 'path_to_your_excel_file.xlsx'
excel_data = read_excel_with_metadata(file_path)
print(excel_data)
