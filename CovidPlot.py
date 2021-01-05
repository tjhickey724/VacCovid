'''
   CovidPlot is a class which inherits from CovidData and ListOps and provides several plotting methods for Covid19 data
   Pedagogically, this gives an example of multiple inheritance... objects in the CovidPlot class have all of the 
   variables and methods defined in CovidData and in ListOps
'''
import matplotlib.pyplot as plt
import datetime

from CovidTracking import CovidData
from ListOps import ListOps

class CovidPlot(CovidData,ListOps):
    '''  
      CovidPlot is a class that inherits from CovidData and ListOps,
         and adds a bunch of plotting methods to plot Covid data for 2020
      Note that we inherit all the methods from CovidData and from ListOps!
      This is an example of Code Reuse.  The CovidData could be used in other applications as could the ListOps
      We are putting them in separate modules so they can be used by other Modules!
    '''
    
    def __init__(self):
        ''' initialize the object to have all of the methods and fields of the CovidData class '''
        super().__init__() # initialize the CovidData class, includes loading in the data!
        self.width=12
        self.height=12

    def plotState(self,state,field = 'hospitalizedCurrently'):
        '''  plot the 2020 data for the state and the specified field, e.g. "deathIncrease"  '''
        plt.rcParams['figure.figsize'] = [self.width,self.height]
        data = self.getStateData(state,field)
        plt.plot(data)
        plt.grid()
        plt.title(state+": "+field)
        self.addMonthLabels()

    def plotStateAvg(self,state,field = 'hospitalizedCurrently',k=7):
        '''  plot the 2020 data for the state and the specified field, e.g. "deathIncrease"  '''
        plt.rcParams['figure.figsize'] = [self.width,self.height]
        data = self.getStateData(state,field)
        data = self.averageByK(k,data)
        plt.plot(data)
        plt.grid()
        plt.title(state+": "+field+" averaged over "+str(k)+" days")
        self.addMonthLabels()
    
    def plotStates(self,states,field = 'hospitalizedCurrently'):
        '''  plot the 2020 data for the state and the specified field, e.g. "deathIncrease"  '''
        plt.rcParams['figure.figsize'] = [self.width,self.height]
        for state in states:
            data = self.getStateData(state,field)
            data = self.averageByK(k,data)
            plt.plot(data,label=state)
        plt.grid()
        if len(states)<10:
            plt.legend(states)
            plt.title(str(states)+": "+field+" averaged over "+str(k)+" days")
        else:
            plot.title('Covid19 data for '+field)
        self.addMonthLabels()

    def plotStatesAvg(self,states,field = 'hospitalizedCurrently',k=7):
        '''  plot the 2020 data for the state and the specified field, e.g. "deathIncrease"  '''
        plt.rcParams['figure.figsize'] = [self.width,self.height]
        for state in states:
            data = self.getStateData(state,field)
            plt.plot(data,label=state)
        plt.grid()
        if len(states)<10:
            plt.legend(states)
            plt.title(state+": "+field)
        else:
            plot.title('Covid19 data for '+field)
        self.addMonthLabels()
        
    
    def addMonthLabels1(self):
        plt.xticks([0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366],'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec Jan'.split(' '))

    def addMonthLabels(self):
        days1 = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335];
        months = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split(' ')
        days2 = [x+366 for x in days1] 
        plt.xticks(days1+days2,months+months)  
        
    def plotStateDataPerCapita(self,state,field,N):
        ''' plots the specified perCapita data for a state for the entire year to date stating an 1/1/2020 for every N residents '''
        '''  plot the 2020 data for the state and the specified field, e.g. "deathIncrease"  '''
        plt.rcParams['figure.figsize'] = [self.width,self.height]
        data = self.getStateDataPerCapita(N,state,field)
        plt.plot(data)
        plt.grid()
        plt.title(state+": "+field)
        self.addMonthLabels()
    
    def plotStateDataPerCapitaAvg(self,state,field,N,K):
        ''' plots the specified perCapita data for a state for the entire year to date stating an 1/1/2020 for every N residents '''
        return

        
    def plotStatesDataPerCapita(self,states,field,N):
        ''' plots the specified perCapita data for a list of states for the entire year to date stating an 1/1/2020 for every N residents '''
        plt.rcParams['figure.figsize'] = [self.width,self.height]
        for state in states:
            data = self.getStateDataPerCapita(N,state,field)
            plt.plot(data,label=state)
        plt.grid()
        if len(states)<10:
            plt.legend(states)
            plt.title(str(states)+": "+field+" per "+str(N)+" people")
        else:
            plot.title('Covid19 data for '+field)
        self.addMonthLabels()
    
    def plotStatesDataPerCapitaAvg(self,states,field,N,K):
        ''' plots the specified perCapita data for a list of states for the entire year to date stating an 1/1/2020 for every N residents '''
        plt.rcParams['figure.figsize'] = [self.width,self.height]
        for state in states:
            data = self.getStateDataPerCapita(N,state,field)
            data = self.averageByK(K,data)
            plt.plot(data,label=state)
        plt.grid()
        if len(states)<10:
            plt.legend(states)
            plt.title(str(states)+": "+field+" per "+str(N)+" people, averaged "+str(K)+" days")
        else:
            plt.title('Covid19 data for '+field)
        self.addMonthLabels()
    
    def plotRegionsDataPerCapitaAvg(self,regions,field,N,K):
        ''' plots the specified perCapita data for a list of states for the entire year to date stating an 1/1/2020 for every N residents '''
        plt.rcParams['figure.figsize'] = [self.width,self.height]
        for region in regions:
            data = self.getRegionDataPerCapita(N,region,field)
            data = self.averageByK(K,data)
            plt.plot(data,label=region)
        plt.grid()
 
        plt.title('Covid19 data for '+field+' per '+str(N)+' averaged over '+str(K)+' days')
        self.addMonthLabels()

    def plotRegionsDataAvg(self,regions,field,K):
        ''' plots the specified perCapita data for a list of states for the entire year to date stating an 1/1/2020 for every N residents '''
        plt.rcParams['figure.figsize'] = [self.width,self.height]
        for region in regions:
            data = self.getRegionData(region,field)
            data = self.averageByK(K,data)
            plt.plot(data,label=region)
        plt.grid()
 
        plt.title('Covid19 data for '+field+' averaged over '+str(K)+' days')
        self.addMonthLabels()

    def plotRegionsPositivityRate(self,regions):
        ''' plots the region positivity rate '''
        plt.rcParams['figure.figsize'] = [self.width,self.height]
        for region in regions:
            k=7
            pi = self.averageByK(k,self.getRegionDataPerCapita(1000000,region,'positiveIncrease'))
            tt = self.averageByK(k,self.getRegionDataPerCapita(1000000,region,'totalTestResultsIncrease'))
            r = self.averageByK(1,self.clamp(self.divLists(pi,tt),0,1.0))
            plt.plot(self.scaleByC(100,r))
        plt.grid()
        self.addMonthLabels()
        plt.title("positive test rate")
        plt.grid()
        self.addMonthLabels()

        
    def plotPositivityRateState(self,state,k=7):
        plt.rcParams['figure.figsize'] = [self.width,self.height]
        pi = self.averageByK(k,self.getStateData(state,'positiveIncrease'))
        tt = self.averageByK(k,self.getStateData(state,'totalTestResultsIncrease'))
        r = self.averageByK(1,self.clamp(self.divLists(pi,tt),0,1.0))
        plt.plot(r,label=state)
        plt.grid()
        self.addMonthLabels()
        plt.title("positive test rate for "+state)
        
    def plotPositivityRateStates(self,states,k=7):
        plt.rcParams['figure.figsize'] = [self.width,self.height]
        for s in states:
            self.plotPositivityRateState(s,k)
        plt.grid()
        self.addMonthLabels()
        plt.title("positive test rate for "+str(states[:5]))

        

