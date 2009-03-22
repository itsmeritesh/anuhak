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
	     self.redirect("/settings")
	     
        else:
            settingsInCache = mycache.get("settings")
	    settingsInCache = self.createSettings(settingsInCache)
	    mycache.replace("settings",settingsInCache)
            path = os.path.join(os.path.dirname(__file__), 'templates/settings.html')
            dictSettings = {}
            dictSettings['dataset_name'] = settingsInCache.dataset_name
	    dictSettings['no_items'] = settingsInCache.no_of_items_in_cache
            dictSettings['workflow_type'] = settingsInCache.type_of_workflow
            logging.error(dictSettings['dataset_name'])
            self.response.out.write(template.render(path, dictSettings))    

    def createSettings(self,settingsInCache):
        dataset_name = self.request.get('dataset')
        number_items = self.request.get('no_cache')
        type_of_workflow = self.request.get('workflow_type')
        
    	if not dataset_name:
    		if settingsInCache.dataset_name=="":
    			settingsInCache.set_dataset_name("default")
    	else:
    	    settingsInCache.set_dataset_name(dataset_name)
    	    
    	if not number_items:
    		if not settingsInCache.no_of_items_in_cache:
    			settingsInCache.set_no_of_items_in_cache("1000")
    	else:
    	    settingsInCache.set_no_of_items_in_cache(number_items)
    	    
        if not type_of_workflow:
        	if settingsInCache.type_of_workflow=="":
        		settingsInCache.set_type_of_workflow("gears")
        else:
            settingsInCache.set_type_of_workflow(type_of_workflow)         
         
    	return settingsInCache
        

class SettingsInCache:
    dataset_name =""
    no_of_items_in_cache = None
    type_of_workflow = ""
    
    def set_dataset_name(self,in_name):
        self.dataset_name = in_name
        
    def set_no_of_items_in_cache(self,in_items):
        self.no_of_items_in_cache = in_items
        
    def set_type_of_workflow(self,in_type):
        self.type_of_workflow = in_type        

application = webapp.WSGIApplication(
                                     [('/settings', Settings)],                                     
                                     debug=True)


def main():
  run_wsgi_app(application)
  
  
if __name__ == "__main__":
  main()
        
