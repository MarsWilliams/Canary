from sqlalchemy import (Column, Integer, String, Numeric, Boolean, Float, ForeignKey, Table, create_engine)
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#hash 

# encoding utf-8

Base = declarative_base()

### Class declarations go here



# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True)
#     firstname = Column(String, nullable = False)
#     lastname = Column(String, nullable = False)
#     username = Column(String, nullable = False)
#     password = Column(String, nullable = False)
#     email = Column(String, nullable = False)
#     zipcode = Column(Integer, nullable = False)
#     salt =Column(String, nullable = False)

# class Photographs(Base):
#     __tablename__ = "photographs"
    
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable = False)
#     recipe_id = Column(Integer, ForeignKey('recipes.id'), nullable = False)

#     user = relationship("User",
#         backref=backref("photographs", order_by=id))

#     recipe = relationship("Recipe", 
#         backref=backref("recipes", order_by=id))

# class Rating(Base):
#     __tablename__ = "ratings"

#     id = Column(Integer, primary_key = True)
#     recipe_id = Column(Integer, ForeignKey('recipes.id'), nullable = False)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable = False)
#     rating = Column(Integer, nullable = True)

#     recipe = relationship("Recipe", 
#         backref=backref("ratings", order_by=id))

#     user = relationship("User",
#         backref=backref("ratings", order_by=id))


# class Recipe(Base):
#     __tablename__ = "recipes"
    
#     id = Column(Integer, primary_key=True)
#     url = Column(String, nullable=True)
#     name = Column(String, nullable=True)
#     description = Column(String, nullable=True)
#     image = Column(String, nullable=True)
#     servings = Column(String, nullable=True)
#     instructions = Column(String, nullable=True)
#     calories = Column(String, nullable=True)
#     fatContent = Column(String, nullable=True)
#     saturatedFatConent = Column(String, nullable=True)
#     cholesterolContent = Column(String, nullable=True)
#     carbohydrateContent = Column(String, nullable=True)
#     fiberContent = Column(String, nullable=True)
#     sugarContent = Column(String, nullable=True)
#     proteinContent = Column(String, nullable=True)
#     sodiumContent = Column(String, nullable=True)
#     keywords = Column(String, nullable=True)


# class RecipeIngredient(Base):
#     __tablename__ = "recipe_ingredients"
    
#     id = Column(Integer, primary_key = True)
#     recipe_id = Column(Integer, ForeignKey("recipes.id"), nullable = False)
#     food_id = Column(String, ForeignKey("food_descriptions.id"))
#     quantity = Column(Float, nullable = False)

#     food = relationship("FoodDescription",
#         backref=backref("food_descriptions", order_by=id))



### Association table for many-many relationships
langual_factor = Table('langual', Base.metadata,
                       Column('food_id', String(5),
                              ForeignKey('food_descriptions.id')), 
                       Column('lang_desc_id', String(5),
                              ForeignKey('lang_desc.id')))

class FoodDescription(Base):
    __tablename__ = 'food_descriptions'

    # 5-digit Nutrient Databank number that uniquely identifies a food item. If
    # this field is defined as numeric, the leading zero will be lost.
    id = Column(String(5), primary_key = True)
    # 4-digit code indicating food group to which a food item belongs.
    foodGroup_id = Column(String(4), ForeignKey('food_groups.id'))
    # 200-character description of food item.
    longDesc = Column(String(200), nullable = False)
    # 60-character abbreviated description of food item. Generated from the
    # 200-character description using abbreviations in Appendix A. If short
    # description is longer than 60 characters, additional abbreviations are
    # made.
    shrtDesc = Column(String(60), nullable = False)
    # Other names commonly used to describe a food, including local or regional
    # names for various foods, for example, soda or pop for carbonated
    # beverages.
    commonName = Column(String(100), nullable = True)
    # Indicates the company that manufactured the product, when appropriate.
    manufactureName = Column(String(65), nullable = True)
    # Indicates if the food item is used in the USDA Food and Nutrient Database
    # for Dietary Studies (FNDDS) and thus has a complete nutrient profile for
    # the 65 FNDDS nutrients.
    survey = Column(Boolean, nullable = True)
    # Description of inedible parts of a food item (refuse), such as seeds or
    # bone.
    refuseDescription = Column(String(135), nullable = True)
    # Percentage of refuse.
    refuse = Column(Integer, nullable = True)
    # Scientific name of the food item. Given for the least processed form of
    # the food (usually raw), if applicable.
    sciName = Column(String(65), nullable = True)
    # Factor for converting nitrogen to protein (see p. 11).
    nitrogenFactor = Column(Numeric(4,2), nullable = True)
    # Factor for calculating calories from protein (see p. 12).
    proteinFactor = Column(Numeric(4,2), nullable = True)
    # Factor for calculating calories from fat (see p. 12).
    fatFactor = Column(Numeric(4,2), nullable = True)
    # Factor for calculating calories from carbohydrate (see p. 12).
    carbohydrateFactor = Column(Numeric(4,2), nullable = True)

    food_descriptions = relationship("FoodGroupDescription", backref = "food_descriptions", order_by = id)
    nutrients = relationship("NutrientData", backref="food_descriptions", order_by = id)
    footnotes = relationship("Footnote", backref="food_descriptions", order_by = id)

class FoodGroupDescription(Base):
    __tablename__ = 'food_groups'
    
    # 4-digit code identifying a food group. Only the first 2 digits are
    # currently assigned. In the future, the last 2 digits may be used. Codes
    # may not be consecutive.
    id = Column(String(4), primary_key = True)
    # Name of food group.
    description = Column(String(60), nullable = False)

class LanguaLFactorsDescription(Base):
    __tablename__ = 'lang_desc'
    
    # The LanguaL factor from the Thesaurus. Only those codes used to factor the
    # foods contained in the LanguaL Factor file are included in this file
    id = Column(String(5), primary_key = True)
    # The description of the LanguaL Factor Code from the thesaurus
    description = Column(String(140), nullable = False)

    food_descriptions = relationship("FoodDescription", secondary = "langual", backref = "lang_desc")

class NutrientData(Base):
    __tablename__ = 'nutrients'

    id = Column(Integer, primary_key = True)
    # 5-digit Nutrient Databank number.
    food_id = Column(String(5), ForeignKey('food_descriptions.id'))
    # Unique 3-digit identifier code for a nutrient 
    nutrient_definitions_id = Column(String(3), ForeignKey('nutrient_definitions.id'))
    # Amount in 100 grams, edible portion 
    nutr_Val = Column(Numeric(10,3), nullable = False)
    # Number of data points (previously called Sample_Ct) is the number of
    # analyses used to calculate the nutrient value. If the number of data
    # points is 0, the value was calculated or imputed.
    num_Data_Pts = Column(Numeric(5,0), nullable = False)
    # Standard error of the mean. Null if cannot be calculated. The standard
    # error is also not given if the number of data points is less than three.
    std_Error = Column(Numeric(8,3), nullable = True)
    # Code indicating type of data.
    src_Cd_id = Column(String(2), ForeignKey('src_cds.id'))
    # Data Derivation Code giving specific information on how the value is
    # determined
    deriv_Cd_id = Column(String(4), ForeignKey('deriv_cd.id'))
    # NDB number of the item used to impute a missing value. Populated only for
    # items added or updated starting with SR14.
    ref_id = Column(String(5), nullable = True)
    # Indicates a vitamin or mineral added for fortification or enrichment. This
    # field is populated for ready-to-eat breakfast cereals and many brand-name
    # hot cereals in food group 8.
    add_Nutr_Mark = Column(Boolean, nullable = True)
    # Number of studies
    num_Studies = Column(Integer, nullable = True)
    # Minimum values
    minVal = Column(Numeric(10,3), nullable = True)
    # Maximum value
    maxVal = Column(Numeric(10,3), nullable = True)
    # Degrees of freedom
    dF = Column(Integer, nullable = True)
    # Lower 95% error bound
    low_EB = Column(Numeric(10,3), nullable = True)
    # Upper 95% error bound
    up_EB = Column(Numeric(10,3), nullable = True)
    # Statistical comments
    stat_cmt = Column(String(10), nullable = True)
    # Indicates when a value was either added to the database or last modified.
    addMod_Date = Column(String(10), nullable = True)
    # Confidence Code indicating data quality, based on evaluation of sample
    # plan, sample handling, analytical method, analytical quality control, and
    # number of samples analyzed. Not included in this release, but is planned
    # for future releases.
    cC = Column(String(1), nullable = True)

    data_source_id = Column(String(6), ForeignKey('data_source.id'), nullable = True)

class NutrientDefinition(Base):
    __tablename__ = 'nutrient_definitions'

    # Unique 3-digit identifier code for a nutrient.
    id = Column(String(3), primary_key = True)
    # Units of measure (mg, g, g, and so on).
    units = Column(String(7), nullable = False)
    # International Network of Food Data Systems (INFOODS) Tagnames. A unique
    # abbreviation for a nutrient/food component developed by INFOODS to aid in
    # the interchange of data.
    tagname = Column(String(20), nullable = True)
    # Name of nutrient/food component.
    nutrDesc = Column(String(60), nullable = False)
    # Number of decimal places to which a nutrient value is rounded.
    num_Dec = Column(String(1), nullable = False)
    # Used to sort nutrient records in the same order as various reports
    # produced from SR.
    sR_Order = Column(Integer, nullable = False)

    nutrients = relationship("NutrientData", backref="nutrient_definitions")
    footnotes = relationship("Footnote", backref="footnotes") 

class SourceCode(Base):
    __tablename__ = 'src_cds'

    # 2-digit code
    id = Column(String(2), primary_key = True)
    # Description of source code that identifies the type of nutrient data.
    srcCd_Desc = Column(String(60), nullable = False)

    nutrients = relationship("NutrientData", backref="source")

class DataDerivationCodeDescription(Base):
    __tablename__ = 'deriv_cd'

    # Derivation Code.
    id = Column(String(4), primary_key = True)
    # Description of derivation code giving specific information on how the
    # value was determined.
    deriv_Desc = Column(String(120), nullable = False)

    nutrients = relationship("NutrientData", backref="dataDeriv")

class Weight(Base):
    __tablename__ = 'weight'

    id = Column(Integer, primary_key = True)
    # 5-digit Nutrient Databank number.
    food_id = Column(String(5), ForeignKey('food_descriptions.id'))
    # Sequence number
    seq = Column(String(2))
    # Unit modifier (for example, 1 in "1 cup").
    amount = Column(Numeric(5,3), nullable = False)
    # Description (for example, cup, diced, and 1-inch pieces).
    msre_Desc = Column(String(84), nullable = False)
    # Gram weight
    gm_Wgt = Column(Numeric(7,1), nullable = False)
    # Number of data points
    num_Data_Pts = Column(Integer, nullable = True)
    # Standard deviation
    std_Dev = Column(Numeric(7,3), nullable = True)

    food_descriptions = relationship("FoodDescription", backref = "weights")

class Footnote(Base):
    __tablename__ = 'footnotes'

    id = Column(Integer, primary_key = True)
    # 5-digit Nutrient Databank number.
    food_id = Column(String(5), ForeignKey('food_descriptions.id'))
    # Sequence number. If a given footnote applies to more than one nutrient
    # number, the same footnote number is used. As a result, this file cannot be
    # indexed.
    footnt_No = Column(String(4), nullable = False)
    # Type of footnote (see pdf, p.35)
    footnt_Typ = Column(String(1), nullable = False)
    # Unique 3-digit identifier code for a nutrient to which footnote applies.
    nutrient_definitions_id = Column(String(3), ForeignKey('nutrient_definitions.id'))
    # Footnote text
    footnt_Txt = Column(String(200), nullable = False)

class SourcesOfData(Base):
    __tablename__ = 'data_source'

    # Unique number identifying the reference/source.
    id = Column(String(6), primary_key = True)
    # List of authors for a journal article or name of sponsoring organization
    # for other documents.
    authors = Column(String(255), nullable = True)
    # Title of article or name of document, such as a report from a company or
    # trade association. 
    title = Column(String(255), nullable = True)
    # Year article or document was published.
    year = Column(String(4), nullable = True)
    # Name of the journal in which the article was published.
    journal = Column(String(135), nullable = True)
    # Volume number for journal articles, books, or reports; city where
    # sponsoring organization is located.
    vol_City = Column(String(16), nullable = True)
    # Issue number for journal article; State where the sponsoring organization
    # is located.
    issue_State = Column(String(5), nullable = True)
    # Starting page number of article/document.
    start_Page = Column(String(5), nullable = True)
    # Ending page number of article/document.
    end_Page = Column(String(5), nullable = True)

    nutrients = relationship("NutrientData", backref = "dataSource")