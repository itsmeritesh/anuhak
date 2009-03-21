import cgi
from cachecontrol import cache
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
import logging
import os

class Settings(webapp.RequestHandler):
    def get(self):
	mycache = cache()
        if not mycache.get("settings"):
             settingsInCache = SettingsInCache()
	     settingsInCache = self.createSettings(settingsInCache)
	     mycache.put("settings",settingsInCache)
             logging.error("added to cache")
	     self.response.out.write("Created and Read Settings. Please Reload the page to view/change settings")
	     
        else:
            logging.error("item already in cache")
            settingsInCache = mycache.get("settings")
	    settingsInCache = self.createSettings(settingsInCache)
            path = os.path.join(os.path.dirname(__file__), 'templates/settings.html')
            dictSettings = {}
            dictSettings['dataset_name'] = settingsInCache.dataset_name
	    dictSettings['no_items'] = settingsInCache.no_of_items_in_cache
            logging.error(dictSettings['dataset_name'])
            self.response.out.write(template.render(path, dictSettings))    

    def createSettings(self,settingsInCache):
	dataset_name = self.request.get('dataset')
	number_items = self.request.get('no_cache')
	if dataset_name == "":
	    settingsInCache.set_dataset_name("default")
	else:
	    settingsInCache.set_dataset_name(dataset_name)
	if number_items == "":
	    settingsInCache.set_no_of_items_in_cache("1000")
	else:
	    settingsInCache.set_no_of_items_in_cache(number_items)
	return settingsInCache
        

class SettingsInCache:
    dataset_name ="default"
    no_of_items_in_cache = 1000
    
    def set_dataset_name(self,in_name):
        self.dataset_name = in_name
        
    def set_no_of_items_in_cache(self,in_items):
        self.no_of_items_in_cache = in_items
        
    
            
        
    
       
         
        
        

application = webapp.WSGIApplication(
                                     [('/settings', Settings)],                                     
                                     debug=True)


def main():
  run_wsgi_app(application)
  
  
if __name__ == "__main__":
  main()
        