from map import CacheMapStore
from cachecontrol import cache

class Maploader:
    
    mycache = None
    offset = None
    mapstore = None
    type = None
    number_items = 1000

    def __init__(self,type):
        self.mycache = cache()
        self.offset  = 0
        self.type = type
        start()

    def start(self):
        
        #check if Mapstore is in the cache
        retval = mycache.get("store")
        if retval == None:
            callput()

    def callput(self):
        #call map make mapstore and put
        self.mapstore = CacheMapStore(self.type,self.number_items,"Map",0)
        mycache.put("store", mapstore.maplist)
        mycache.put("mappos",0)
        
    def getmap(self):
        
        #gets a simgle item from the head of list and return to caller
        
        maplist = mycache.get("store")
        pos = mycache.get("mappos")
        item = maplist[pos]
        pos =pos+1
        mycache.replace("mappos",pos)
        
        if pos >= mycache.get("mapcount"):
            #make new mapstore with new indexes and replace in cache
            self.mapstore = CacheMapStore(self.type,self.number_items,"Map",mycache.get("mapoffset"))
            mycache.replace("store",self.mapstore)
        
        return item
            
