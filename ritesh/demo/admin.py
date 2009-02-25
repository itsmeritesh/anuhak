import cgi
from cachecontrol import cache
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class Admin(webapp.RequestHandler):
	def get(self):
		admin= AdminData()
		self.response.out.write(admin.get())
		
	


class AdminData():
	""" Holds the current state of the application
	"""
	currentStatus = "inactive"
	
	"""
	 initializes the currentStatus to initialized and adds itself to the cache
	"""
	def initialize(self):
		if self.getStatus() != "inactive" :
			currentStatus = "initialized"
		cc = cache()
		cc.put("admin_data",self)
	
	"""
	Gets the current status of the application from this object
	Returns:
		currentStatus of the object
	"""	
	def getStatus(self):
		cc = cache()	
		admin_object = cc.get("admin_data")
		if not admin_object:
			return None
		else:
			return admin_object.currentStatus
	
	
	"""
	Changes the status of the application to the newStatus
	"""
	def changeStatus(self,newStatus):
		currentStatus = newStatus
		cc = cache()
		cc.replace("admin_data",self)	
	
	def get(self):
		if not self.getStatus():
			return "Application not yet initialized"
		
		
			

application = webapp.WSGIApplication(
                                     [('/admin', Admin)],                                     
                                     debug=True)
def main():
  run_wsgi_app(application)  
  
if __name__ == "__main__":
  main()
