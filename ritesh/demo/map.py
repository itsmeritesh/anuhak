from google.appengine.ext import db
from definemap import Maplet
from cachecontrol import cache
import logging
class CacheMapStore:
    
    maplist = None
    number_items = 10
    offset = 0
    iterator = 0
    type = None
    query = None
    tablename = None
    maps = None

    def __init__(self,type,number,tablename,offset):

        mycache = cache()
        if mycache.get("mapoffset") == None :
            mycache.put("mapoffset",0)
            logging.info("inside ljlkjljljjljjklk")
        else:
            logging.info("inside dkashdkashdkashd")
            mapoffset = mycache.get("mapoffset")
            mapoffset = int(mapoffset)+10
            mycache.replace("mapoffset",mapoffset)
            self.offset = mapoffset
        logging.info("this is called"+str(self.offset))
        
        self.number_items = number
        self.tablename = tablename
        self.type = type
        query ="select * from "+self.tablename+" where dataset_name = '"+self.type+"'"
        logging.info(query)
        self.query = query
        self.maps=db.GqlQuery(self.query)
        logging.info("fetching "+ str(self.number_items) + " starting from "+ str(self.offset))
        results=self.maps.fetch(self.number_items,self.offset)
        retval = self.populate(results)
        self.maplist = retval
        if not mycache.get("mapcount"):
           mycache.put("mapcount",len(self.maplist))
        else:
           mycache.replace("mapcount",len(self.maplist))
            
        
        
    def populate(self,results):
        maps = []
        for onemap in results:
            logging.info("inside populate")
            maplet = Maplet()
            maplet.uniqueid = int(onemap.uniqueid)
            maplet.dataset_name = str(onemap.dataset_name)
            maplet.dated = str(onemap.dated)
            maplet.text = str(onemap.text)
            maplet.filename = str(onemap.filename)
            maps.append(maplet)
        return maps
    
        
        

    
            
            
        
        
        
        
        
    
