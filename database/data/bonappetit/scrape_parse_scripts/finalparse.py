# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup as Soup
import json
import string

files = []
gluten_list = {
    'anadama bread': 'gluten-free bread',
    'bagel': 'gluten-free bread',
    'baguette': 'gluten-free bread',
    'balep korkun': 'gluten-free bread',
    'banana bread': 'gluten-free bread',
    'bannock': 'gluten-free bread',
    'bara brith': 'gluten-free bread',
    'barbari bread': 'gluten-free bread',
    'barmbrack': 'gluten-free bread',
    'bastone': 'gluten-free bread',
    'bazlama': 'gluten-free bread',
    'beer bread': 'gluten-free bread',
    'waffle': 'gluten-free bread',
    'bhakri': 'gluten-free bread',
    'biscuit mix': 'gluten-free flour mix',
    'biscuit': 'gluten-free bread',
    'black bread': 'gluten-free bread',
    'bolani': 'gluten-free bread',
    'borlengo': 'gluten-free bread',
    'borodinsky': 'gluten-free bread',
    'boule': 'gluten-free bread',
    'bread roll': 'gluten-free bread',
    'breadstick': 'gluten-free bread',
    'brioche': 'gluten-free bread',
    'brown bread': 'gluten-free bread',
    'bublik': 'gluten-free bread',
    'soda bread': 'gluten-free bread',
    'challah': 'gluten-free bread',
    'cesnica': 'gluten-free bread',
    'chapati': 'gluten-free bread',
    'cholermus': 'gluten-free bread',
    'ciabatta': 'gluten-free bread',
    'cookie dough': 'gluten-free cookie dough',
    'coppia ferrarese': 'gluten-free bread',
    'cottage loaf': 'gluten-free bread',
    'crepe': 'gluten-free bread',
    'crisp bread': 'gluten-free bread',
    'croutons': 'gluten-free bread',
    'croissant': 'gluten-free bread',
    'crumpet': 'gluten-free bread',
    'cuban bread': 'gluten-free bread',
    'damper': 'gluten-free bread',
    'dampfnudl': 'gluten-free bread',
    'pizza dough': 'gluten-free pizza dough',
    'dough': 'gluten-free dough',
    'dosa': 'gluten-free bread',
    'english muffin': 'gluten-free bread',
    'flatbread': 'gluten-free bread',
    'focaccia': 'gluten-free bread',
    'matzo': 'gluten-free bread',
    'naan': 'gluten-free bread',
    'pancake': 'gluten-free bread',
    'papadum': 'gluten-free bread',
    'paratha': 'gluten-free bread',
    'pita': 'gluten-free bread',
    'potato bread': 'gluten-free bread',
    'pretzle': 'gluten-free bread',
    'pumpernickel bread': 'gluten-free bread',
    'rye bread': 'gluten-free bread',
    'scone': 'gluten-free bread',
    'sourdough bread': 'gluten-free bread',
    'spelt bread': 'gluten-free bread',
    'white bread': 'gluten-free bread',
    'country white bread': 'gluten-free bread',
    'whole wheat bread': 'gluten-free bread',

    'amplang': 'gluten-free crackers',
    'animal cracker': 'gluten-free crackers',
    'bath oliver': 'gluten-free crackers',
    'couque de dinant': 'gluten-free crackers',
    'cream cracker': 'gluten-free crackers',
    'crispbread': 'gluten-free crackers',
    'digestive biscuit': 'gluten-free crackers',
    'graham cracker': 'gluten-free graham crackers',
    'hardtack': 'gluten-free crackers',
    "jacob's oddities": 'gluten-free crackers',
    'maltose crackers': 'gluten-free crackers',
    'mein gon': 'gluten-free crackers',
    'nantong xiting cracker': 'gluten-free crackers',
    'olive no hana': 'gluten-free crackers',
    'oyster cracker': 'gluten-free crackers',
    'pletzel': 'gluten-free crackers',
    'premium plus': 'gluten-free crackers',
    'ry-krisp': 'gluten-free crackers',
    'saltine cracker': 'gluten-free crackers',
    'taralli': 'gluten-free crackers',
    "arnott's shapes": 'gluten-free crackers',
    'bremner wafer': 'gluten-free crackers',
    "captain's wafers": 'gluten-free crackers',
    "carr's": 'gluten-free crackers',
    'cheese nips': 'gluten-free crackers',
    'cheez-it': 'gluten-free crackers',
    'club crackers': 'gluten-free crackers',
    'cones': 'gluten-free ice-cream cones',
    'crown pilot crackers': 'gluten-free crackers',
    'goldfish crackers': 'gluten-free crackers',
    'in a biskit': 'gluten-free crackers',
    'le snak': 'gluten-free crackers',
    'pepperidge farm': 'gluten-free crackers',
    'rice thins': 'gluten-free crackers',
    'ritz crackers': 'gluten-free crackers',
    'ryvita': 'gluten-free crackers',
    'sao (biscuit)': 'gluten-free crackers',
    'triscuit': 'gluten-free crackers',
    'tuc (cracker)': 'gluten-free crackers',
    'vegetable thins': 'gluten-free crackers',
    'Wasabröd': 'gluten-free crackers',
    'westminster cracker company': 'gluten-free crackers',
    'wheat thins': 'gluten-free crackers',

    'phyllo': 'gluten-free phyllo',
    'puff pastry': 'gluten-free puff pastry',
    'cookies': 'gluten-free cookies',
    'shortbread': 'gluten-free shortbread',
    'shortcake': 'gluten-free shortcake',
    'angelfood cake': 'gluten-free cake',
    'pound cake': 'gluten-free cake',
    'sandwich cookies': 'gluten-free sandwich cookies',
    'cookie crumbs': 'gluten-free cookie crumbs',
    'pie crust': 'gluten-free pie crust',
    'puff pastry sheets': 'gluten-free puff pastry sheets',
    'licorice': 'gluten-free licorice',

    'panko': 'gluten-free panko',
    'breadcrumb': 'gluten-free breadcrumbs',
    'beer': 'gluten-free beer',
    'lager': 'gluten-free lager',
    'wheatberries': 'quinoa',
    'farro': 'quinoa',
    'barley': 'quinoa',
    'triticale': "sorry, we don't have a substitution recommendation at this time.",
    'malt': "sorry, we don't have a substitution recommendation at this time.",
    "brewer's yeast": "sorry, we don't have a recommendation at this time.",
    'couscous': 'quinoa',
    'bulgur': 'quinoa',
    'dinkle': 'quinoa',
    'seitan': 'gluten-free protein',
    'soy sauce': 'gluten-free tamari',

    'bowtie': 'gluten-free pasta',
        'macaroni': 'gluten-free pasta',
        'ramen': 'gluten-free pasta',
        'soba': 'gluten-free pasta',
        'udon': 'gluten-free pasta',
        'chow mein': 'gluten-free pasta',
        'egg noodle': 'gluten-free pasta',
        'bigoli': 'gluten-free pasta',
        'bucatini': 'gluten-free pasta',
        "capelli d'angelo": 'gluten-free pasta',
        'capellini': 'gluten-free pasta',
        'fedelini': 'gluten-free pasta',
        'fusilli': 'gluten-free pasta',
        'fusilli bucati': 'gluten-free pasta',
        'maccheroni alla molinara': 'gluten-free pasta',
        'matriciani': 'gluten-free pasta',
        'perciatelli': 'gluten-free pasta',
        'pici': 'gluten-free pasta',
        'spaghetti': 'gluten-free pasta',
        'spaghettini': 'gluten-free pasta',
        'spaghettoni': 'gluten-free pasta',
        'vermicelli': 'gluten-free pasta',
        'vermicelloni': 'gluten-free pasta',
        'ziti': 'gluten-free pasta',
        'zitoni': 'gluten-free pasta',
        'bavette': 'gluten-free pasta',
        'bavettine': 'gluten-free pasta',
        'ciriole': 'gluten-free pasta',
        'fettuce': 'gluten-free pasta',
        'fettuccine': 'gluten-free pasta',
        'fettucelle': 'gluten-free pasta',
        'lagane': 'gluten-free pasta',
        'lasagne': 'gluten-free pasta',
        'gravagna': 'gluten-free pasta',
        'lasagnette': 'gluten-free pasta',
        'lasagnotte': 'gluten-free pasta',
        'linguettine': 'gluten-free pasta',
        'linguine': 'gluten-free pasta',
        'mafalde': 'gluten-free pasta',
        'mafaldine': 'gluten-free pasta',
        'pappardelle': 'gluten-free pasta',
        'pillus': 'gluten-free pasta',
        'pizzoccheri': 'gluten-free pasta',
        'sagnarelli': 'gluten-free pasta',
        'scialatelli': 'gluten-free pasta',
        'scilatielli': 'gluten-free pasta',
        'spaghetti alla chitarra': 'gluten-free pasta',
        'stringozzi': 'gluten-free pasta',
        'tagliatelle': 'gluten-free pasta',
        'taglierini': 'gluten-free pasta',
        'trenette': 'gluten-free pasta',
        'tripoline': 'gluten-free pasta',
        'calamarata': 'gluten-free pasta',
        'calamaretti': 'gluten-free pasta',
        'cannelloni': 'gluten-free pasta',
        'cavatappi': 'gluten-free pasta',
        'cellentani': 'gluten-free pasta',
        'chifferi': 'gluten-free pasta',
        'ditalini': 'gluten-free pasta',
        'elicoidali': 'gluten-free pasta',
        'fagioloni': 'gluten-free pasta',
        'Fideuà': 'gluten-free pasta',
        'garganelli': 'gluten-free pasta',
        'gemelli': 'gluten-free pasta',
        'macaroni': 'gluten-free pasta',
        'maccheroncelli': 'gluten-free pasta',
        'maltagliati': 'gluten-free pasta',
        'manicotti': 'gluten-free pasta',
        'marziani': 'gluten-free pasta',
        'mezzani pasta': 'gluten-free pasta',
        'mezze penne': 'gluten-free pasta',
        'mezzi bombardoni': 'gluten-free pasta',
        'mostaccioli': 'gluten-free pasta',
        'paccheri': 'gluten-free pasta',
        'pasta al ceppo': 'gluten-free pasta',
        'penne': 'gluten-free pasta',
        'penne rigate': 'gluten-free pasta',
        'penne lisce': 'gluten-free pasta',
        'penne zita': 'gluten-free pasta',
        'pennette': 'gluten-free pasta',
        'pennoni': 'gluten-free pasta',
        'rigatoncini': 'gluten-free pasta',
        'rigatoni': 'gluten-free pasta',
        'rotini': 'gluten-free pasta',
        "sagne 'ncannulate": 'gluten-free pasta',
        'spirali': 'gluten-free pasta',
        'spiralini': 'gluten-free pasta',
        'trenne': 'gluten-free pasta',
        'trennette': 'gluten-free pasta',
        'tortiglioni': 'gluten-free pasta',
        'tuffoli': 'gluten-free pasta',
        'biciclette': 'gluten-free pasta',
        'campanelle': 'gluten-free pasta',
        'capunti': 'gluten-free pasta',
        'casarecce': 'gluten-free pasta',
        'cavatelli': 'gluten-free pasta',
        'cencioni': 'gluten-free pasta',
        'conchiglie': 'gluten-free pasta',
        'conchiglioni': 'gluten-free pasta',
        'corzetti': 'gluten-free pasta',
        'creste di galli': 'gluten-free pasta',
        'croxetti': 'gluten-free pasta',
        'farfalle': 'gluten-free pasta',
        'farfalloni': 'gluten-free pasta',
        'fiorentine': 'gluten-free pasta',
        'fiori': 'gluten-free pasta',
        "foglie d'ulivo": 'gluten-free pasta',
        'gigli': 'gluten-free pasta',
        'gramigna': 'gluten-free pasta',
        'lanterne': 'gluten-free pasta',
        'lumache': 'gluten-free pasta',
        'lumaconi': 'gluten-free pasta',
        'maltagliati': 'gluten-free pasta',
        'mandala': 'gluten-free pasta',
        'marille': 'gluten-free pasta',
        'orecchiette': 'gluten-free pasta',
        'quadrefiore': 'gluten-free pasta',
        'radiatori': 'gluten-free pasta',
        'ricciolini': 'gluten-free pasta',
        'ricciutelle': 'gluten-free pasta',
        'rotelle': 'gluten-free pasta',
        'rotini': 'gluten-free pasta',
        'sorprese': 'gluten-free pasta',
        'sorprese': 'gluten-free pasta',
        'strozzapreti': 'gluten-free pasta',
        'torchio': 'gluten-free pasta',
        'trofie': 'gluten-free pasta',
        'acini di pepe': 'gluten-free pasta',
        'alfabeto': 'gluten-free pasta',
        'anelli': 'gluten-free pasta',
        'anellini': 'gluten-free pasta',
        'conchigliette': 'gluten-free pasta',
        'corallini': 'gluten-free pasta',
        'ditali': 'gluten-free pasta',
        'ditalini': 'gluten-free pasta',
        'egg barley': 'gluten-free pasta',
        'farfalline': 'gluten-free pasta',
        'fideos': 'gluten-free pasta',
        'filini': 'gluten-free pasta',
        'fregula': 'gluten-free pasta',
        'funghini': 'gluten-free pasta',
    'grattini': 'gluten-free pasta',
    'grattoni': 'gluten-free pasta',
    'midolline': 'gluten-free pasta',
    'occhi di pernice': 'gluten-free pasta',
    'orzo': 'gluten-free pasta',
    'risoni': 'gluten-free pasta',
    'pastina': 'gluten-free pasta',
    "pearl 'Pasta'": 'gluten-free pasta',
    'puntine': 'gluten-free pasta',
    'quadrettini': 'gluten-free pasta',
    'risi': 'gluten-free pasta',
    'seme di melone': 'gluten-free pasta',
    'stelle': 'gluten-free pasta',
    'stelline': 'gluten-free pasta',
    'stortini': 'gluten-free pasta',
    'tripolini': 'gluten-free pasta',
    'agnolotti': 'gluten-free pasta',
    'cappelletti': 'gluten-free pasta',
    'casoncelli': 'gluten-free pasta',
    'Casonsèi': 'gluten-free pasta',
    'casunziei': 'gluten-free pasta',
    'fagottini': 'gluten-free pasta',
    'maultasche': 'gluten-free pasta',
    'mezzelune': 'gluten-free pasta',
    'occhi di lupo': 'gluten-free pasta',
    'pelmeni': 'gluten-free pasta',
    'pierogi': 'gluten-free pasta',
    'ravioli': 'gluten-free pasta',
    'sacchettini': 'gluten-free pasta',
    'sacchettoni': 'gluten-free pasta',
    'sacchetti': 'gluten-free pasta',
    'tortellini': 'gluten-free pasta',
    'tortelloni': 'gluten-free pasta',
    'cappelli del prete': 'gluten-free pasta',
    'gnocchi': 'gluten-free pasta',
    'passatelli': 'gluten-free pasta',
    'spätzle': 'gluten-free pasta'
}

unit_list = {
    'cups': 'cup',
    'cup': 'cup',
    'c.': 'cup',
    'c': 'cup',
    'fluid ounces': 'fl-oz',
    'ounce': 'oz',
    'oz.': 'oz',
    'oz': 'oz',
    'fl ounces': 'fl-oz',
    'fl ounce': 'fl-oz',
    'fl oz.': 'fl-oz',
    'fl oz': 'fl-oz',
    'fl. ounces': 'fl-oz',
    'fl. ounce': 'fl-oz',
    'fl. oz.': 'fl-oz',
    'fl. oz': 'fl-oz',
    'gallons': 'gal',
    'gallon': 'gal',
    'gal.': 'gal',
    'gal': 'gal',
    'ounces': 'oz',
    'pints': 'pnt',
    'pint': 'pnt',
    'pt.': 'pnt',
    'pt': 'pnt',
    'pounds': 'lb',
    'pound': 'lb',
    'lbs.': 'lb',
    'lbs': 'lb',
    'lb.': 'lb',
    'lb': 'lb',
    'quarts': 'qt',
    'quart': 'qt',
    'qts.': 'qt',
    'qts': 'qt',
    'qt.': 'qt',
    'qt': 'qt',
    'tablespoons': 'tbsp',
    'tablespoon': 'tbsp',
    'tbsp.': 'tbsp',
    'tbsp': 'tbsp',
    'tbs.': 'tbsp',
    'tbs': 'tbsp',
    'T.': 'tbsp',
    'T': 'tbsp',
    'teaspoons': 'tsp',
    'teaspoon': 'tsp',
    'tsp.': 'tsp',
    'tsp': 'tsp',
    't.': 'tsp',
    't': 'tsp',
    'grams': 'g',
    'gram': 'g',
    'gr.': 'g',
    'gr': 'g',
    'g.': 'g',
    'g': 'g',
    'kilograms': 'kg',
    'kilogram': 'kg',
    'kg.': 'kg',
    'kg': 'kg',
    'liters': 'ltr',
    'liter': 'ltr',
    'l.': 'ltr',
    'l': 'ltr',
    'milligrams': 'mg',
    'milligram': 'mg',
    'mg.': 'mg',
    'mg': 'mg',
    'milliliters': 'ml',
    'milliliter': 'ml',
    'ml.': 'ml',
    'ml': 'ml'
}

punctuation = string.punctuation


light_ratio = {}
light_ratio['protein'] = ['sorghum flour', .165]
light_ratio['fat'] = ['cashew flour', .165]
light_ratio['lightness'] = ['white rice flour', .33]
light_ratio['stickiness'] = ""
light_ratio['texture'] = ""
light_ratio['density'] = ""
light_ratio['starch'] = ['cornstarch', .33]
light_ratio['binder'] = ['xanthum gum', .5]
light_ratio['leavener'] = ""

regular_ratio = {}
regular_ratio['protein'] = ['sorghum flour', .142]
regular_ratio['fat'] = ['almond flour', .142]
regular_ratio['lightness'] = ['white rice flour', .284]
regular_ratio['stickiness'] = ""
regular_ratio['density'] = ['brown rice flour', .142]
regular_ratio['texture'] = ""
regular_ratio['starch'] = ['potato starch', .284]
regular_ratio['binder'] = ['xanthum gum', .5]
regular_ratio['leavener'] = ""

dense_ratio = {}
dense_ratio['protein'] = ['sorghum flour', .25]
dense_ratio['fat'] = ['walnut flour', .125]
dense_ratio['lightness'] = ['oat flour', .125]
dense_ratio['stickiness'] = ""
dense_ratio['density'] = ['buckwheat flour', .25]
dense_ratio['texture'] = ""
dense_ratio['starch'] = ['potato starch', .25]
dense_ratio['binder'] = ['xanthum gum', 1]
dense_ratio['leavener'] = ""

light_textured_ratio = {}
light_textured_ratio['protein'] = ['sorghum flour', .142]
light_textured_ratio['fat'] = ['almond flour', .142]
light_textured_ratio['lightness'] = ['teff flour', .285]
light_textured_ratio['stickiness'] = ""
light_textured_ratio['density'] = ""
light_textured_ratio['texure'] = ['millet flour', .142]
light_textured_ratio['starch'] = ['tapioca starch', .285]
light_textured_ratio['binder'] = ['xanthum gum', .5]
light_textured_ratio['leavener'] = ""

dense_textured_ratio = {}
dense_textured_ratio['protein'] = ['sorghum flour', .142]
dense_textured_ratio['fat'] = ['hazelnut flour', .142]
dense_textured_ratio['lightness'] = ['corn flour', .142]
dense_textured_ratio['stickiness'] = ""
dense_textured_ratio['density'] = ['potato flour', .142]
dense_textured_ratio['texure'] = ['hemp flour', .142]
dense_textured_ratio['starch'] = ['potato starch', .285]
dense_textured_ratio['binder'] = ['xanthum gum', 1]
dense_textured_ratio['leavener'] = ""

light_sticky_ratio = {}
light_sticky_ratio['protein'] = ['sorghum flour', .125]
light_sticky_ratio['fat'] = ['almond flour', .25]
light_sticky_ratio['lightness'] = ['teff flour', .125]
light_sticky_ratio['stickiness'] = ['sweet rice flour', .25]
light_sticky_ratio['density'] = ""
light_sticky_ratio['texture'] = ""
light_sticky_ratio['starch'] = ['arrowroot starch', .25]
light_sticky_ratio['binder'] = ['guar gum', 1]
light_sticky_ratio['leavener'] = ""

regular_sticky_ratio = {}
regular_sticky_ratio['protein'] = ['sorghum flour', .11]
regular_sticky_ratio['fat'] = ['chesnut flour', .22]
regular_sticky_ratio['lightness'] = ['white rice flour', .11]
regular_sticky_ratio['stickiness'] = ['amaranth flour', .11]
regular_sticky_ratio['density'] = ['brown rice flour', .22]
regular_sticky_ratio['texure'] = ""
regular_sticky_ratio['starch'] = ['potato starch', .22]
regular_sticky_ratio['binder'] = ['guar gum', 1]
regular_sticky_ratio['leavener'] = ""

dense_sticky_ratio = {}
dense_sticky_ratio['protein'] = ['sorghum flour', .2]
dense_sticky_ratio['fat'] = ['hazelnut flour', .2]
dense_sticky_ratio['lightness'] = ['white rice flour', .1]
dense_sticky_ratio['stickiness'] = ['amaranth flour', .1]
dense_sticky_ratio['density'] = ['buckwheat flour', .2]
dense_sticky_ratio['texure'] = ""
dense_sticky_ratio['starch'] = ['acorn starch', .2]
dense_sticky_ratio['binder'] = ['guar gum', 1]
dense_sticky_ratio['leavener'] = ""

light_rising_ratio = {}
light_rising_ratio['protein']= ['sorghum flour', .164]
light_rising_ratio['fat'] = ['almond flour', .164]
light_rising_ratio['lightness'] = ['white rice flour', .328]
light_rising_ratio['stickiness'] = ""
light_rising_ratio['density'] = ""
light_rising_ratio['texure'] = ""
light_rising_ratio['starch'] = ['cornstarch', .328]
light_rising_ratio['binder'] = ['xanthum gum', 1]
light_rising_ratio['leavener'] = ['baking powder', 1]

dense_rising_ratio = {}
dense_rising_ratio['protein'] = ['sorghum flour', .25]
dense_rising_ratio['fat'] = ['almond flour', .125]
dense_rising_ratio['lightness'] = ['white rice flour', .125]
dense_rising_ratio['stickiness'] = ""
dense_rising_ratio['density'] = ['brown rice flour', .25]
dense_rising_ratio['texure'] = ""
dense_rising_ratio['starch'] = ['potato starch', .25]
dense_rising_ratio['binder'] = ['xanthum gum', 1]
dense_rising_ratio['leavener'] = ['baking powder', 1]

gluten_flours = {
'all purpose flour': {'type':regular_ratio, 'weight': 125},
'all-purpose flour': {'type':regular_ratio, 'weight':125},
    'semolina flour': {'type':dense_ratio, 'weight': 167},
    'cake flour': {'type':light_ratio, 'weight': 137},
    'white whole wheat flour': {'type':dense_ratio, 'weight': 120},
    'regular whole wheat flour': {'type':dense_ratio, 'weight': 125},
    'durum wheat flour': {'type':dense_ratio, 'weight': 125},
    'whole wheat pastry flour': {'type':regular_ratio, 'weight': 136},
    'whole wheat flour': {'type':dense_ratio, 'weight': 120},
    'bread flour': {'type':regular_sticky_ratio, 'weight': 144},
    'graham flour': {'type':dense_textured_ratio, 'weight': 120},
    'instant flour': {'type':light_ratio, 'weight': 120},
    'Wondra': {'type':light_ratio, 'weight': 120},
    'pastry flour': {'type':light_ratio, 'weight': 136},
    'pumpernickel flour': {'type':dense_ratio, 'weight': 120},
    'rye flour': {'type':dense_ratio, 'weight': 128},
    'self-rising flour': {'type':light_rising_ratio, 'weight': 120},
    'spelt flour': {'type':light_sticky_ratio, 'weight': 120},
    'whole wheat bread flour': {'type':dense_sticky_ratio, 'weight': 152},
    'durum flour': {'type':regular_ratio, 'weight': 144},
    'kamut flour': {'type':regular_ratio, 'weight': 120},
    'barley flour': {'type':regular_ratio, 'weight': 120},
    'triticale flour': {'type':regular_sticky_ratio, 'weight': 130},
    'wholemeal flour': {'type':dense_ratio, 'weight': 152},
    'gluten flour': {'type':dense_sticky_ratio, 'weight': 120},
    'enriched flour': {'type':regular_ratio, 'weight': 120},
    'plain flour': {'type':regular_ratio, 'weight': 120},
    'atta flour': {'type':dense_ratio, 'weight': 152},
    'maida flour': {'type':light_ratio, 'weight': 152},
    'noodle flour': {'type':regular_ratio, 'weight': 120},
    'high gluten flour': {'type':dense_sticky_ratio, 'weight': 152},
    'first clear flour': {'type':regular_sticky_ratio, 'weight': 120},
    'enriched all-purpose flour': {'type':regular_ratio, 'weight': 125},
    'bleached enriched all-purpose flour': {'type':regular_ratio, 'weight': 125},
    'unbleached enriched all-purpose flour': {'type':regular_ratio, 'weight': 136},
    'bleached all-purpose flour': {'type':regular_ratio, 'weight': 125},
    'unbleached all-purpose flour': {'type':regular_ratio, 'weight': 136},
    'bolted flour': {'type':regular_ratio, 'weight': 120},
    'self-rising cake flour': {'type':light_rising_ratio, 'weight': 137},
    'clear flour': {'type':regular_ratio, 'weight': 128},
    'farina': {'type':light_textured_ratio, 'weight': 176},
    'cream of wheat': {'type':light_textured_ratio, 'weight': 176},
    'patent flour': {'type':regular_ratio, 'weight': 128},
    'extra short patent flour': {'type':light_ratio, 'weight': 128},
    'fancy patent flour': {'type':light_ratio, 'weight':128},
    'first patent flour': {'type':regular_ratio, 'weight': 152},
    'short patent flour': {'type':regular_sticky_ratio, 'weight': 152},
    'medium patent flour': {'type':regular_sticky_ratio, 'weight': 136},
    'long patent flour': {'type':regular_sticky_ratio, 'weight': 136},
    'fancy clear flour': {'type':light_ratio, 'weight': 152},
    'second clear flour': {'type':dense_ratio, 'weight': 152},
    'stuffed straight flour': {'type':regular_sticky_ratio, 'weight': 150},
    'straight flour': {'type':regular_sticky_ratio, 'weight': 150},
    'vital wheat gluten': {'type':dense_ratio, 'weight': 120},
    'wheat germ': {'type':dense_textured_ratio, 'weight': 115},
    'wheat bran': {'type':dense_textured_ratio, 'weight': 94},
    'unprocessed bran': {'type':dense_textured_ratio, 'weight': 94},
    'plain wholemeal flour': {'type':dense_ratio, 'weight': 120},
    'hard whole wheat flour': {'type':dense_textured_ratio, 'weight': 120},
    'stone ground whole wheat flour': {'type':dense_ratio, 'weight': 120},
    'whole wheat white flour': {'type':dense_ratio, 'weight': 120},
    'not a match': 'Safe'
}
classification = {'starch':'potato starch', 'starch':'tapioca starch', 'starch':'cornstarch', 'starch':'arrowroot starch', 'starch':'acorn starch', 'gum':'xanthum gum', 'gum':'guar gum','protein':'garbanzo bean flour', 'protein':'fava bean flour', 'protein':'sorghum flour','protein':'amaranth flour',  'protein':'lentil flour', 'protein':'chickpea flour', 'protein':'oat flour', 'protein':'soy flour',
'fat':'almond flour', 'fat':'hazelnut flour', 'fat':'chesnut flour', 'fat':'cashew flour', 'fat':'walnut flour', 'fat':'flax meal','lightness':'white rice flour',  'lightness':'oat flour', 'lightness':'corn flour', 'lightness':'teff flour','stickiness':'amaranth', 'stickiness':'sweet rice flour','texture':'coconut flour', 'texture':'masa harina', 'texture':'corn meal', 'texture':'lupin flour', 'texture':'hemp flour', 'texture':'millet flour',
'density':'brown rice flour', 'density':'quinoa flour', 'density':'chia flour', 'density':'buckwheat flour', 'density':'potato flour' }

def swap_flour(name):
	count = 0
	for flour in gluten_flours:
		count += 1
		if flour in name:
			return gluten_flours[flour]
		elif count < len(gluten_flours):
			continue
		else:
			return gluten_flours['not a match']


def make_soup(my_file):
    print my_file
    html = open(my_file).read()
    soup = Soup(html)
    return soup

def check_sub(name): 
    count = 0
    for item in gluten_list: 
        count += 1
        if item in name: 
            print "here!", item
            return gluten_list[item]
        elif count < len(gluten_list): 
            continue
        else :
            return "no substitute needed"   

def check_gluten(name): 
    count = 0
    for item in gluten_list: 
        count += 1
        if item in name: 
            print "here!", item
            return "gluten here!"
        if count < len(gluten_list): 
            continue
        else :
            return "no gluten here!"

def distill(soup):
    recipe = {}
    recipe['ingredients'] = {}
    try:

        recipe['url'] = soup.findAll('a', {'class': 'addToBox btn primary shaded save-recipe hoverable'})[0].get('href')
    except IndexError:
        recipe['url'] = ""
    try:
        recipe['name'] = soup.findAll('h1', {'itemprop': 'name'})[0].text.encode('utf-8')
    except IndexError:
        recipe['name'] = ""
    try:    
        description = soup.findAll('div', {'id': 'recipes-hdr'})[0].findAll('h2')
        if description != []:
            recipe['description'] = soup.findAll('div', {'id': 'recipes-hdr'})[0].findAll('h2')[0].text.encode('utf-8')
    except IndexError:
        recipe['description'] = ""
    try:
        recipe['image'] = soup.findAll('img',{'itemprop': 'image'})[0].get('src')
    except IndexError:
        recipe['image'] = ""
    try:
        servings = soup.findAll('span', {'class': 'total-servings'})[0]
        if servings != 0:
            recipe['servings'] = soup.findAll('span', {'class': 'total-servings'})[0].text.encode('utf-8')
    except IndexError:
        recipe['servings'] = ""
    try:
        ingredients = soup.findAll('span', {'class': 'ingredient'})
        for i in range(len(ingredients)):
            name = ingredients[i].find('span', {'class': 'name'}).text.encode('utf-8').lower()
            quantity = ingredients[i].find('span', {'class': 'quantity'}).text
            unit = ingredients[i].find('span', {'class': 'unit'}).text.encode('utf-8').lower()
            if unit == "":
                splitname = name.split("(click ")
                if splitname[-1] == "for recipe)":
                    splitname = " ".join(splitname[:-1]).split()
                if splitname[0] in unit_list: 
                    splitname = name.split()    
                    newunit = splitname[0]
                    newname = " ".join(splitname[1:]).lower()
                    flourratio = swap_flour(newname)
                    if flourratio != "Safe":
                        print flourratio, recipe['name']
                    glutenstat = check_gluten(newname)
                    sub = check_sub(newname)
                    recipe['ingredients'][newname] = {'quantity': quantity, 'unit': newunit, 'flour':flourratio, 'gluten': glutenstat, 'substitute': sub}
                else:
                    flourratio = swap_flour(name)
                    if flourratio != "Safe":
                        print flourratio, recipe['name']
                    glutenstat = check_gluten(name)
                    sub = check_sub(name)
                    recipe['ingredients'][name] = {'quantity':quantity, 'unit': "", 'flour':flourratio, 'gluten': glutenstat, 'substitute': sub}
            else:
                flourratio = swap_flour(name)
                if flourratio != "Safe":
                        print flourratio, recipe['name']
                glutenstat = check_gluten(name)
                sub = check_sub(name)
                recipe['ingredients'][name] = {'quantity': quantity, 'unit':unit, 'flour':flourratio, 'gluten': glutenstat, 'substitute': sub}
    except IndexError:
    	print "im empty"
        recipe['ingredients'] = {}
    try:
        instructions = soup.findAll('div', {'itemprop': 'recipeInstructions'})
        if instructions != []:
            steps = []
            for i in range(len(instructions)):
                steps.append(instructions[i].text.encode('utf-8'))
            recipe['instructions'] = steps
    except IndexError:
        recipe['instructions'] = ""
    try:
        recipe['calories'] = soup.findAll('li', {'itemprop': 'calories'})[0].text
    except IndexError:
        recipe['calories'] = ""
    try:
        recipe['fatContent'] = soup.findAll('li', {'itemprop': 'fatContent'})[0].text
    except IndexError:
        recipe['fatContent'] = ""
    try:
        recipe['saturatedFatContent'] = soup.findAll('li', {'itemprop': 'saturatedFatContent'})[0].text
    except IndexError:
        recipe['saturatedFatContent'] = ""
    try:
        recipe['cholesterolContent'] = soup.findAll('li', {'itemprop': 'cholesterolContent'})[0].text
    except IndexError:
        recipe['cholesterolContent'] = ""
    try:
        recipe['carbohydrateContent'] = soup.findAll('li', {'itemprop': 'carbohydrateContent'})[0].text
    except IndexError:
        recipe['carbohydrateContent'] = ""
    try:
        recipe['fiberContent'] = soup.findAll('li', {'itemprop': 'fiberContent'})[0].text
    except IndexError:
        recipe['fiberContent'] = ""
    try:
        recipe['sugarContent'] = soup.findAll('li', {'itemprop': 'sugarContent'})[0].text
    except IndexError:
        recipe['sugarContent'] = ""
    try:
        recipe['proteinContent'] = soup.findAll('li', {'itemprop': 'proteinContent'})[0].text
    except IndexError:
        recipe['proteinContent'] = ""
    try:
        recipe['sodiumContent'] = soup.findAll('li', {'itemprop': 'sodiumContent'})[0].text
    except IndexError:
        recipe['sodiumContent'] = ""
    try:
        recipekeywords = []
        keywords = soup.findAll('p', {'class': 'grouped'})[0].findAll('a')
        for keyword in keywords:
            recipekeywords.append(keyword.text.encode('utf-8'))
        recipe['keywords'] = recipekeywords
    except IndexError:
        recipe['keywords'] = []

    return recipe


def write_json_recipe_object(recipe, counter):
    if recipe['ingredients'] == {}:
        print recipe['name'], "empty"
        recipe = json.JSONEncoder(sort_keys=True, indent = 2).encode(recipe)
        with open("/Users/marswilliams/src/funtimes/database/data/bonappetit/maybenot/recipeobject" + str(counter) + ".json", "w") as newfile: 
            newfile.write(recipe)
    else:
		recipe = json.JSONEncoder(sort_keys=True, indent = 2).encode(recipe)
		with open("/Users/marswilliams/src/funtimes/database/data/bonappetit/maybehim/recipeobject" + str(counter) + ".json", "w") as newfile: 
		    newfile.write(recipe)

def make_list():
    with open("recipelist.txt") as listfile:
        completelist = listfile.read().split("\n")
        return completelist

def main():
    counter = 0
    files = make_list()
    print len(files)
    for i in files:
        soup = make_soup(i)
        recipe = distill(soup)
        counter +=1
        write_json_recipe_object(recipe, counter)
    


if __name__ == "__main__":
    main()