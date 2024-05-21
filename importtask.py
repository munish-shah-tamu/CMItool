import pandas as pd
import openpyxl
import classes.py

def read_excel_with_metadata(file_path):
    # Load the workbook and the first sheet
    workbook = openpyxl.load_workbook(file_path, data_only=True)
    sheet_names = workbook.sheetnames
    
    # Extract metadata and content
    excel_data = {}
    
    for tab in sheet_names:
        # Using pandas to read the content
        df = pd.read_excel(file_path, sheet_name=tab)
        
        # Metadata about the sheet
        metadata = {
            'sheet_name': tab,
            'num_rows': df.shape[0],
            'num_columns': df.shape[1]
        }
        
        # Store metadata and content in dictionary
        excel_data[tab] = {
            'metadata': metadata,
            'content': df
        }
    
    return excel_data

# Usage
file_path = 'path_to_your_excel_file.xlsx'
excel_data = read_excel_with_metadata(file_path)
print(excel_data)

# Dictonary : key -> tab ; value -> dictionary: -> key (column header), value: array of the data

# -> -> -> -> -> ->
# -  -
# -  -
# -


# Tasks
# - read sheets into dictionary
# - copy over classes
# - read dictionary into some DS of bots

class EatMetadataType:
    def __init__(self, 
                 sysType=None, 
                 specifiers=None, 
                 qualifiers=None, 
                 eatName="", 
                 eatFullName="", 
                 ghgAmFullName="", 
                 ghgAmName="", 
                 mdDescription="", 
                 methodologyName="", 
                 carbonSource="", 
                 action="", 
                 activityDescription="", 
                 reportedQuantity="", 
                 rqDescription="", 
                 rqAbbreviation="", 
                 eaDataSource=""):
        self.sysType = sysType or self.default_sysType()
        self.specifiers = specifiers or []
        self.qualifiers = qualifiers or []
        self.eatName = eatName
        self.eatFullName = eatFullName
        self.ghgAmFullName = ghgAmFullName
        self.ghgAmName = ghgAmName
        self.mdDescription = mdDescription
        self.methodologyName = methodologyName
        self.carbonSource = carbonSource
        self.action = action
        self.activityDescription = activityDescription
        self.reportedQuantity = reportedQuantity
        self.rqDescription = rqDescription
        self.rqAbbreviation = rqAbbreviation
        self.eaDataSource = eaDataSource

