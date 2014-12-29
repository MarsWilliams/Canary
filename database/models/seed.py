import csv
from model import *
from run import session, createTables

#

def fixString(str):
    str = str.strip('~').decode('latin-1').encode('utf-8')
    if not str:
        return None
    return str

def stripTilde(table):
    for row in table:
        yield [fixString(str) for str in row]

createTables()



print "Importing Food Descriptions"
with open('data/USDA/FOOD_DES.txt', 'rb') as food_des_file:
    foodGrpQuery = session.query(FoodGroupDescription)
    utility_csv  = csv.reader(food_des_file, delimiter='^')
    for row in stripTilde(utility_csv):

        food_description = FoodDescription()
        
        food_description.id = row[0]
        food_description.foodGroup_id = row[1]
        food_description.longDesc = row[2]
        food_description.shrtDesc = row[3]
        food_description.commonName = row[4]
        food_description.manufactureName = row[5]

        if row[6]:
            survey = True
        else:
            survey = False
        food_description.survey = survey

        food_description.refuseDescription = row[7]
        food_description.refuse = (row[8])
        food_description.sciName = row[9]
        food_description.nitrogenFactor = (row[10])
        food_description.proteinFactor = (row[11])
        food_description.fatFactor = (row[12])
        food_description.carbohydrateFactor = (row[13])

        session.add(food_description)

print "Importing Food Group Descriptions"
with open('data/USDA/FD_GROUP.txt', 'rb') as fd_group_file:
    utility_csv  = csv.reader(fd_group_file, delimiter='^')
    for row in stripTilde(utility_csv):
        
        food_group = FoodGroupDescription()

        food_group.id = row[0]
        food_group.description = row[1]
        
        session.add(food_group)

session.commit()



print "Importing LanguaL Factors Descriptions"
with open('data/USDA/LANGDESC.txt', 'rb') as langdesc_file:
    utility_csv  = csv.reader(langdesc_file, delimiter='^')
    for row in stripTilde(utility_csv):
        
        langdesc = LanguaLFactorsDescription()

        langdesc.id = row[0]
        langdesc.description = row[1]
        
        session.add(langdesc)

session.commit()



with open('data/USDA/NUT_DATA.txt', 'rb') as nut_data_file:
    dataSrcQuery = session.query(SourcesOfData)
    print "Importing Nutrient Data"
    utility_csv  = csv.reader(nut_data_file, delimiter='^')
    i = 0
    for row in stripTilde(utility_csv):
        i = i+1
        print i
        
        nuttrient = NutrientData()

        nutrient.id = row[0]
        nutrient.food_id = row[1]
        nutrient.nutr_Val = row[2]
        nutrient.num_Data_Pts = row[3]
        nutrient.std_Error = row[4]
        nutrient.src_Cd_id = row[5]
        nutrient.deriv_Cd_id = row[6]
        nutrient.ref_id = row[7]

        if row[8]:
            nutr_mark = True
        else:
            nutr_mark = False
            nutrient.add_Nutr_Mark = nutr_mark

        nutrient.num_Studies = row[9]
        nutrient.minVal = row[10]
        nutrient.maxVal = row[11]
        nutrient.dF = row[12]
        nutrient.low_EB = row[13]
        nutrient.up_EB = row[14]
        nutrient.stat_cmt = row[15]
        nutrient.addMod_Date = row[16]
        nutrient.cC = row[17]

        dataSource = dataSrcQuery.filter_by(id = row[7]).first()
        if dataSource:
            nutrient.dataSource = dataSource

        session.add(nutrient)

session.commit()



print "Importing Nutrient Definitions"
with open('data/USDA/NUTR_DEF.txt', 'rb') as nutr_def_file:
    utility_csv  = csv.reader(nutr_def_file, delimiter='^')
    for row in stripTilde(utility_csv):
        
        nutr_definition = NutrientDefinition()

        nutr_definition.id = row[0]
        nutr_definition.units = row[1]
        nutr_definition.tagname = row[2]
        nutr_definition.nutrDesc = row[3]
        nutr_definition.num_Dec = row[4]
        nutr_definition.sR_Order = row[5]
        
        session.add(nutr_definition)

session.commit()



print "Importing Source Codes"
with open('data/USDA/SRC_CD.txt', 'rb') as src_cd_file:
    utility_csv  = csv.reader(src_cd_file, delimiter='^')
    for row in stripTilde(utility_csv):
        
        src_cd = SourceCode()

        src_cd.id = row[0]
        src_cd.srcCd_Desc = row[1]
        
        session.add(src_cd)

session.commit()



print "Importing Data Derivation Code Descriptions"
with open('data/USDA/DERIV_CD.txt', 'rb') as deriv_cd_file:
    utility_csv  = csv.reader(deriv_cd_file, delimiter='^')
    for row in stripTilde(utility_csv):
        
        deriv_cd = DataDerivationCodeDescription()

        deriv_cd.id = row[0]
        deriv_cd.deriv_Desc = row[1]
        
        session.add(deriv_cd)

session.commit()



print "Importing Weights"
with open('data/USDA/WEIGHT.txt', 'rb') as weight_file:
    foodDesQuery = session.query(FoodDescription)

    utility_csv  = csv.reader(weight_file, delimiter='^')
    for row in stripTilde(utility_csv):
        
        weight = Weight()

        weight.food_id = row[0]
        weight.seq = row[1]
        weight.amount = row[2]
        weight.msre_Desc = row[3]
        weight.gm_Wgt = row[4]
        weight.num_Data_Pts = row[5]
        weight.std_Dev = row[6]

        session.add(weight)

session.commit()


print "Joining Food Descriptions and Langual tables"
with open('data/USDA/LANGUAL.txt', 'rb') as langual_file:
    langualQuery = session.query(LanguaLFactorsDescription)
    utility_csv  = csv.reader(langual_file, delimiter='^')
    for row in stripTilde(utility_csv):
        food_descriptions = foodDesQuery.filter_by(id = row[0]).first()
        langual = langualQuery.filter_by(id = row[1]).first()
        if food_descriptions and langual:
            food_descriptions.lang_desc.append(langual)

session.commit()

print "Importing Footnotes"
with open('data/USDA/FOOTNOTE.txt', 'rb') as footnote_file:
    utility_csv  = csv.reader(footnote_file, delimiter='^')
    for row in stripTilde(utility_csv):
        
        footnote = Footnote()
        footnote.id = row[0]
        footnote.footnt_No = row[1]
        footnote.footnt_Typ = row[2]
        footnote.nutr_No = row[3]
        footnote.footnt_Txt = row[4]
        
        session.add(footnote)

session.commit()



print "Importing Data Sources"
with open('data/USDA/DATA_SRC.txt', 'rb') as data_src_file:
    utility_csv  = csv.reader(data_src_file, delimiter='^')
    for row in stripTilde(utility_csv):
        
        data_src = SourcesOfData()

        data_src.id = row[0]
        data_src.authors = row[1]
        data_src.title = row[2]
        data_src.year = row[3]
        data_src.journal = row[4]
        data_src.vol_City = row[5]
        data_src.issue_State = row[6]
        data_src.start_Page = row[7]
        data_src.end_Page = row[8]
        
        session.add(data_src)

session.commit()