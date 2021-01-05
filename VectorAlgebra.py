''' Vector Algebra is a module of useful functions operating on list of numbers '''

def averageByK(k,data):
        ''' return the average of the previous k elements of the list assuming all values before the beginning are zero'''
        d = [0]*(k-1) + data
        avg = [sum(d[i:i+k])/k for i in range(len(data))]
        return avg
    
def addLists(lists):
        ''' given a list of lists of the same length, add them component-wise, e.g.
            addLists([[1,2,3],[5,6,7]]) ==> [6,8,10]
            addList([[1,2,3],[1,1,1],[100,1000,1000000]) ==> [102, 1003, 1000004]
            This will be used to combine the timeseries data from several sources ...
        '''
        result=[]
        x0 = lists[0]
        for i in range(len(x0)):
            s=0
            for x in lists:
                s = s+ x[i]
            result += [s]
        return result

def partialMaxs(data):
    total = 0
    result=[]
    for x in data:
        if (x>total):
            total=x
        result += [total]
    return result
    
def divLists(listA,listB):
        ''' return the component-wise quotient of elements of listA by elements of listB
            return 0 if the denominator is 0
        '''
        listC = [listA[i]/listB[i] if listB[i]>0 else 0 for i in range(len(listA))]
        return listC

def clamp(listA,lo,hi):
        return [min(hi,max(lo,a)) for a in listA]

def changeByK(k,listA):
        z = [listA[i]-listA[i-k] for i in range(k,len(listA))]
        return listA[:k]+z

def shiftByK(k,listA):
        if k>0:
            return [0]*k+listA[:-k]
        else:
            return listA[-k:]+[listA[-1]]*(-k)

def scale(c,listA):
        return [c*x for x in listA]




        
    



        
