from google.appengine.ext import db
from definemap import Maplet
from cachecontrol import cache

class CacheMapStore:
    
    maplist = None
    number_items = 1000
    offset = 0
    iterator = 0
    type = None
    query = None
    tablename = None
    maps = None

    def __init__(self,type,number,tablename,offset):
        self.offset = offset
        self.number_items = number
        self.tablename = tablename
        self.type = type
        query ="select * from "self.tablename+" where dataset_name = '"+self.type+"'"
        self.query = query
        self.maps=db.GqlQuery(self.query)
        results=self.maps.fetch(self.number_items,self.offset) 
        retval = self.populate(results)
        self.maplist = maps
        mycache = cache()
        mycache.put("mapcount",len(maplist))
        if not mycache.get("mapoffset"):
            mycache.put("mapoffset",0)
        else:
            mapoffset = mycache.get("mapoffset")
            mapoffset = mapoffset+1000
            mycache.put("mapoffset",mapoffset)
        
        
    def populate(self,results):
        maps = []
        for onemap in results:
            maplet = Maplet()
            maplet.uniqueid = int(onemap.uniqueid)
            maplet.dataset_name = str(onemap.dataset_name)
            maplet.dated = str(onemap.dated)
            maplet.text = str(onemap.text)
            maplet.filename = str(onemap.filename)
            maps.append(maplet)
        return maps
    
        
        

    
            
            
        
        
        
        
        
    
