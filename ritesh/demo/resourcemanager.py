import cgi
import os
from google.appengine.ext import webapp
from cachecontrol import cache
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from client import Resource
from google.appengine.ext.webapp import template

class ResourceManager(webapp.RequestHandler):

  resource_cache = None
  resourcelist = []

  def get(self):
    self.resource_cache = cache()
    self.response.out.write("In Resource Manager")
    self.resourcelist = self.resource_cache.get("clientlist")
    if self.resourcelist == None:
	self.response.out.write("Non clients yet")
    else:
	path = os.path.join(os.path.dirname(__file__), 'templates/resource.html')
	dictSettings = {}
	dictSettings['resources']=self.resourcelist
	self.response.out.write(template.render(path, dictSettings))    

application = webapp.WSGIApplication(
                                     [('/resourcemanager', ResourceManager)],                                     
                                     debug=True)
def main():
  run_wsgi_app(application)  
  
if __name__ == "__main__":
  main()