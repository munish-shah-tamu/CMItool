class AttachmentType:
    def __init__(self, sysType=None, description=""):
        self.sysType = sysType or self.default_sysType()
        self.description = description

    def default_sysType(self):
        return 0  # Replace with appropriate default value

class NameInfoFacet:
    def __init__(self, name=""):
        self.name = name

class CategorizedType:
    def __init__(self, category=""):
        self.category = category

class TreeNodeFacet:
    def __init__(self, treeLabel="", begQLabel="", owner=None):
        self.treeLabel = treeLabel
        self.begQLabel = begQLabel
        self.owner = owner

class TreeCategoryNodeType:
    def __init__(self, sysType=None, description=""):
        self.sysType = sysType or self.default_sysType()
        self.description = description

    def default_sysType(self):
        return 0  # Replace with appropriate default value

class MetadataType(TreeCategoryNodeType):
    def __init__(self, sysType=None, description=""):
        super().__init__(sysType, description)

class NamedAttachmentType(AttachmentType, NameInfoFacet):
    def __init__(self, sysType=None, description="", name=""):
        AttachmentType.__init__(self, sysType, description)
        NameInfoFacet.__init__(self, name)

class CategorizedAttachmentType(NamedAttachmentType, CategorizedType):
    def __init__(self, sysType=None, description="", name="", category=""):
        NamedAttachmentType.__init__(self, sysType, description, name)
        CategorizedType.__init__(self, category)

class TreeNodeAttachmentType(AttachmentType, TreeNodeFacet):
    def __init__(self, sysType=None, description="", treeLabel="", begQLabel="", owner=None):
        AttachmentType.__init__(self, sysType, description)
        TreeNodeFacet.__init__(self, treeLabel, begQLabel, owner)
        self.unique_tree_node()

    def unique_tree_node(self):
        if self.treeLabel and self.begQLabel and self.owner:
            self.uTreeNode = f"{self.treeLabel},{self.begQLabel},{self.owner}"
        else:
            self.uTreeNode = None

class DtMetadataType(MetadataType):
    def __init__(self, sysType=None, description="", format="", country="", language="", bartId=""):
        super().__init__(sysType, description)
        self.format = format
        self.country = country
        self.language = language
        self.bartId = bartId

class EaMetadataType(MetadataType):
    def __init__(self, sysType=None, description="", eatId="", eaId="", referenceYear=None, primaryCountry="", secondaryCountry="", notForCountry="", dataQuality="", efDataSource="", eaDataSourceDetail="", extendedData=False, specifiers=None, factors=None):
        super().__init__(sysType, description)
        self.eatId = eatId
        self.eaId = eaId
        self.referenceYear = referenceYear
        self.primaryCountry = primaryCountry
        self.secondaryCountry = secondaryCountry
        self.notForCountry = notForCountry
        self.dataQuality = dataQuality
        self.efDataSource = efDataSource
        self.eaDataSourceDetail = eaDataSourceDetail
        self.extendedData = extendedData
        self.specifiers = specifiers or []
        self.factors = factors or []

class EatMetadataType(MetadataType):
    def __init__(self, sysType=None, description="", specifiers=None, qualifiers=None, eatName="", eatFullName="", ghgAmFullName="", ghgAmName="", mdDescription="", methodologyName="", carbonSource="", action="", activityDescription="", reportedQuantity="", rqDescription="", rqAbbreviation="", eaDataSource=""):
        super().__init__(sysType, description)
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

class BartMetadataType(MetadataType):
    def __init__(self, sysType=None, description="", specifiers=None, qualifiers=None, bartFullName="", carbonSource="", carbonSourceLifecycle="", activityDescription="", measuredQuantity="", measuredQuantityType="", mqDescription="", mqAbbreviation="", unitAllowedValues=""):
        super().__init__(sysType, description)
        self.specifiers = specifiers or []
        self.qualifiers = qualifiers or []
        self.bartFullName = bartFullName
        self.carbonSource = carbonSource
        self.carbonSourceLifecycle = carbonSourceLifecycle
        self.activityDescription = activityDescription
        self.measuredQuantity = measuredQuantity
        self.measuredQuantityType = measuredQuantityType
        self.mqDescription = mqDescription
        self.mqAbbreviation = mqAbbreviation
        self.unitAllowedValues = unitAllowedValues

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

class MethodologyType(MetadataType):
    def __init__(self, sysType=None, description="", releaseYear=None, referenceYear=None, systemPreference=None, status='active'):
        super().__init__(sysType, description)
        self.releaseYear = releaseYear
        self.referenceYear = referenceYear
        self.systemPreference = systemPreference
        self.status = status

class CvtMetadataType(MetadataType):
    def __init__(self, sysType=None, description="", specifiers=None, qualifiers=None, cvtSourceName="", cvtSourceDescription="", cvtID="", cvtName="", cvtType="", cvtUsageDescription="", cfName="", conversionFactorDescription="", inputQuantityDescription="", inputQuantityUnitClass="", outputQuantityDescription="", outputQuantityUnitClass=""):
        super().__init__(sysType, description)
        self.specifiers = specifiers or []
        self.qualifiers = qualifiers or []
        self.cvtSourceName = cvtSourceName
        self.cvtSourceDescription = cvtSourceDescription
        self.cvtID = cvtID
        self.cvtName = cvtName
        self.cvtType = cvtType
        self.cvtUsageDescription = cvtUsageDescription
        self.cfName = cfName
        self.conversionFactorDescription = conversionFactorDescription
        self.inputQuantityDescription = inputQuantityDescription
        self.inputQuantityUnitClass = inputQuantityUnitClass
        self.outputQuantityDescription = outputQuantityDescription
        self.outputQuantityUnitClass = outputQuantityUnitClass

class CfMetadataType(AttachmentType):
    def __init__(self, sysType=None, description="", cvtID="", cfId="", cfName="", specifier1Name="", specifier1Value="", cfValue=None, inputQuantityUnit="", outputQuantityUnit=""):
        super().__init__(sysType, description)
        self.cvtID = cvtID
        self.cfId = cfId
        self.cfName = cfName
        self.specifier1Name = specifier1Name
        self.specifier1Value = specifier1Value
        self.cfValue = cfValue
        self.inputQuantityUnit = inputQuantityUnit
        self.outputQuantityUnit = outputQuantityUnit

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

class BotPodMappingType(AttachmentType):
    def __init__(self, sysType=None, description="", owner=None, podName="", customer='Atomiton', podReq=""):
        super().__init__(sysType, description)
        self.owner = owner
        self.podName = podName
        self.customer = customer
        self.podReq = podReq

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

class MetadataAttachmentType(AttachmentType):
    def __init__(self, sysType=None, description="", owner=None, text="", index=None, specifierValue="", categoryTree="", allowedValues=""):
        super().__init__(sysType, description)
        self.owner = owner
        self.text = text
        self.index = index
        self.specifierValue = specifierValue
        self.categoryTree = categoryTree
        self.allowedValues = allowedValues

class EatAttachmentType(MetadataAttachmentType):
    def __init__(self, sysType=None, description=""):
        super().__init__(sysType, description)

class EatSpecifierType(EatAttachmentType):
    def __init__(self, sysType=None, description=""):
        super().__init__(sysType, description)

class EatQualifierType(EatAttachmentType):
    def __init__(self, sysType=None, description=""):
        super().__init__(sysType, description)

class BartAttachmentType(MetadataAttachmentType):
    def __init__(self, sysType=None, description=""):
        super().__init__(sysType, description)

class BartSpecifierType(BartAttachmentType):
    def __init__(self, sysType=None, description=""):
        super().__init__(sysType, description)

class BartQualifierType(BartAttachmentType):
    def __init__(self, sysType=None, description=""):
        super().__init__(sysType, description)

class EaAttachmentType(MetadataAttachmentType):
    def __init__(self, sysType=None, description=""):
        super().__init__(sysType, description)

class EaSpecifierType(EaAttachmentType):
    def __init__(self, sysType=None, description=""):
        super().__init__(sysType, description)

class EaQualifierType(EaAttachmentType):
    def __init__(self, sysType=None, description=""):
        super().__init__(sysType, description)

class CvtAttachmentType(MetadataAttachmentType):
    def __init__(self, sysType=None, description=""):
        super().__init__(sysType, description)

class CvtSpecifierType(CvtAttachmentType):
    def __init__(self, sysType=None, description=""):
        super().__init__(sysType, description)

class CvtQualifierType(CvtAttachmentType):
    def __init__(self, sysType=None, description=""):
        super().__init__(sysType, description)

class DmBartEatMappingType(AttachmentType):
    def __init__(self, sysType=None, description="", eatId="", dmId="", pref=None, bartId=""):
        super().__init__(sysType, description)
        self.eatId = eatId
        self.dmId = dmId
        self.pref = pref
        self.bartId = bartId

class AdditionalVariableType(AttachmentType):
    def __init__(self, sysType=None, description="", avName="", cvtId="", owner=None):
        super().__init__(sysType, description)
        self.avName = avName
        self.cvtId = cvtId
        self.owner = owner

class UnitType:
    def __init__(self, unitName="", unitSymbol="", unitType=""):
        self.unitName = unitName
        self.unitSymbol = unitSymbol
        self.unitType = unitType

class UnitConversionType:
    def __init__(self, fromUnit="", toUnit="", conversionFactor=1.0):
        self.fromUnit = fromUnit
        self.toUnit = toUnit
        self.conversionFactor = conversionFactor

class ConversionFactorType:
    def __init__(self, factorName="", factorValue=1.0):
        self.factorName = factorName
        self.factorValue = factorValue

class EmissionFactorType:
    def __init__(self, activityType="", emissionFactor=1.0):
        self.activityType = activityType
        self.emissionFactor = emissionFactor

class ModelEntryStatusType:
    def __init__(self, statusName="", statusDescription=""):
        self.statusName = statusName
        self.statusDescription = statusDescription

class ColumnsOrderType:
    def __init__(self, columnName="", orderIndex=0):
        self.columnName = columnName
        self.orderIndex = orderIndex

class Unit(UnitType):
    pass

class UnitConversion(UnitConversionType):
    pass

class ConversionFactor(ConversionFactorType):
    pass

class EmissionFactor(EmissionFactorType):
    pass

class ModelEntryStatus(ModelEntryStatusType):
    pass

class ColumnsOrder(ColumnsOrderType):
    pass
       
