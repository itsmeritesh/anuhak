from cachecontrol import cache
from classdefs import resultlet


class reducequeue:
    
    count = 0
    reduce_cache = None
    getcount =0

    def __init__(self):
        self.reduce_cache = cache()
    
    def put(self,id,resultdata):
        result = resultlet()
        result.token = id
        result.data = resultdata
        self.count = self.count+1
        self.reduce_cache.put("result"+str(self.count),result)
    
        

class reducemanager:
    
    getcount = None
    
    def __init__(self):
        self.getcount = 1
    
    
    def getreduceitems(self,number):
        returnlist = []
        count = 0
        for i in range(1,number):
            item=self.reduce_cache.get("result"+str(self.getcount+(i-1)))
            if item == None:
            #reduce pairs done
                return -1
            returnlist.append(item)
            
        self.getcount = self.getcount + number
        return returnlist
        
        
    
        

        
         
