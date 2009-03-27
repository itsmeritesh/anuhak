from map import CacheMapStore
from cachecontrol import cache
import logging
class Maploader:
    
    mycache = None
    offset = None
    mapstore = None
    type = None
    number_items = 10

    def __init__(self,type):
        self.mycache = cache()
        self.offset  = 0
        self.type = type
        self.start()

    def start(self):
        
        #check if Mapstore is in the cache
        retval = self.mycache.get("store")
        if retval == None:
            self.callput()

    def callput(self):
        #call map make mapstore and put
        self.mapstore = CacheMapStore(self.type,self.number_items,"Map",0)
        self.mycache.put("store", self.mapstore.maplist)
        self.mycache.put("mappos",0)
        
    def getmap(self):
        
        #gets a simgle item from the head of list and return to caller
        
        maplist = self.mycache.get("store")
        pos = self.mycache.get("mappos")
        if pos  >= self.mycache.get("mapcount"):
            
            logging.info("check")
            #make new mapstore with new indexes and replace in cache
            mapstore = CacheMapStore(self.type,self.number_items,"Map",self.mycache.get("mapoffset"))
            self.mycache.replace("store",mapstore.maplist)
            self.mycache.replace("mappos",0)
            maplist=mapstore.maplist
            pos = 0
        print pos
        try:
            item = maplist[pos]
        except IndexError:
            return None
        pos =pos+1
        self.mycache.replace("mappos",pos)
        return item
            
    def cleanup(self):
        self.mycache.delete("store")
        self.mycache.delete("mappos")
        self.mycache.delete("mapoffset")
        self.mycache.delete("mapcount")
