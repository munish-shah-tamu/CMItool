import pandas as pd
from ModelRepresentation import BotMetadata, PodMetadata, EatMetadata, DmMetadata, BartMetadata
from SheetParser import parse_excel_sheets

def create_bot_objects_from_excel(file_path):
    sheets = parse_excel_sheets(file_path)
    bots = {}

    for sheet_name, df in sheets.items():
        for _, row in df.iterrows():
            # Identify Bot data
            bot_name = row.get('BOT Name')
            if pd.notna(bot_name):
                bot_name = str(bot_name)
                if bot_name not in bots:
                    bots[bot_name] = BotMetadata(
                        sysType=row.get('BOT SysType', 0),
                        description=row.get('Description', ''),
                        botName=bot_name,
                        botId=row.get('BOT ID', ''),
                        botType=row.get('BOT Type', ''),
                        botIndex=row.get('BOT Index', ''),
                        botDescription=row.get('BOT Description', ''),
                        domainInformation=row.get('Domain Information', ''),
                        image=row.get('Image', ''),
                        longDescription=row.get('Long Description', ''),
                        summary=row.get('Summary', ''),
                        commonEquipment=row.get('Common Equipment', ''),
                        commonProcesses=row.get('Common Processes', ''),
                        commonOperations=row.get('Common Operations', ''),
                        customer=row.get('Customer', 'Atomiton'),
                        eatId=row.get('EAT ID', ''),
                    )
                # Update existing BOT with additional information
                bot = bots[bot_name]
                attributes = [
                    ('Description', 'description'),
                    ('BOT ID', 'botId'),
                    ('BOT Type', 'botType'),
                    ('BOT Index', 'botIndex'),
                    ('BOT Description', 'botDescription'),
                    ('Domain Information', 'domainInformation'),
                    ('Image', 'image'),
                    ('Long Description', 'longDescription'),
                    ('Summary', 'summary'),
                    ('Common Equipment', 'commonEquipment'),
                    ('Common Processes', 'commonProcesses'),
                    ('Common Operations', 'commonOperations'),
                    ('Customer', 'customer'),
                    ('EAT ID', 'eatId')
                ]
                for column, attr in attributes:
                    if pd.notna(row.get(column)):
                        setattr(bot, attr, row[column])

    return bots

def create_pod_objects_from_excel(file_path):
    sheets = parse_excel_sheets(file_path)
    pods = {}

    for sheet_name, df in sheets.items():
        pod_name_column = None
        
        # Find the column with "POD Name"
        for column in df.columns:
            if df[column].astype(str).str.contains("POD Name", na=False).any():
                pod_name_column = column
                break
        if pod_name_column is None:
            continue  # No POD Name column found in this sheet, skip to next sheet
        
        # Get the index of the row where "POD Name" appears
        pod_start_index = df[df[pod_name_column].astype(str).str.contains("POD Name", na=False)].index[0] + 1
        
        # Iterate through rows starting from the row below "POD Name"
        for _, row in df[pod_start_index:].iterrows():
            pod_name = row[pod_name_column]
            if pd.notna(pod_name):
                pod_name = str(pod_name)
                if pod_name not in pods:
                    pods[pod_name] = PodMetadata(
                        sysType=row.get('POD SysType', 0),
                        description=row.get('Description', ''),
                        carbonSource=row.get('Carbon Source', ''),
                        podName=pod_name,
                        customer=row.get('Customer', 'Atomiton'),
                        podCategory=row.get('POD Category', ''),
                        usability=row.get('Usability', ''),
                        domainInformation=row.get('Domain Information', ''),
                        image=row.get('Image', ''),
                        countrySpecific=row.get('Country Specific', ''),
                        referenceYear=row.get('Reference Year', ''),
                    )
                # Update existing POD with additional information
                pod = pods[pod_name]
                for col in df.columns:
                    if pd.notna(row[col]):
                        column_name = col.strip()
                        value = row[col]
                        if column_name == 'POD SysType':
                            pod.sysType = value
                        elif column_name == 'Description':
                            pod.description = value
                        elif column_name == 'Carbon Source':
                            pod.carbonSource = value
                        elif column_name == 'Customer':
                            pod.customer = value
                        elif column_name == 'POD Category':
                            pod.podCategory = value
                        elif column_name == 'Usability':
                            pod.usability = value
                        elif column_name == 'Domain Information':
                            pod.domainInformation = value
                        elif column_name == 'Image':
                            pod.image = value
                        elif column_name == 'Country Specific':
                            pod.countrySpecific = value
                        elif column_name == 'Reference Year':
                            pod.referenceYear = value

    return pods

def create_eat_objects_from_excel(file_path):
    sheets = parse_excel_sheets(file_path)
    eats = {}

    for sheet_name, df in sheets.items():
        for _, row in df.iterrows():
            # Identify EAT data
            eatName = row.get('EAT Name')
            if pd.notna(eatName):
                eatName = str(eatName) 
                if eatName not in eats:
                    eats[eatName] = EatMetadata(
                        sysType=row.get('EAT SysType', 0),
                        description=row.get('Description', ''),
                        eatName=row.get('EAT Name', ''),
                        eatFullName=row.get('#EAT Full Name', ''),
                        ghgAmFullName=row.get('#GHG-AM Full Name', ''),
                        ghgAmName=row.get('GHG-AM Name', ''),
                        mdDescription=row.get('MD Description', ''),
                        methodologyName=row.get('Methodology Name', ''),
                        carbonSource=row.get('Carbon Source', ''),
                        action=row.get('Action', ''),
                        activityDescription=row.get('Activity Description', ''),
                        reportedQuantity=row.get('Reported Quantity', ''),
                        rqDescription=row.get('Reported Quantity Description', ''),
                        rqAbbreviation=row.get('RQ Abbreviation', ''),
                        eaDataSource=row.get('EA Data Source', ''),
                    )
                # Update existing EAT with additional information
                eat = eats[eatName]
                attributes = [
                    ('EAT SysType', 'sysType'),
                    ('Description', 'description'),
                    ('#EAT Full Name', 'eatFullName'),
                    ('#GHG-AM Full Name', 'ghgAmFullName'),
                    ('GHG-AM Name', 'ghgAmName'),
                    ('MD Description', 'mdDescription'),
                    ('Methodology Name', 'methodologyName'),
                    ('Carbon Source', 'carbonSource'),
                    ('Action', 'action'),
                    ('Activity Description', 'activityDescription'),
                    ('Reported Quantity', 'reportedQuantity'),
                    ('Reported Quantity Description', 'rqDescription'),
                    ('RQ Abbreviation', 'rqAbbreviation'),
                    ('EA Data Source', 'eaDataSource')
                ]
                for column, attr in attributes:
                    if pd.notna(row.get(column)):
                        setattr(eat, attr, row[column])

    return eats

def create_dm_objects_from_excel(file_path):
    sheets = parse_excel_sheets(file_path)
    dms = {}

    for sheet_name, df in sheets.items():
        for _, row in df.iterrows():
            # Identify DM data
            dm_id = row.get('DM ID') or row.get('DM')
            if pd.notna(dm_id):
                dm_id = str(dm_id)
                if dm_id not in dms:
                    dms[dm_id] = DmMetadata(
                        sysType=row.get('DM SysType', 0),
                        description=row.get('Description', ''),
                        dmType=row.get('DM Type', ''),
                        formula=row.get('Formula', ''),
                        notations=row.get('Notations', ''),
                        additionalVariables=row.get('Additional Variables', ''),
                        dmPref=row.get('DM Pref', None),
                        condition1=row.get('Condition 1', ''),
                        condition2=row.get('Condition 2', ''),
                        condition3=row.get('Condition 3', ''),
                        notes=row.get('Notes', ''),
                    )
                # Update existing DM with additional information
                dm = dms[dm_id]
                attributes = [
                    ('DM SysType', 'sysType'),
                    ('Description', 'description'),
                    ('DM Type', 'dmType'),
                    ('Formula', 'formula'),
                    ('Notations', 'notations'),
                    ('Additional Variables', 'additionalVariables'),
                    ('DM Pref', 'dmPref'),
                    ('Condition 1', 'condition1'),
                    ('Condition 2', 'condition2'),
                    ('Condition 3', 'condition3'),
                    ('Notes', 'notes')
                ]
                for column, attr in attributes:
                    if pd.notna(row.get(column)):
                        setattr(dm, attr, row[column])

    return dms

def create_bart_objects_from_excel(file_path):
    sheets = parse_excel_sheets(file_path)
    barts = {}

    for sheet_name, df in sheets.items():
        for _, row in df.iterrows():
            # Identify BART data
            bart_name = row.get('BART ID')
            if pd.notna(bart_name):
                bart_name = str(bart_name)
                if bart_name not in barts:
                    barts[bart_name] = BartMetadata(
                        sysType=row.get('BART SysType', 0),
                        description=row.get('Description', ''),
                        bartFullName=row.get('#BART Full Name', ''),
                        carbonSource=row.get('Carbon Source', ''),
                        carbonSourceLifecycle=row.get('Carbon Source', ''),
                        activityDescription=row.get('Activity Description', ''),
                        measuredQuantity=row.get('Measured Quantity', ''),
                        measuredQuantityType=row.get('Measured Quantity Type', ''),
                        mqDescription=row.get('Measured Quantity Description', ''),
                        mqAbbreviation=row.get('MQ Abbreviation', ''),
                        unitAllowedValues=row.get('Unit Allowed Values', ''),
                    )
                # Update existing BART with additional information
                bart = barts[bart_name]
                attributes = [
                    ('BART SysType', 'sysType'),
                    ('Description', 'description'),
                    ('#BART Full Name', 'bartFullName'),
                    ('Carbon Source', 'carbonSource'),
                    ('Carbon Source', 'carbonSourceLifecycle'),
                    ('Activity Description', 'activityDescription'),
                    ('Measured Quantity', 'measuredQuantity'),
                    ('Measured Quantity Type', 'measuredQuantityType'),
                    ('Measured Quantity Description', 'mqDescription'),
                    ('MQ Abbreviation', 'mqAbbreviation'),
                    ('Unit Allowed Values', 'unitAllowedValues')
                ]
                for column, attr in attributes:
                    if pd.notna(row.get(column)):
                        setattr(bart, attr, row[column])

    return barts
def print_bart(barts):
    for bart_name, bart in barts.items():
        print(f"BART Name: {bart_name}")
        print(f"  SysType: {bart.sysType}")
        print(f"  Description: {bart.description}")
        print(f"  BART Full Name: {bart.bartFullName}")
        print(f"  Carbon Source: {bart.carbonSource}")
        print(f"  Carbon Source Lifecycle: {bart.carbonSourceLifecycle}")
        print(f"  Activity Description: {bart.activityDescription}")
        print(f"  Measured Quantity: {bart.measuredQuantity}")
        print(f"  Measured Quantity Type: {bart.measuredQuantityType}")
        print(f"  MQ Description: {bart.mqDescription}")
        print(f"  MQ Abbreviation: {bart.mqAbbreviation}")
        print(f"  Unit Allowed Values: {bart.unitAllowedValues}")
        print("\n")

def print_dm(dms):
    for dm_id, dm in dms.items():
        print(f"DM Name: {dm_id}")
        print(f"  SysType: {dm.sysType}")
        print(f"  Description: {dm.description}")
        print(f"  DM Type: {dm.dmType}")
        print(f"  Formula: {dm.formula}")
        print(f"  Notations: {dm.notations}")
        print(f"  Additional Variables: {dm.additionalVariables}")
        print(f"  DM Pref: {dm.dmPref}")
        print(f"  Condition 1: {dm.condition1}")
        print(f"  Condition 2: {dm.condition2}")
        print(f"  Condition 3: {dm.condition3}")
        print(f"  Notes: {dm.notes}")
        print("\n")
        
def print_eat(eats):
    for eat_name, eat in eats.items():
        print(f"EAT Name: {eat.eatName}")
        print(f"  SysType: {eat.sysType}")
        print(f"  Description: {eat.description}")
        print(f"  EAT Full Name: {eat.eatFullName}")
        print(f"  GHG AM Full Name: {eat.ghgAmFullName}")
        print(f"  GHG AM Name: {eat.ghgAmName}")
        print(f"  MD Description: {eat.mdDescription}")
        print(f"  Methodology Name: {eat.methodologyName}")
        print(f"  Carbon Source: {eat.carbonSource}")
        print(f"  Action: {eat.action}")
        print(f"  Activity Description: {eat.activityDescription}")
        print(f"  Reported Quantity: {eat.reportedQuantity}")
        print(f"  RQ Description: {eat.rqDescription}")
        print(f"  RQ Abbreviation: {eat.rqAbbreviation}")
        print(f"  EA Data Source: {eat.eaDataSource}")
        print("\n")

def print_pod(pod_name, pods):
    if pod_name in pods:
        pod = pods[pod_name]
        print(f"Pod Name: {pod.podName}")
        print(f"SysType: {pod.sysType}")
        print(f"Description: {pod.description}")
        print(f"Carbon Source: {pod.carbonSource}")
        print(f"Customer: {pod.customer}")
        print(f"Pod Category: {pod.podCategory}")
        print(f"Usability: {pod.usability}")
        print(f"Domain Information: {pod.domainInformation}")
        print(f"Image: {pod.image}")
        print(f"Country Specific: {pod.countrySpecific}")
        print(f"Reference Year: {pod.referenceYear}")
        print("GhgAms:")
        for ghg_am in pod.ghgAms:
            print(f"  GhgAm FullName: {ghg_am.ghgAMFullName}")
            print(f"  Suppressed Dm List: {ghg_am.suppressedDmList}")
        print("Descriptions:")
        for desc in pod.descriptions:
            print(f"  - {desc}")
    else:
        print(f"Pod with name '{pod_name}' not found.")

def print_bot(bot_name, bots):
    if bot_name in bots:
        bot = bots[bot_name]
        print(f"Bot Name: {bot.botName}")
        print(f"Bot ID: {bot.botId}")
        print(f"Bot Type: {bot.botType}")
        print(f"Bot Index: {bot.botIndex}")
        print(f"Description: {bot.description}")
        print(f"Bot Description: {bot.botDescription}")
        print(f"Domain Information: {bot.domainInformation}")
        print(f"Image: {bot.image}")
        print(f"Long Description: {bot.longDescription}")
        print(f"Summary: {bot.summary}")
        print(f"Common Equipment: {bot.commonEquipment}")
        print(f"Common Processes: {bot.commonProcesses}")
        print(f"Common Operations: {bot.commonOperations}")
        print(f"Customer: {bot.customer}")
        print(f"EAT ID: {bot.eatId}")
        print("Descriptions:")
        for desc in bot.descriptions:
            print(f"  - {desc}")
        print("Pods:")
        for pod in bot.pods:
            print(f"  Pod Name: {pod.podName}")
            print(f"  Customer: {pod.customer}")
            print(f"  Pod Requirement: {pod.podReq}")
    else:
        print(f"Bot with name '{bot_name}' not found.")

def print_all_pods(pods):
    for pod_name, pod in pods.items():
        print(f"Pod Name: {pod.podName}")
        print(f"  SysType: {pod.sysType}")
        print(f"  Description: {pod.description}")
        print(f"  Carbon Source: {pod.carbonSource}")
        print(f"  Customer: {pod.customer}")
        print(f"  Pod Category: {pod.podCategory}")
        print(f"  Usability: {pod.usability}")
        print(f"  Domain Information: {pod.domainInformation}")
        print(f"  Image: {pod.image}")
        print(f"  Country Specific: {pod.countrySpecific}")
        print(f"  Reference Year: {pod.referenceYear}")
        print("  GhgAms:")
        for ghg_am in pod.ghgAms:
            print(f"    GhgAm FullName: {ghg_am.ghgAMFullName}")
            print(f"    Suppressed Dm List: {ghg_am.suppressedDmList}")
        print("  Descriptions:")
        for desc in pod.descriptions:
            print(f"    - {desc}")
        print("\n")
# Example usage
if __name__ == "__main__":
    file_path = 'System Data Authoring_Oct 2023.xlsx'
    bots = create_bot_objects_from_excel(file_path)
    pods = create_pod_objects_from_excel(file_path)
    eats = create_eat_objects_from_excel(file_path)
    dms = create_dm_objects_from_excel(file_path)
    barts = create_bart_objects_from_excel(file_path)
    
    # Print all BARTs
    # print_bart(barts)
    # Print all DMs
    # print_dm(dms)
    # Print all EATs
    print_eat(eats)
    # # Print all BOT names
    # print("All BOT Names:")
    # for bot_name in bots:
    #     print(bot_name)

    # print("All POD Names:")
    # for pod_name in pods:
    #     print(pod_name)

    # # Print a specific BOT by name
    # print("\nDetails of a specific BOT:")
    # print_bot("Operate Refrigeration or Air Conditioning Systems", bots)

    # print("\nDetails of a specific POD:")
    # print_pod("Running electrical passenger vehicles with distance data", pods)

    # print_all_pods(pods)
