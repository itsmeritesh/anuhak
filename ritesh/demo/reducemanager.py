from cachecontrol import cache
from classdefs import resultlet


class reducequeue:

   count = 0
   reduce_cache = None
   reducelist = []

   def __init__(self):
       self.reduce_cache = cache()
       self.reduce_cache.put("resultlist",self.reducelist)

   def put(self,id,resultdata):
       result = resultlet()
       result.token = id
       result.data = resultdata
       self.reducelist = self.reduce_cache.get("resultlist")
       self.reducelist.append(result)
       self.reduce_cache.replace("resultlist",self.reducelist)



class reducemanager:


   mycache = None

   def __init__(self,number):
       self.mycache = cache()


   def getreduceitems(self,number):
       returnlist = []
       templist=self.mycache.get("resultlist")
       if len(templist) == 0:
           self.mycache.delete("resultlist")
           returnlist = None
           return returnlist
           #list is empty

       for i in range(1,number):
           try:
               returnlist.append(templist.pop(0))
           except:
               #maybe we are done with the list
               if len(returnlist) == 0:
                   #now we have an empty list
                   returnlist = None
                   self.mycache.delete("resultlist")
                   return returnlist

       self.mycache.replace("resultlist",templist)
       return returnlist
