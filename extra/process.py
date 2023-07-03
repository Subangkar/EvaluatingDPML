import pandas as pd
df = pd.read_csv('census_all_str.csv')
colm_ren_map = dict(zip(['DREM', 'DPHY', 'DEAR', 'DEYE'], ['Cognitive Difficulty', 'Ambulatory Difficulty', 'Hearing Difficulty', 'Vision Difficulty']))
df.rename(columns=colm_ren_map, inplace=True)

attribute_replace_dict = {}

for col in ['Cognitive Difficulty', 'Ambulatory Difficulty', 'Hearing Difficulty', 'Vision Difficulty']:
    attribute_replace_dict[col] = {'No ' + col: 'n', col: 'y'}


ST_map = { 0:'Alabama/AL',
        1:'Alaska/AK',
        2:'Arizona/AZ',
        3:'Arkansas/AR',
        4:'California/CA',
        5:'Colorado/CO',
        6:'Connecticut/CT',
        7:'Delaware/DE',
        8:'District of Columbia/DC',
        9:'Florida/FL',
        10:'Georgia/GA',
        11:'Hawaii/HI',
        12:'Idaho/ID',
        13:'Illinois/IL',
        14:'Indiana/IN',
        15:'Iowa/IA',
        16:'Kansas/KS',
        17:'Kentucky/KY',
        18:'Louisiana/LA',
        19:'Maine/ME',
        20:'Maryland/MD',
        21:'Massachusetts/MA',
        22:'Michigan/MI',
        23:'Minnesota/MN',
        24:'Mississippi/MS',
        25:'Missouri/MO',
        26:'Montana/MT',
        27:'Nebraska/NE',
        28:'Nevada/NV',
        29:'New Hampshire/NH',
        30:'New Jersey/NJ',
        31:'New Mexico/NM',
        32:'New York/NY',
        33:'North Carolina/NC',
        34:'North Dakota/ND',
        35:'Ohio/OH',
        36:'Oklahoma/OK',
        37:'Oregon/OR',
        38:'Pennsylvania/PA',
        39:'Rhode Island/RI',
        40:'South Carolina/SC',
        41:'South Dakota/SD',
        42:'Tennessee/TN',
        43:'Texas/TX',
        44:'Utah/UT',
        45:'Vermont/VT',
        46:'Virginia/VA',
        47:'Washington/WA',
        48:'West Virginia/WV',
        49:'Wisconsin/WI',
        50:'Wyoming/WY',
        51:'Puerto Rico/PR'
    }

st_short_names = {v: v[-2:] for k,v in ST_map.items()}

attribute_replace_dict['ST'] = st_short_names

# attribute_replace_dict['MAR'] = {'Married': 'm', 'Widowed': 'w', 'Divorced': 'd', 'Separated': 's', 'Never married': 'n'}
attribute_replace_dict['MAR'] = {'Married': 'Married', 'Widowed': 'Widowed', 'Divorced': 'Divorced', 'Separated': 'Separated', 'Never married': 'never'}
# attribute_replace_dict['SCHL'] = {'No schooling completed': 'no', 'Nursery school, preschool': 'nursery/pre', 'Kindergarten': 'kinder', 
#                                   'Grade 1': 'G01', 'Grade 2': 'G02', 'Grade 3': 'G03', 'Grade 4': 'G04', 'Grade 5': 'G05', 
#                                   'Grade 6': 'G06', 'Grade 7': 'G07', 'Grade 8': 'G08', 'Grade 9': 'G09', 
#                                   'Grade 10': 'G10', 'Grade 11': 'G11', '12th grade - no diploma': 'G12-no dipl', 
#                                   'Regular high school diploma': 'reg hs diploma', 'GED or alternative credential': 'ged/alt', 
#                                   'Some college, but less than 1 year': '<1y clg', '1 or more years of college credit, no degree': '1y+ no deg', 
#                                   'Associates degree': 'Asso. degree', 'Bachelors degree': 'Bachelors', 'Masters degree': 'Masters', 
#                                   'Professional degree beyond a bachelors degree': 'Prof deg w bachelors', 'Doctorate degree': 'Dr.'}

attribute_replace_dict['SCHL'] = {v: k for k, v in {0: 'No schooling completed', 1: 'Nursery school, preschool', 2: 'Kindergarten', 
                                                    3: 'Grade 1', 4: 'Grade 2', 5: 'Grade 3', 6: 'Grade 4', 7: 'Grade 5', 8: 'Grade 6', 
                                                    9: 'Grade 7', 10: 'Grade 8', 11: 'Grade 9', 12: 'Grade 10', 13: 'Grade 11', 
                                                    14: '12th grade - no diploma', 15: 'Regular high school diploma', 
                                                    16: 'GED or alternative credential', 17: 'Some college, but less than 1 year', 
                                                    18: '1 or more years of college credit, no degree', 19: 'Associates degree', 
                                                    20: 'Bachelors degree', 21: 'Masters degree', 
                                                    22: 'Professional degree beyond a bachelors degree', 23: 'Doctorate degree'}.items()
                                  }

df.replace(attribute_replace_dict).to_csv('census_all_str_short.csv', index=False)