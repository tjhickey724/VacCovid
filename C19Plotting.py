''' this contains utilities to make plotting of the covid data easier '''

import matplotlib.pyplot as plt
    
monthnames="Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(" ")
    
def xticks(daterange):
        ''' daterange is the integers of the form YYYYMMDD 
            we will have a tick at each month (i.e. ending in 01) fe
        '''
        ticknums=[]
        ticknames=[]
        for i in range(len(daterange)):
            d=daterange[i]
            if d%100==1:
                ticknums+=[i]
                mon = (d//100)%100
                ticknames += [monthnames[mon-1]]
        plt.xticks(ticknums,ticknames)
