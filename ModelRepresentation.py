#Data Types
class AttachmentType:
    def __init__(self, sysType=None, description=""):
        self.sysType = sysType or self.default_sysType()
        self.description = description

    def default_sysType(self):
        return 0  # Replace with appropriate default value

class TreeCategoryNodeType:
    def __init__(self, sysType=None, description=""):
        self.sysType = sysType or self.default_sysType()
        self.description = description

    def default_sysType(self):
        return 0  # Replace with appropriate default value

class MetadataType(TreeCategoryNodeType):
    def __init__(self, sysType=None, description=""):
        super().__init__(sysType, description)

class MetadataAttachmentType(AttachmentType):
    def __init__(self, sysType=None, description="", owner=None, text="", index=None, specifierValue="", categoryTree="", allowedValues=""):
        super().__init__(sysType, description)
        self.owner = owner
        self.text = text
        self.index = index
        self.specifierValue = specifierValue
        self.categoryTree = categoryTree
        self.allowedValues = allowedValues

class BartAttachmentType(MetadataAttachmentType):
    def __init__(self, sysType=None, description=""):
        super().__init__(sysType, description)

class BartSpecifierType(BartAttachmentType):
    def __init__(self, sysType=None, description=""):
        super().__init__(sysType, description)

class BartQualifierType(BartAttachmentType):
    def __init__(self, sysType=None, description=""):
        super().__init__(sysType, description)

class BartMetadataType(MetadataType):
    def __init__(self, sysType=None, description="", bartFullName="", carbonSource="", carbonSourceLifecycle="", activityDescription="", measuredQuantity="", measuredQuantityType="", mqDescription="", mqAbbreviation="", unitAllowedValues="", specifiers=None, qualifiers=None):
        super().__init__(sysType, description)
        self.bartFullName = bartFullName
        self.carbonSource = carbonSource
        self.carbonSourceLifecycle = carbonSourceLifecycle
        self.activityDescription = activityDescription
        self.measuredQuantity = measuredQuantity
        self.measuredQuantityType = measuredQuantityType
        self.mqDescription = mqDescription
        self.mqAbbreviation = mqAbbreviation
        self.unitAllowedValues = unitAllowedValues
        self.specifiers = specifiers or []
        self.qualifiers = qualifiers or []

    def add_specifier(self, specifier):
        self.specifiers.append(specifier)

    def add_qualifier(self, qualifier):
        self.qualifiers.append(qualifier)

class AdditionalVariableType(AttachmentType):
    def __init__(self, sysType=None, description="", avName="", cvtId="", owner=None):
        super().__init__(sysType, description)
        self.avName = avName
        self.cvtId = cvtId
        self.owner = owner

class DmMetadataType(MetadataType):
    def __init__(self, sysType=None, description="", dmType="", formula="", notations="", additionalVariables="", dmPref=None, condition1="", condition2="", condition3="", notes="", variables=None):
        super().__init__(sysType, description)
        self.dmType = dmType
        self.formula = formula
        self.notations = notations
        self.additionalVariables = additionalVariables
        self.dmPref = dmPref
        self.condition1 = condition1
        self.condition2 = condition2
        self.condition3 = condition3
        self.notes = notes
        self.variables = variables or []

    def add_variable(self, variable):
        self.variables.append(variable)

class EatAttachmentType(MetadataAttachmentType):
    def __init__(self, sysType=None, description=""):
        super().__init__(sysType, description)

class EatSpecifierType(EatAttachmentType):
    def __init__(self, sysType=None, description=""):
        super().__init__(sysType, description)

class EatQualifierType(EatAttachmentType):
    def __init__(self, sysType=None, description=""):
        super().__init__(sysType, description)

class EatMetadataType(MetadataType):
    def __init__(self, sysType=None, description="", eatName="", eatFullName="", ghgAmFullName="", ghgAmName="", mdDescription="", methodologyName="", carbonSource="", action="", activityDescription="", reportedQuantity="", rqDescription="", rqAbbreviation="", eaDataSource="", specifiers=None, qualifiers=None):
        super().__init__(sysType, description)
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
        self.specifiers = specifiers or []
        self.qualifiers = qualifiers or []

    def add_specifier(self, specifier):
        self.specifiers.append(specifier)

    def add_qualifier(self, qualifier):
        self.qualifiers.append(qualifier)
    
class GhgAmMetadataType(MetadataType):
    def __init__(self, sysType=None, description="", ghgAmName="", ghgAMFullName="", operationalScope="", processScope=""):
        super().__init__(sysType, description)
        self.ghgAmName = ghgAmName
        self.ghgAMFullName = ghgAMFullName
        self.operationalScope = operationalScope
        self.processScope = processScope

class GhgAmEatMappingType(AttachmentType):
    def __init__(self, sysType=None, description="", ghgAm=None, ghgAMFullName="", eat=None, eatFullName=""):
        super().__init__(sysType, description)
        self.ghgAm = ghgAm
        self.ghgAMFullName = ghgAMFullName
        self.eat = eat
        self.eatFullName = eatFullName

class PodGhgAmMappingType(AttachmentType):
    def __init__(self, sysType=None, description="", owner=None, ghgAMFullName="", suppressedDmList=""):
        super().__init__(sysType, description)
        self.owner = owner
        self.ghgAMFullName = ghgAMFullName
        self.suppressedDmList = suppressedDmList

class MetadataAnnotationType(AttachmentType):
    def __init__(self, sysType=None, description="", owner=None, metadataId="", metadataType="", bartUsedNames="", bartSpecifierValues="", methodDescription="", podName="", ghgAmFullName="", eatFullName="", dmId="", bartFullName="", suppressedDm=False, ghgAMReq="", operationalScope="", processScope="", methodAnnotation="", bartUsedNamesBot="", bartSpecifierValuesBot=""):
        super().__init__(sysType, description)
        self.owner = owner
        self.metadataId = metadataId
        self.metadataType = metadataType
        self.bartUsedNames = bartUsedNames
        self.bartSpecifierValues = bartSpecifierValues
        self.methodDescription = methodDescription
        self.podName = podName
        self.ghgAmFullName = ghgAmFullName
        self.eatFullName = eatFullName
        self.dmId = dmId
        self.bartFullName = bartFullName
        self.suppressedDm = suppressedDm
        self.ghgAMReq = ghgAMReq
        self.operationalScope = operationalScope
        self.processScope = processScope
        self.methodAnnotation = methodAnnotation
        self.bartUsedNamesBot = bartUsedNamesBot
        self.bartSpecifierValuesBot = bartSpecifierValuesBot

class PodMetadataType(MetadataType):
    def __init__(self, sysType=None, description="", carbonSource="", podName="", customer='Atomiton', podCategory="", usability="", domainInformation="", image="", countrySpecific="", referenceYear="", ghgAms=None, descriptions=None):
        super().__init__(sysType, description)
        self.carbonSource = carbonSource
        self.podName = podName
        self.customer = customer
        self.podCategory = podCategory
        self.usability = usability
        self.domainInformation = domainInformation
        self.image = image
        self.countrySpecific = countrySpecific
        self.referenceYear = referenceYear
        self.ghgAms = ghgAms or []
        self.descriptions = descriptions or []

    def add_ghg_am(self, ghg_am):
        self.ghgAms.append(ghg_am)

    def add_description(self, description):
        self.descriptions.append(description)

class BotPodMappingType(AttachmentType):
    def __init__(self, sysType=None, description="", owner=None, podName="", customer='Atomiton', podReq=""):
        super().__init__(sysType, description)
        self.owner = owner
        self.podName = podName
        self.customer = customer
        self.podReq = podReq

class BotMetadataType(MetadataType):
    def __init__(self, sysType=None, description="", botName="", botId="", botType="", botIndex="", botDescription="", domainInformation="", image="", longDescription="", summary="", commonEquipment="", commonProcesses="", commonOperations="", customer='Atomiton', eatId="", descriptions=None, pods=None):
        super().__init__(sysType, description)
        self.botName = botName
        self.botId = botId
        self.botType = botType
        self.botIndex = botIndex
        self.botDescription = botDescription
        self.domainInformation = domainInformation
        self.image = image
        self.longDescription = longDescription
        self.summary = summary
        self.commonEquipment = commonEquipment
        self.commonProcesses = commonProcesses
        self.commonOperations = commonOperations
        self.customer = customer
        self.eatId = eatId
        self.descriptions = descriptions or []
        self.pods = pods or []

    def add_description(self, description):
        self.descriptions.append(description)

    def add_pod(self, pod):
        self.pods.append(pod)

class DmBartEatMappingType(AttachmentType):
    def __init__(self, sysType=None, description="", eatId="", dmId="", pref=None, bartId=""):
        super().__init__(sysType, description)
        self.eatId = eatId
        self.dmId = dmId
        self.pref = pref
        self.bartId = bartId


#Data Models
class BartMetadata(BartMetadataType):
    def __init__(self, sysType=None, description="", bartFullName="", carbonSource="", carbonSourceLifecycle="", activityDescription="", measuredQuantity="", measuredQuantityType="", mqDescription="", mqAbbreviation="", unitAllowedValues="", specifiers=None, qualifiers=None):
        super().__init__(sysType, description, bartFullName, carbonSource, carbonSourceLifecycle, activityDescription, measuredQuantity, measuredQuantityType, mqDescription, mqAbbreviation, unitAllowedValues, specifiers, qualifiers)

class DmMetadata(DmMetadataType):
    def __init__(self, sysType=None, description="", dmType="", formula="", notations="", additionalVariables="", dmPref=None, condition1="", condition2="", condition3="", notes="", variables=None):
        super().__init__(sysType, description, dmType, formula, notations, additionalVariables, dmPref, condition1, condition2, condition3, notes, variables)

class EatMetadata(EatMetadataType):
    def __init__(self, sysType=None, description="", eatName="", eatFullName="", ghgAmFullName="", ghgAmName="", mdDescription="", methodologyName="", carbonSource="", action="", activityDescription="", reportedQuantity="", rqDescription="", rqAbbreviation="", eaDataSource="", specifiers=None, qualifiers=None):
        super().__init__(sysType, description, eatName, eatFullName, ghgAmFullName, ghgAmName, mdDescription, methodologyName, carbonSource, action, activityDescription, reportedQuantity, rqDescription, rqAbbreviation, eaDataSource, specifiers, qualifiers)

class PodMetadata(PodMetadataType):
    def __init__(self, sysType=None, description="", carbonSource="", podName="", customer='Atomiton', podCategory="", usability="", domainInformation="", image="", countrySpecific="", referenceYear="", ghgAms=None, descriptions=None):
        super().__init__(sysType, description, carbonSource, podName, customer, podCategory, usability, domainInformation, image, countrySpecific, referenceYear, ghgAms, descriptions)

class BotMetadata(BotMetadataType):
    def __init__(self, sysType=None, description="", botName="", botId="", botType="", botIndex="", botDescription="", domainInformation="", image="", longDescription="", summary="", commonEquipment="", commonProcesses="", commonOperations="", customer='Atomiton', eatId="", descriptions=None, pods=None):
        super().__init__(sysType, description, botName, botId, botType, botIndex, botDescription, domainInformation, image, longDescription, summary, commonEquipment, commonProcesses, commonOperations, customer, eatId, descriptions, pods)

class MetadataAttachment(MetadataAttachmentType):
    def __init__(self, sysType=None, description="", owner=None, text="", index=None, specifierValue="", categoryTree="", allowedValues=""):
        super().__init__(sysType, description, owner, text, index, specifierValue, categoryTree, allowedValues)

class BartSpecifier(BartSpecifierType, MetadataAttachment):
    def __init__(self, sysType=None, description="", owner=None, text="", index=None, specifierValue="", categoryTree="", allowedValues=""):
        BartSpecifierType.__init__(self, sysType, description)
        MetadataAttachment.__init__(self, sysType, description, owner, text, index, specifierValue, categoryTree, allowedValues)

class BartQualifier(BartQualifierType, MetadataAttachment):
    def __init__(self, sysType=None, description="", owner=None, text="", index=None, specifierValue="", categoryTree="", allowedValues=""):
        BartQualifierType.__init__(self, sysType, description)
        MetadataAttachment.__init__(self, sysType, description, owner, text, index, specifierValue, categoryTree, allowedValues)

class EatSpecifier(EatSpecifierType, MetadataAttachment):
    def __init__(self, sysType=None, description="", owner=None, text="", index=None, specifierValue="", categoryTree="", allowedValues=""):
        EatSpecifierType.__init__(self, sysType, description)
        MetadataAttachment.__init__(self, sysType, description, owner, text, index, specifierValue, categoryTree, allowedValues)

class EatQualifier(EatQualifierType, MetadataAttachment):
    def __init__(self, sysType=None, description="", owner=None, text="", index=None, specifierValue="", categoryTree="", allowedValues=""):
        EatQualifierType.__init__(self, sysType, description)
        MetadataAttachment.__init__(self, sysType, description, owner, text, index, specifierValue, categoryTree, allowedValues)

# Classes to be completed
class AdditionalVariable(AdditionalVariableType, MetadataAttachment):
    def __init__(self, sysType=None, description="", owner=None, text="", index=None, specifierValue="", categoryTree="", allowedValues=""):
        AdditionalVariableType.__init__(self, sysType, description, avName="", cvtId="", owner=owner)
        MetadataAttachment.__init__(self, sysType, description, owner, text, index, specifierValue, categoryTree, allowedValues)

class GhgAmMetadata(GhgAmMetadataType):
    def __init__(self, sysType=None, description="", ghgAmName="", ghgAMFullName="", operationalScope="", processScope=""):
        super().__init__(sysType, description, ghgAmName, ghgAMFullName, operationalScope, processScope)
# Example usage
# Import necessary modules
# Assuming the classes are defined in a file named `data_models.py`
# from data_models import AttachmentType, TreeCategoryNodeType, MetadataType, MetadataAttachmentType, BartAttachmentType, BartSpecifierType, BartQualifierType, BartMetadataType, AdditionalVariableType, DmMetadataType, EatAttachmentType, EatSpecifierType, EatQualifierType, EatMetadataType, PodGhgAmMappingType, MetadataAnnotationType, PodMetadataType, BotPodMappingType, BotMetadataType, DmBartEatMappingType, BartMetadata, DmMetadata, EatMetadata, PodMetadata, BotMetadata, MetadataAttachment, BartSpecifier, BartQualifier, EatSpecifier, EatQualifier, AdditionalVariable, GhgAmMetadata
# Example usage
def main():
    # Create instances of each class
    bart_metadata = BartMetadata(
        sysType=1,
        description="Bart Metadata Example",
        bartFullName="Bart Full Name",
        carbonSource="Carbon Source",
        carbonSourceLifecycle="Lifecycle",
        activityDescription="Activity Description",
        measuredQuantity="Measured Quantity",
        measuredQuantityType="Measured Quantity Type",
        mqDescription="MQ Description",
        mqAbbreviation="MQ Abbreviation",
        unitAllowedValues="Unit Allowed Values"
    )

    dm_metadata = DmMetadata(
        sysType=2,
        description="DM Metadata Example",
        dmType="DM Type",
        formula="Formula",
        notations="Notations",
        additionalVariables="Additional Variables",
        dmPref=1,
        condition1="Condition 1",
        condition2="Condition 2",
        condition3="Condition 3",
        notes="Notes"
    )

    eat_metadata = EatMetadata(
        sysType=3,
        description="EAT Metadata Example",
        eatName="Eat Name",
        eatFullName="Eat Full Name",
        ghgAmFullName="GHG AM Full Name",
        ghgAmName="GHG AM Name",
        mdDescription="MD Description",
        methodologyName="Methodology Name",
        carbonSource="Carbon Source",
        action="Action",
        activityDescription="Activity Description",
        reportedQuantity="Reported Quantity",
        rqDescription="RQ Description",
        rqAbbreviation="RQ Abbreviation",
        eaDataSource="EA Data Source"
    )

    pod_metadata = PodMetadata(
        sysType=4,
        description="POD Metadata Example",
        carbonSource="Carbon Source",
        podName="Pod Name",
        customer="Atomiton",
        podCategory="Pod Category",
        usability="Usability",
        domainInformation="Domain Information",
        image="Image",
        countrySpecific="Country Specific",
        referenceYear="Reference Year"
    )

    bot_metadata = BotMetadata(
        sysType=5,
        description="BOT Metadata Example",
        botName="Bot Name",
        botId="Bot ID",
        botType="Bot Type",
        botIndex="Bot Index",
        botDescription="Bot Description",
        domainInformation="Domain Information",
        image="Image",
        longDescription="Long Description",
        summary="Summary",
        commonEquipment="Common Equipment",
        commonProcesses="Common Processes",
        commonOperations="Common Operations",
        customer="Atomiton",
        eatId="EAT ID"
    )

    # Adding relationships
    bart_specifier = BartSpecifier(
        sysType=6,
        description="Bart Specifier",
        owner=bart_metadata,
        text="Specifier Text",
        index=1,
        specifierValue="Specifier Value",
        categoryTree="Category Tree",
        allowedValues="Allowed Values"
    )

    bart_qualifier = BartQualifier(
        sysType=7,
        description="Bart Qualifier",
        owner=bart_metadata,
        text="Qualifier Text",
        index=1,
        specifierValue="Qualifier Value",
        categoryTree="Category Tree",
        allowedValues="Allowed Values"
    )

    eat_specifier = EatSpecifier(
        sysType=8,
        description="Eat Specifier",
        owner=eat_metadata,
        text="Specifier Text",
        index=1,
        specifierValue="Specifier Value",
        categoryTree="Category Tree",
        allowedValues="Allowed Values"
    )

    eat_qualifier = EatQualifier(
        sysType=9,
        description="Eat Qualifier",
        owner=eat_metadata,
        text="Qualifier Text",
        index=1,
        specifierValue="Qualifier Value",
        categoryTree="Category Tree",
        allowedValues="Allowed Values"
    )

    bart_metadata.add_specifier(bart_specifier)
    bart_metadata.add_qualifier(bart_qualifier)
    eat_metadata.add_specifier(eat_specifier)
    eat_metadata.add_qualifier(eat_qualifier)

    # Adding GHG AMs to POD
    ghg_am_metadata = GhgAmMetadata(
        sysType=10,
        description="GHG AM Metadata Example",
        ghgAmName="GHG AM Name",
        ghgAMFullName="GHG AM Full Name",
        operationalScope="Operational Scope",
        processScope="Process Scope"
    )

    pod_metadata.add_ghg_am(ghg_am_metadata)

    # Adding Additional Variables to DMs
    additional_variable = AdditionalVariable(
        sysType=11,
        description="Additional Variable Example",
        owner=dm_metadata,
        text="Additional Variable Text",
        index=1,
        specifierValue="Specifier Value",
        categoryTree="Category Tree",
        allowedValues="Allowed Values"
    )

    dm_metadata.add_variable(additional_variable)

    # Print the objects to verify
    print("Bart Metadata:", vars(bart_metadata))
    print("DM Metadata:", vars(dm_metadata))
    print("EAT Metadata:", vars(eat_metadata))
    print("POD Metadata:", vars(pod_metadata))
    print("BOT Metadata:", vars(bot_metadata))

    print("\nBart Specifiers and Qualifiers:")
    for specifier in bart_metadata.specifiers:
        print(vars(specifier))
    for qualifier in bart_metadata.qualifiers:
        print(vars(qualifier))

    print("\nEat Specifiers and Qualifiers:")
    for specifier in eat_metadata.specifiers:
        print(vars(specifier))
    for qualifier in eat_metadata.qualifiers:
        print(vars(qualifier))

    print("\nGHG AMs in POD Metadata:")
    for ghg_am in pod_metadata.ghgAms:
        print(vars(ghg_am))

    print("\nAdditional Variables in DM Metadata:")
    for variable in dm_metadata.variables:
        print(vars(variable))

if __name__ == "__main__":
    main()




