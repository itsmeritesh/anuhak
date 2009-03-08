import cgi,os
from cachecontrol import cache
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class Admin(webapp.RequestHandler):
						
	def get(self):
		admin= AdminData()		
		path = os.path.join(os.path.dirname(__file__), 'templates/admin.html')
		#populate the admin settings variable
		if not admin.get():
			admin.initialize()
		adminSettings ={}
		adminSettings["status"]=admin.get()
		self.response.out.write(template.render(path, adminSettings))
	
	def post(self):
		admin = AdminData()
		startapp = self.request.get('startapp')
		if startapp!= None:
			admin.changeStatus("dataload")
			self.response.out.write("<div style='background-color:yellow'> Application Started</div>")
		path = os.path.join(os.path.dirname(__file__), 'templates/admin.html')
		adminSettings ={}
		adminSettings["status"]=admin.get()
		self.response.out.write(template.render(path, adminSettings))
	
	
	"""
	test driver for the AdminData class. change this to get to test it out
	"""
	def testDriver(self):
		admin=AdminData()		
		if not admin.get():
			admin.initialize()
		self.response.out.write("admin.get() =" + admin.get()+"<br>")
		self.response.out.write("admin.getCurrentStatus() = " + admin.getStatus()+"<br>")
		admin.changeStatus("dataload")
		#self.response.out.write("admin.changestatus" + str(admin.changeStatus("dataload")) +"<br>")		
		self.response.out.write("admin.get() = " + admin.get()+"<br>")	
		
	


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
		self.currentStatus = newStatus
		cc = cache()
		cc.replace("admin_data",self)	
	
	"""
	Returns the current status of the Admin Data settings
	"""	
	def get(self):
		if not self.getStatus():
			return None
		else:
			return self.getStatus()
		
		
			

application = webapp.WSGIApplication(
                                     [('/admin', Admin)],                                     
                                     debug=True)
def main():
  run_wsgi_app(application)  
  
if __name__ == "__main__":
  main()
