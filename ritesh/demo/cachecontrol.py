from google.appengine.api import memcache
import logging

class cache():

	TIMEOUT = 10000	
	
	def get(self,key):
		""" getValue 		
		gets the value for the given key
		Returns:
			the value of object identified by the key or None
		"""		
		data = memcache.get(key)
 		if data is not None:
 			return data
 		else:
 			return None
 		
 		
 	def put(self,key,value):
 		"""put
 		Puts the value into the cache identified by key for TIMEOUT period of time
 		Returns:
 			boolean value whether the insert was successful or not
 		"""
 		global TIMEOUT
 		if not memcache.add(key,value,self.TIMEOUT):
 			logging.error("Couldn't add to cache - key" + str(key) + " value=" + str(value))
 			return False 
 		else:
 			return True
 		
 		
 	def delete(self,key):
 		""" delete
 		 deletes the value specified by the given key.
 		 Returns:
 		 	true if delete is successful. false otherwise
 		"""
 		if memcache.delete(key) > 1:
 			return True
 		else:
 			logging.error("Couldn't delete record from cache for key " + str(key))
 			return False
 		
 	def replace(self,key,value):
 		 """ replace
 		 replaces the value of the  object identified by key in the cache. fails if object not already present
 		 Returns:
 		 	true if replaced successfully . false otherwise
 		 """
 		 global TIMEOUT
 		 if not memcache.replace(key,value,self.TIMEOUT):
 		 	logging.error("Couldn't replace value of key:" + str(key))
 		 	return False
 		 else:
 		 	return True
 		 
 	def set(self,key,value):
 		 """ set
 		 sets the value of the object in the cache identified by key irrespective of its previos state
 		 Returns:
 		 	True if value is set, false otherwise.
 		 """
 		 if not memcache.set(key,value,self.TIMEOUT):
 		 	logging.error("couldn't set value for key "+str(key))
 		 	return False
 		 else:
 		 	return True
 		 	
 		 	
 		
 		
 		
 		
 		
