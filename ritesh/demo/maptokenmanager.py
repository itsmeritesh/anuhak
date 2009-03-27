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

class client:
    token=-1
    maps=[]
    
    def addMap(self,mapId):
        maps.append(mapId)
    

class maptokenmanager:
    
    mapTokenMapping = {}
    workflow_type = ""
    
    def __init__(self):
        mycache = cache()
        if not mycache.get("maptokenmanager"):
            mycache.put("maptokenmanager",self)        
                
        if not mycache.get("settings"):
             settingsInCache = SettingsInCache()
        else:
            settingsInCache = mycache.get("settings")
        workflow_type = settingsInCache.type_of_workflow
             
        
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
            existingClient = dict[inToken]
            existingClient.addMap(inMap)
                                    
        else:
            newClient = client()
            newClient.token = inToken
            newClient.addMap(inMap)
            dict[inToken] = newClient
        mycache.replace("maptokenmanager",self)
        

        