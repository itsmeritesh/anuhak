import cgi
from maptokenmanager import maptokenmanager
from maploader import Maploader
from admin import AdminData
from cachecontrol import cache
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class GetData(webapp.RequestHandler):
    """
     this is mostly a post call but get is used to test whether its working
    """
    
    def get(self):
        clientCookie = self.request.cookies.get('BigKahuna', '')
        maploader = Maploader("blogs")
        map = maploader.getmap()         
        
        #add to maptokenmapping
        mtmanager = maptokenmanager()
        #mtmanager.putMapToken(map,clientCookie)
        workflow_type = self.getWorkflowType()
        
        if not map:
            admin = AdminData()
            if workflow_type=="gears":
            	admin.changeStatus("gearsmapreduce")
            else:
            	admin.changeStatus("reduce")
        else:
            self.response.out.write("{ \"data\": \"" + map.text +"\", \"id\":" + str(map.uniqueid) + "}")    


    """
    gets the workflow type from the settings file
    """
    def getWorkflowType(self):    	
    	mycache = cache()
    	if not mycache.get("settings"):
		settingsInCache = SettingsInCache()
	else:
		settingsInCache = mycache.get("settings")
	workflow_type = settingsInCache.type_of_workflow
	return workflow_type
		
    def post(self):
        clientCookie = self.request.cookies.get('BigKahuna', '')
        maploader = Maploader("blogs")
        map = maploader.getmap()         
        
        #add to maptokenmapping if type is non gears
        workflow_type = self.getWorkflowType()
        if workflow_type=="pure":
        	mtmanager = maptokenmanager()
        	mtmanager.putMapToken(map,clientCookie)

        
        if not map:
            admin = AdminData()
            if workflow_type=="gears":
            	admin.changeStatus("gearsmapreduce")
            else:
            	admin.changeStatus("reduce")
        else:
            self.response.out.write("{ \"data\": \"" + map.text +"\", \"id\":" + str(map.uniqueid) + "}")    


application = webapp.WSGIApplication(
                                     [('/getdata', GetData)],                                     
                                     debug=True)


def main():
  run_wsgi_app(application)
  
  
if __name__ == "__main__":
  main()
        
