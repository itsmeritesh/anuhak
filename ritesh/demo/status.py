import cgi
from cachecontrol import cache
from admin import AdminData
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class Status(webapp.RequestHandler):
	def post(self):
		self.response.out.write(self.getCurrentStatus())
		
	
	def getCurrentStatus(self):
		admin_data = AdminData()
		return admin_data.get()
	
	
	
	def get(self):
		self.response.out.write(self.getCurrentStatus())
		#self.response.out.write("Post only with Identification Token")


application = webapp.WSGIApplication(
                                     [('/status', Status)],                                     
                                     debug=True)
def main():
  run_wsgi_app(application)  
  
if __name__ == "__main__":
  main()
