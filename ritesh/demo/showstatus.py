from google.appengine.ext import db
from cachecontrol import cache


		

class status:

    mycache = None 
    token = None

    def __init(self):
        self.mycache = cache()

    def datstoremapcount(self):
    	self.mycache = cache()
        count  = self.mycache.get("mapcount")
        return count
        
    def currentmapcount(self):
    	self.mycache = cache()
    	offset = self.mycache.get("mapoffset")
        pos =  self.mycache.get("mappos")	
        return pos+offset


    def resultcount(self):
    	self.mycache = cache()
        resultlist =self. mycache.get("resultlist")
        if resultlist== None:
        	return 0
        else:
        	return len(resultlist)
    

    def whatsgoinon(self):
        #self.mycache = cache()
        #admin_data =self.mycache.get("admin_data")
        #return admin_data.currentStatus
        return ""

        
    
    def resultobject(self):
        #returns latest result
        self.mycache = cache()
        reslist = self.mycache.get("reduceresult")
        if reslist == None:
        	return "0"
        else:
        	return reslist


        
                 
        
        
    
    
    
    
