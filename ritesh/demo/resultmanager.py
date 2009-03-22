import cgi
from google.appengine.ext import webapp
from cachecontrol import cache
from google.appengine.ext.webapp.util import run_wsgi_app
from cachecontrol import cache
from reducemanager import reducequeue
from reducemanager import reducemanager
import logging

class resultmanager(webapp.RequestHandler):
  def post(self):
      resultType = self.request.get('resulttype')
      clientCookie = self.request.cookies.get('BigKahuna', '')
      result = self.request.get('result')
      reduceQueue = reducequeue()
      reduceQueue.put(clientCookie,result)
      logging.info("Map result received" + resultType + ":" + result)

      


application = webapp.WSGIApplication(
                                     [('/resultmanager', resultmanager)],
				     debug=True)
def main():
  run_wsgi_app(application)  
  
if __name__ == "__main__":
  main()

