'''
  CovidAnalysis defines several classes representing data 
  needed to analyze the state of the covid-19 pandemic on any particular date.
  We get our data from these sites:
  * https://covidtracking.com for the low level data about covid-19 in each state
  * https://raw.githubusercontent.com/govex/COVID-19  data about vaccination in each state
  * https://www.kaggle.com/madeleineferguson/state-population  state populations in 2019 (and density, etc.) 
'''

import math
import csv
import json
import requests
import matplotlib.pyplot as plt
import datetime

import VectorAlgebra as VA
import States



class CovidTracking():
    def __init__(self,use_cached_data=True):
        ''' this loads in the data either from a file (if use_cached_data is true) or from the website to get the latest data '''
        if use_cached_data:
            with open("us_covid_data.json") as jsonfile:
                self.us_covid_data = json.load(jsonfile)
            with open("us_vac_data.json") as jsonfile:
                self.us_vac_data = json.load(jsonfile)
        else:
            url = "https://covidtracking.com/api/states/daily"
            text = requests.get(url).text
            data = json.loads(text)
            # now we need to clean the data by replacing all None values with 0
            for d in data:
                for x in d.keys():
                    if d[x]==None:
                        d[x]=0

            self.us_covid_data = data
            jsonfile = open("us_covid_data.json","w")
            json.dump(self.us_covid_data,jsonfile)
            jsonfile.close()
            
            url = "https://raw.githubusercontent.com/govex/COVID-19/" + "master/data_tables/vaccine_data/raw_data/vaccine_data_us_state_timeline.csv"
            text = requests.get(url).text

            data = list(csv.DictReader(text.split("\n")))
            self.us_vac_data = data
            for x in data:
                x['oldDate'] = x['date']
                x['date']= self.convertDate(x['date'])
            jsonfile = open("us_vac_data.json","w")
            json.dump(self.us_vac_data,jsonfile)
            jsonfile.close()

            
        # now we calculate the set of dates this data represents 
        self.dates = sorted(list({d['date'] for d in self.us_covid_data}))
        
        # and the offset of the first date in the year 2020
        self.date0 = (self.dates[0]%100)-1 # the first date is 202001XX for some XX, this returns XX-1
        self.first_date = self.dates[0]
        self.last_date = self.dates[-1]
    
    def _getField(self,x,field,default=0):
        ''' auxiliary function to deal with missing values for fields when represented as None '''
        if field in x:
            z = x.get(field,default)
            if (z==None):
                return default
            else:
                return z
        else:
            return 0
    
    def genDateRange(self,first,last):
        '''  given dates in the form YYYYMMDD, it generates a list of such dates with first<=d<=last'''
        year = first//10000
        month = (first%10000)//100
        day = first%100
        d0 = self.from_JHU_date(first)
        d1 = self.from_JHU_date(last)
        daterange=[]
        n0 = d0.toordinal()
        n1 = d1.toordinal()
        while d0<=d1:
            daterange += [self.to_JHU_date(d0)]
            n0+=1
            d0 = d0.fromordinal(n0)
        return daterange
    
    def to_JHU_date(self,d):
        return int(str(d.year)+('0' if d.month<10 else "")+str(d.month)+("0" if d.day<10 else "")+ str(d.day))
    
    def from_JHU_date(self,d):
        year = d//10000
        month = (d%10000)//100
        day = d%100
        d0 = datetime.date(year,month,day)
        return d0
    
    def convertDate(self,s):
        s=s.split('/')
        mon=int(s[0])
        day = int(s[1])
        year = int(s[2])
        if year<2000:
            year += 2000
        return int(str(year)+('0' if mon<10 else "") + str(mon)+('0' if day<10 else "")+str(day))

    
        
    
    def getStateData(self,state,field,first,last):
        ''' returns list of tuples (date,value) for that field and that state, ordered by date'''
  
        daterange = self.genDateRange(first,last)
        sd = {x['date']:self._getField(x,field) 
                  for x in self.us_covid_data 
                  if x['state'] == state 
                     and x['date'] in daterange} 
        sd2 =[sd.get(d,0) for d in daterange]
        return sd2
        #return VA.clamp(sd2,0,max(sd2))
        
      
    def getStateVacData(self,state,field,first,last):
        ''' returns list of tuples (date,value) for that field and that state, ordered by date'''
  
        daterange = self.genDateRange(first,last)
        sd = {x['date']:self._getField(x,field) 
                  for x in self.us_vac_data 
                  if x['stabbr'] == state 
                     and x['date'] in daterange} 
        #print(sd)
        sd1 =[sd.get(d,0) for d in daterange]
        sd2 = [0 if x=="" or x==None else int(x) for x in sd1]
        return VA.partialMaxs(sd2)
        #return VA.clamp(sd2,0,max(sd2))

    def getUSData(self,field,first,last):
        ''' returns list of tuples (date,value) for that field and that state, ordered by date'''
  
        daterange = self.genDateRange(first,last)
        normalize = lambda x: 0 if x=="" or x==None else int(x)
        
        sd = {}
        for d in daterange:
            vacs = [normalize(self._getField(x,field))
                        for x in self.us_covid_data 
                        if x['date']==d 
                        and x['state'] in States.stateAbbrs.values()]
            #print(d,vacs)
            sd[d] = sum(vacs)
        
        sd1 =[sd.get(d,0) for d in daterange]
        return sd1
  

    def getUSVacData(self,field,first,last):
        daterange = self.genDateRange(first,last)
        #print(daterange)
        #print(States.stateAbbrs.values())
        normalize = lambda x: 0 if x=="" or x==None else int(x)
        sd = {}
        for d in daterange:
            vacs = [normalize(self._getField(x,field))
                        for x in self.us_vac_data 
                        if x['date']==d 
                        and x['stabbr'] in States.stateAbbrs.values()]
            #print(d,vacs)
            sd[d] = sum(vacs)
        
            
        #print('sd',sd)

        sd1 =[sd.get(d,0) for d in daterange]
        return VA.partialMaxs(sd1)

    def byState(self,state,field,options):
        first = options.get('first',self.first_date)
        last  = options.get('last',self.last_date)
        data = self.getStateData(state,field,first,last)
        return data
    
    def vacByState(self,state,field,options):
        first = options.get('first',self.first_date)
        last  = options.get('last',self.last_date)
        data = self.getStateData(state,field,first,last)
        return data
    
    def byStates(self,states,field):
        return {state:self.byState(state,field) for state in states}
    
    def byRegion(self,region,field):
        return VA.addLists(self.byState(state,field) for state in region)

    def byRegions(self,regions,field):
        ''' takes a dictionary of {name:states} and returns a dictionary {name:regiondata} '''
        return {name:self.byRegion(regions[name],field) for name in regions.keys()}

    # the rest of this class is old stuff...
    
    def getStateDataPerCapita(self,k,state,field):
        ''' returns list of tuples (date,value) for that field and that state, ordered by date'''
        # I should rewrite this using VectorAlgebra on the raw data ...
        pop = States.statePop(state)
        sd1 = self.getStateData(state,field)
        return VA.scale(k/pop,sd1)
    


    def getRegionData(self,states,field):
        return VA.addLists(
           [self.getStateData(state,field) for state in states])
    
    def getRegionDataPerCapita(self,k,states,field):
        # I should rewrite this using VectorAlgebra on the raw data ...
        d = self.getRegionData(states,field)
        pop = States.regionPop(states)
        d2 = [x/pop*k for x in d]
        return d2
    
    def getOrd(self,n):
        ''' return the number of days since 1/1/2020 represented by the CovidDate n as an integer YYYYMMDD '''
        aord = datatime.date(2020,1,1).toordinal()
        year=n//10000
        n=n%10000
        mon=n//100
        day=n%100
        return datetime.date(year,mon,day).toordinal() - aord




