from map import CacheMapStore
from maploader import Maploader
from cachecontrol import cache
from settings import SettingsInCache
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

class clientTokenMap:
    token=-1
    maps=""
        
    

class maptokenmanager:
    
    mapTokenMapping = {}
    workflow_type = ""
    
    def __init__(self):
        mycache = cache()
        dic = mycache.get("maptokenmanager")
        if  dic== None:
	    mapTokenMapping = {}        	
            mycache.put("maptokenmanager",mapTokenMapping)
            logging.info("added maptoken manager to cache")
                
        if not mycache.get("settings"):
             settingsInCache = SettingsInCache()
        else:
            settingsInCache = mycache.get("settings")
        workflow_type = settingsInCache.type_of_workflow
             
    def requeueForToken(self,inMap):
    	ml=maploader()
    	ml.map = inMap
    	logging.info("requeueing map for some token")
    	#ashwins new function    	
    	
    def removeMapToken(self,inToken):
        mycache = cache()
        dic = mycache.get("maptokenmanager")
        if not dic:
            logging.error("maptokenmanager not found in removeMapToken")
        if(dic.has_key(inToken)):
            dic.pop(inToken)
            mycache.replace("maptokenmanager",dic)
            
    
    def putMapToken(self,inMap,inToken):
        mycache = cache()
        dic = mycache.get("maptokenmanager")
        if  dic==None:
            logging.error("maptokenmanager not found in putMapToken")
        if dic.has_key(inToken):
            existingClient = dic.pop(inToken)
            self.requeueForToken(existingClient.map)
            dic[inToken]=inMap        
                                    
        else:
            newClient = clientTokenMap()
            newClient.token = inToken
            newClient.map= inMap
            dic[inToken] = newClient
        mycache.replace("maptokenmanager",dic)
        

        
