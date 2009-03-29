import cgi
import os
from google.appengine.ext import webapp
from cachecontrol import cache
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
import logging
from client import Resource

class SetGears(webapp.RequestHandler): 

	def post(self):
		clientCookie = self.request.cookies.get('BigKahuna', '')
		gearsenabled = self.request.get('gearsenabled')
		gears = cache()
		templist = gears.get("clientlist")
		if templist == None:
			self.response.out.write("No clients yet")
		else:
			logging.info("Inside else")
			for obj in templist:
				logging.info("Inside for")
				if obj.cookie == int(clientCookie):
					logging.info("Inside else for if")
					obj.gearsenabled = gearsenabled
					templist.remove(obj)
					templist.append(obj)
					gears.replace("clientlist",templist)
					self.response.out.write("Replaced list")

		self.response.out.write("gears enabled:" + gearsenabled)


application = webapp.WSGIApplication(
                                     [('/setgears', SetGears)],                                     
                                     debug=True)
def main():
  run_wsgi_app(application)  
  
if __name__ == "__main__":
  main()
