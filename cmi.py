import pandas as pd
from SheetParser import parse_excel_sheets
from InternalStructure import BOT, POD, EAT, DM, BART

# Read the Excel file using SheetParser.py
file_path = 'System Data Authoring_Oct 2023.xlsx'
sheets = parse_excel_sheets(file_path)

# Dictionary to store BOT instances
bot_directory = {}

# Function to dynamically add attributes
def add_attributes(entity, row):
    for key, value in row.items():
        if pd.notna(value):  # Only add non-NaN values
            entity.add_attribute(key, value)

# Function to get unique identifier and type
def get_entity_type_and_id(row):
    for key, value in row.items():
        if ('Name' in key or 'ID' in key) and pd.notna(value):
            entity_id = value
            entity_type = key.split()[0]
            return entity_type, entity_id
    return None, None

# Function to get bot name or id
def get_bot_identifier(row):
    if 'BOT Name' in row and pd.notna(row['BOT Name']):
        return row['BOT Name']
    elif 'BOT ID' in row and pd.notna(row['BOT ID']):
        return row['BOT ID']
    return None

# Function to get pod name or id
def get_pod_identifier(row):
    if 'POD Name' in row and pd.notna(row['POD Name']):
        return row['POD Name']
    elif 'POD ID' in row and pd.notna(row['POD ID']):
        return row['POD ID']
    return None

# Function to get eat name or id
def get_eat_identifier(row):
    if 'EAT Name' in row and pd.notna(row['EAT Name']):
        return row['EAT Name']
    elif 'EAT ID' in row and pd.notna(row['EAT ID']):
        return row['EAT ID']
    return None

# Function to get dm name or id
def get_dm_identifier(row):
    if 'DM Name' in row and pd.notna(row['DM Name']):
        return row['DM Name']
    elif 'DM ID' in row and pd.notna(row['DM ID']):
        return row['DM ID']
    return None

# Populate entities dynamically
for sheet_name, df in sheets.items():
    for _, row in df.iterrows():
        entity_type, entity_id = get_entity_type_and_id(row)
        
        if entity_type == 'BOT':
            if entity_id not in bot_directory:
                bot = BOT(entity_id)
                bot_directory[entity_id] = bot
            else:
                bot = bot_directory[entity_id]
            add_attributes(bot, row)
            print(f"Added/Updated BOT: {entity_id}")
        
        elif entity_type == 'POD':
            bot_name = get_bot_identifier(row)
            if bot_name in bot_directory:
                pod = POD(entity_id)
                add_attributes(pod, row)
                bot_directory[bot_name].add_child(pod)
                print(f"Added POD: {entity_id} to BOT: {bot_name}")
        
        elif entity_type == 'EAT':
            bot_name = get_bot_identifier(row)
            pod_name = get_pod_identifier(row)
            if bot_name in bot_directory:
                eat = EAT(entity_id)
                add_attributes(eat, row)
                for pod in bot_directory[bot_name].children:
                    if pod.identifier == pod_name:
                        pod.add_child(eat)
                        print(f"Added EAT: {entity_id} to POD: {pod_name} in BOT: {bot_name}")
        
        elif entity_type == 'DM':
            bot_name = get_bot_identifier(row)
            pod_name = get_pod_identifier(row)
            eat_name = get_eat_identifier(row)
            if bot_name in bot_directory:
                dm = DM(entity_id)
                add_attributes(dm, row)
                for pod in bot_directory[bot_name].children:
                    if pod.identifier == pod_name:
                        for eat in pod.children:
                            if eat.identifier == eat_name:
                                eat.add_child(dm)
                                print(f"Added DM: {entity_id} to EAT: {eat_name} in POD: {pod_name} in BOT: {bot_name}")
        
        elif entity_type == 'BART':
            bot_name = get_bot_identifier(row)
            pod_name = get_pod_identifier(row)
            eat_name = get_eat_identifier(row)
            dm_name = get_dm_identifier(row)
            if bot_name in bot_directory:
                bart = BART(entity_id)
                add_attributes(bart, row)
                for pod in bot_directory[bot_name].children:
                    if pod.identifier == pod_name:
                        for eat in pod.children:
                            if eat.identifier == eat_name:
                                for dm in eat.children:
                                    if dm.identifier == dm_name:
                                        dm.add_child(bart)
                                        print(f"Added BART: {entity_id} to DM: {dm_name} in EAT: {eat_name} in POD: {pod_name} in BOT: {bot_name}")

# Display a specific POD with debugging
bot_identifier = 'Operate Refrigeration or Air Conditioning Systems'  # Replace with actual BOT identifier
pod_identifier = 'Use of grid electricity- location based method (scope 2)'  # Replace with actual POD identifier

if bot_identifier in bot_directory:
    print(f"Found BOT with identifier {bot_identifier}")
    bot = bot_directory[bot_identifier]
    found_pod = False
    for pod in bot.children:
        if pod.identifier == pod_identifier:
            print(f"Found POD with identifier {pod_identifier} in BOT {bot_identifier}")
            print(pod.display_node())
            print(pod.display_node_attributes())
            found_pod = True
            break
    if not found_pod:
        print(f"POD with identifier {pod_identifier} not found in BOT {bot_identifier}")
else:
    print(f"BOT with identifier {bot_identifier} not found.")

# Optionally, display the entire BOT directory
for bot in bot_directory.values():
    print(bot.display())
