import cgi
from google.appengine.ext import webapp
from cachecontrol import cache
from google.appengine.ext.webapp.util import run_wsgi_app
from cachecontrol import cache
from reducemanager import reducequeue
from reducemanager import reducemanager
from maptokenmanager import maptokenmanager
import logging

class resultmanager(webapp.RequestHandler):
  def post(self):
      resultType = self.request.get('resultType')
      clientCookie = self.request.cookies.get('BigKahuna', '')
      result = self.request.get('result')
      id= self.request.get('id')
      reduceQueue = reducequeue()
      reduceQueue.put(id,result)
      if resultType=="map":
        #remove from maptoken manager
        mtm = maptokenmanager()
        mtm.removeMapToken(clientCookie)
      	logging.info("Map result received" + resultType + ":" + result)
      else:
      	mycache = cache()
        curresult = int(mycache.get("reduceresult"))
        if curresult == None:
        	mycache.put("reduceresult",result)
        else:
        	curresult = result + curresult 
        	mycache.replace("reduceresult",curresult)
        	
      	logging.info("Reduce result received:" + result) 
      	

      


application = webapp.WSGIApplication(
                                     [('/resultmanager', resultmanager)],
				     debug=True)
def main():
  run_wsgi_app(application)  
  
if __name__ == "__main__":
  main()

