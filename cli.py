import argparse
from ModelRepresentation import BotMetadata, PodMetadata, EatMetadata, DmMetadata, BartMetadata
from SheetParser import parse_excel_sheets
from SheetModelMapping import create_bot_objects_from_excel, create_pod_objects_from_excel, create_eat_objects_from_excel, create_dm_objects_from_excel, create_bart_objects_from_excel

file_path = 'System Data Authoring_Oct 2023.xlsx'  # Update this path accordingly

# Load data from the Excel file
bots = create_bot_objects_from_excel(file_path)
pods = create_pod_objects_from_excel(file_path)
eats = create_eat_objects_from_excel(file_path)
dms = create_dm_objects_from_excel(file_path)
barts = create_bart_objects_from_excel(file_path)

def list_all_objects(obj_dict, obj_type):
    print(f"All {obj_type}s:")
    for name in obj_dict.keys():
        print(name)

def list_all_details(obj_dict, obj_type):
    print(f"All {obj_type} Details:")
    for obj in obj_dict.values():
        print(vars(obj))

def list_details_by_name(obj_dict, name, obj_type):
    obj = obj_dict.get(name)
    if obj:
        print(vars(obj))
    else:
        print(f"{obj_type} '{name}' not found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI for managing BOTs, PODs, EATs, DMs, and BARTs.")
    
    subparsers = parser.add_subparsers(dest="command")

    # Define commands for listing all names
    list_parser = subparsers.add_parser("list", help="List all names of a given type.")
    list_parser.add_argument("--X", type=str, choices=["BOT", "POD", "EAT", "DM", "BART"], required=True, help="Specify the type of object.")
    
    # Define commands for listing all details
    listdetails_parser = subparsers.add_parser("listdetails", help="List all details of a given type or details of a specific name.")
    listdetails_parser.add_argument("--X", type=str, choices=["BOT", "POD", "EAT", "DM", "BART"], required=True, help="Specify the type of object.")
    listdetails_parser.add_argument("name", nargs='?', type=str, help="The name of the object (optional).")

    args = parser.parse_args()

    if args.command == "list":
        if args.X == "BOT":
            list_all_objects(bots, "BOT")
        elif args.X == "POD":
            list_all_objects(pods, "POD")
        elif args.X == "EAT":
            list_all_objects(eats, "EAT")
        elif args.X == "DM":
            list_all_objects(dms, "DM")
        elif args.X == "BART":
            list_all_objects(barts, "BART")
    elif args.command == "listdetails":
        if args.name:
            if args.X == "BOT":
                list_details_by_name(bots, args.name, "BOT")
            elif args.X == "POD":
                list_details_by_name(pods, args.name, "POD")
            elif args.X == "EAT":
                list_details_by_name(eats, args.name, "EAT")
            elif args.X == "DM":
                list_details_by_name(dms, args.name, "DM")
            elif args.X == "BART":
                list_details_by_name(barts, args.name, "BART")
        else:
            if args.X == "BOT":
                list_all_details(bots, "BOT")
            elif args.X == "POD":
                list_all_details(pods, "POD")
            elif args.X == "EAT":
                list_all_details(eats, "EAT")
            elif args.X == "DM":
                list_all_details(dms, "DM")
            elif args.X == "BART":
                list_all_details(barts, "BART")
    else:
        parser.print_help()
