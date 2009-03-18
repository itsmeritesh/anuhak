from map import CacheMapStore
from maploader import Maploader
from cachecontrol import cache
import logging

class datatokenpair:
    uniqueId="";    
    token=-1;
    
    def __init__(self,inuniqueid,intoken):
        self.uniqueId = inuniqueid 
        self.token = intoken
    
    def getId(self):
        return self.uniqueId
    
    def getToken(self):
        return self.token 


class maptokenmanager:
    
    mapTokenMapping = {}
    
    def __init__(self):
        mycache = cache()
        if not mycache.get("maptokenmanager"):
            mycache.put("maptokenmanager",self)
        
    def removeMapToken(self,inToken):
        mycache = cache()
        dict = mycache.get("maptokenmanager").mapTokenMapping
        if not dict:
            logging.error("maptokenmanager not found in removeMapToken")
        if(dict.has_key(inToken)):
            dict.pop(inToken)
            mycache.replace("maptokenmanager",self)
            
    
    def putMapToken(self,inMap,inToken):
        mycache = cache()
        dict = mycache.get("maptokenmanager").mapTokenMapping
        if not dict:
            logging.error("maptokenmanager not found in removeMapToken")
        if dict.has_key(inToken):
            print "write fault tolerance code here"
        else:
            dict[inToken] = inMap
        mycache.replace("maptokenmanager",self)
        

        