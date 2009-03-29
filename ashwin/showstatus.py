from google.appengine.ext import db
from cachecontrol import cache
from admin import AdminData 

class status:

    mycache = None 
    token = None

    def __init(self):
        self.mycache = cache()

    def datstoremapcount():
        count  = mycache.get("mapcount")
        return count
        
    def cachemapstat(self):
        
        maplist = self.mycache.get("store")
        pos =  self.mycache.get("mappos")
        self.token = maplist[pos].uniqueid
        return maplist[pos]


    def resultcount(self):
        resultlist =self. mycache.get("resultlist")
        return len(resultlist)
    

    def whatsgoinon(self):
        admindata = AdminData()
        return admindata.getStatus()
        
    
    def resultobject():
        #returns latest result
        reslist = self.mycache.get("resultlist"0
        return reslist[-1].data


        
                 
        
        
    
    
    
    
