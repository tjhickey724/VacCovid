''' 
   States.py is a package with function for working with US states 
     stateNames is a dictionary to look up State names from the two letter abbreviations
     stateAbbrs is the reverse dictionary
   We get the names from the covidtracking.com data set for US states
   
   We also have access to 2020 state population data via the funtion
     statePop(stateAbbr)
   
   Finally we have defined a set of variables for regions of the US which 
   are associated to lists of their 2-letter abbreviations and
     regionPop(listOfStates)
   which returns the population of a list of states
   
   And we have demstates2020 and repstates2020.
   
   Most of this data comes from states.json which is read into the variable stateData
   as a list of dictionaries. It has data on "density" which could be interesting
   (e.g. scatter plot density and a covid-19 statistic)

'''

import json

stateData = json.load(open("states.json","r"))['data']

def statePop(state):
        ''' returns the 2019 population of the specified state (with 2 letter abbreviation)'''
        x = [d['Pop'] for d in stateData if d['State']==stateNames[state]]
        return x[0] if len(x)>0 else 100000000 
    
stateNames = {
    "AL": "Alabama",
    "AK": "Alaska",
    #"AS": "American Samoa",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    #"DC": "District Of Columbia",
    #"FM": "Federated States Of Micronesia",
    "FL": "Florida",
    "GA": "Georgia",
    #"GU": "Guam",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    #"MH": "Marshall Islands",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    #"MP": "Northern Mariana Islands",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    #"PW": "Palau",
    "PA": "Pennsylvania",
    #"PR": "Puerto Rico",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VT": "Vermont",
    #"VI": "Virgin Islands",
    "VA": "Virginia",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming"
}

stateAbbrs = {stateNames[x]:x for x in list(stateNames.keys())}
allStates = list(stateNames.keys())

northEast   = ['MA','CT','RI','VT','NH','ME']
midAtlantic = ['NY','PA','NJ','DE','MD','VA','WV']
southEast   = ['NC','SC','GA','FL','AL','MS','LA','AR','TN']
southWest   = ['TX','OK','NM','CO','UT','AZ']
midWest     =  ['OH','KY','IN','IL','MI','WI','MO','IA','MN','KS','NE','SD','ND']
upperMidwest = [                    'MI','WI',          'MN',          'SD','ND']
lowerMidwest = ['OH','KY','IN','IL',          'MO','IA',     'KS','NE']
west        = ['CA','NV','HI']
northWest   = ['WY','MT','ID','OR','WA','AK']

demStates = ['WA','OR','CA','NV','CO','NM',
            'MN','IL','VA','MD','DE','NJ',
            'NY','CT','RI','MA','VT','NH','ME','HI']

demStates2020 = "HI MA VT MD CA NY RI DE WA CT IL NJ OR NM VA ME CO NH MN MI WI NV PA AZ GA".split()
repStates2020 = [ s for s in stateNames.keys() if s not in demStates2020]

def otherStates(L):
    return [s for s in stateNames.keys() if s not in L]

repStates = [s for s in stateNames.keys() if s not in demStates]

def regionPop(states):
    pop=0
    for st in states:
        pop += statePop(st)
    return(pop)

    
    def __init__():
        pass



    