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
             logging.eror("added to cache")
    
        else:
            logging.error("item already in cache")
            settingsInCache = mycache.get("settings")
            path = os.path.join(os.path.dirname(__file__), 'templates/settings.html')
            dictSettings = {}
            dictSettings['dataset_name'] = settingsInCache.dataset_name
            logging.error(dictSettings['dataset_name'])
            self.response.out.write(template.render(path, dictSettings))
            
            
    def createSettings(self,settingsInCache):
        #settingsInCache.set_dataset_name("default")
        #settingsInCache.set_no_of_items_in_cache("1000")
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
        