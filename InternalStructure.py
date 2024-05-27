class Base:
    def __init__(self, identifier):
        self.identifier = identifier
        self.children = []
        self.attributes = {}
    
    def add_child(self, child):
        self.children.append(child)
    
    def add_attribute(self, key, value):
        self.attributes[key] = value
    
    def display(self, level=0):
        indent = "  " * level
        attributes_display = "\n".join(f"{indent}  {k}: {v}" for k, v in self.attributes.items())
        children_display = "\n".join(child.display(level + 1) for child in self.children)
        return f"{indent}{self.identifier}:\n{attributes_display}\n{children_display}"

    def display_node(self, level=0):
        indent = "  " * level
        attributes_display = "\n".join(f"{indent}  {k}: {v}" for k, v in self.attributes.items())
        return f"{indent}{self.identifier}:\n{attributes_display}"
    
    def display_node_attributes(self):
        attributes_display = "\n".join(f"  {k}: {v}" for k, v in self.attributes.items())
        return f"{self.identifier}:\n{attributes_display}"

class BART(Base):
    def __init__(self, identifier):
        super().__init__(identifier)

class DM(Base):
    def __init__(self, identifier):
        super().__init__(identifier)

class EAT(Base):
    def __init__(self, identifier):
        super().__init__(identifier)

class POD(Base):
    def __init__(self, identifier):
        super().__init__(identifier)

class BOT(Base):
    def __init__(self, identifier):
        super().__init__(identifier)

# Example usage
def main():
    bot_directory = []

    # Create a BOT
    bot = BOT("AlphaBot")
    bot.add_attribute("Location", "HQ")
    bot.add_attribute("Status", "Active")

    # Create PODs and add them to the BOT
    pod1 = POD("POD_X200")
    pod1.add_attribute("Manufacturer", "CompanyA")
    pod1.add_attribute("Year", "2022")
    
    pod2 = POD("POD_X300")
    pod2.add_attribute("Manufacturer", "CompanyB")
    pod2.add_attribute("Year", "2023")
    
    bot.add_child(pod1)
    bot.add_child(pod2)

    # Create EATs and add them to the PODs
    eat1 = EAT("EAT_Mixer")
    eat1.add_attribute("Capacity", "500L")
    
    eat2 = EAT("EAT_Blender")
    eat2.add_attribute("Capacity", "300L")
    
    pod1.add_child(eat1)
    pod2.add_child(eat2)

    # Create DMs and add them to the EATs
    dm1 = DM("DM_Mixing")
    dm1.add_attribute("Duration", "2h")
    
    dm2 = DM("DM_Blending")
    dm2.add_attribute("Duration", "1h")
    
    eat1.add_child(dm1)
    eat2.add_child(dm2)

    # Create BARTs and add them to the DMs
    bart1 = BART("BART_Fast")
    bart1.add_attribute("Speed", "Fast")
    bart1.add_attribute("Output", "High")
    
    bart2 = BART("BART_Moderate")
    bart2.add_attribute("Speed", "Moderate")
    bart2.add_attribute("Output", "Medium")
    
    dm1.add_child(bart1)
    dm2.add_child(bart2)

    # Add the BOT to the directory
    bot_directory.append(bot)

    # Display the entire BOT directory
    for bot in bot_directory:
        print(bot.display())

    # Display specific POD and its contents
    print("\nDisplaying specific POD (POD_X200) and its contents:")
    print(pod1.display())

    # Display specific EAT and its contents
    print("\nDisplaying specific EAT (EAT_Mixer) and its contents:")
    print(eat1.display())

    # Display specific DM and its contents
    print("\nDisplaying specific DM (DM_Mixing) and its contents:")
    print(dm1.display())

    # Display specific BART and its contents
    print("\nDisplaying specific BART (BART_Fast) and its contents:")
    print(bart1.display_node())

    print("\nDisplaying BOT's attributes:")
    print(bot.display_node_attributes())

    print("\nDisplaying POD_X200's attributes:")
    print(pod1.display_node_attributes())

    print("\nDisplaying EAT_Mixer's attributes:")
    print(eat1.display_node_attributes())

    print("\nDisplaying DM_Mixing's attributes:")
    print(dm1.display_node_attributes())

    print("\nDisplaying BART_Fast's attributes:")
    print(bart1.display_node_attributes())

if __name__ == "__main__":
    main()
