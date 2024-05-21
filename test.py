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



import pandas as pd

def read_all_sheets(filepath):
    """
    Reads an Excel file and returns a dictionary with sheet names as keys and the corresponding DataFrames as values.

    Args:
        filepath (str): The path to the Excel file.
    
    Returns:
        dict: A dictionary containing all sheets in the Excel file.
    """
    # Load the Excel file
    xls = pd.ExcelFile(filepath)

    # Dictionary to store DataFrames, one for each sheet
    sheets_dict = {}

    # Iterate through all the sheets in the file
    for sheet_name in xls.sheet_names:
        # Load each sheet into a DataFrame
        df = pd.read_excel(xls, sheet_name=sheet_name)
        # Store the DataFrame in the dictionary
        sheets_dict[sheet_name] = df

    return sheets_dict

# Example usage:
if __name__ == "__main__":
    file_path = 'System Data Authoring_Oct 2023.xlsx'  # Update this path to the location of your Excel file
    all_sheets = read_all_sheets(file_path)
    
    # Print each sheet's data
    for sheet_name, data in all_sheets.items():
        print(f"Data from sheet: {sheet_name}")
        # print(data)
        
    # # Assuming the seventh sheet is what you want to access
    # seventh_sheet_name = all_sheets[list(all_sheets.keys())[6]]  # Get the name of the seventh sheet

    # # Access the 'BOT name' column from the seventh sheet
    # bot_name_column = seventh_sheet_name['BOT name']
    
    # # Print the 'BOT name' column data
    # print("Data from the 'BOT name' column in the seventh sheet:")
    # print(bot_name_column)

    # Access the seventh sheet by index, ensuring at least seven sheets exist
    if len(all_sheets.keys()) >= 7:
        seventh_sheet_name = list(all_sheets.keys())[6]  # Get the name of the seventh sheet
        seventh_sheet_data = all_sheets[seventh_sheet_name]  # Access the seventh sheet's DataFrame
    
        # Print the entire DataFrame for the seventh sheet
        print(f"Complete data from the seventh sheet ({seventh_sheet_name}):")
        print(seventh_sheet_data)
        
        # Access and print the second column from the seventh sheet's DataFrame
        if seventh_sheet_data.shape[1] >= 2:  # Ensure there are at least two columns
            second_column_data = seventh_sheet_data.iloc[:, 0]  # iloc[:, 1] accesses the second column
            print(f"Data from the second column of the seventh sheet ({seventh_sheet_name}):")
            print(second_column_data)
        else:
            print("The seventh sheet does not have a second column.")
    else:
        print("There are less than seven sheets in the workbook.")



# https://docs.google.com/spreadsheets/d/1o8NjfYWiQTzU78IjoGepu133yx2lxFex/edit?usp=sharing&ouid=107245739744795459088&rtpof=true&sd=true


# CLI
# <BOT/POD/EAT...> 