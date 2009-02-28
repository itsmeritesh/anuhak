from google.appengine.ext import db
from google.appengine.ext import webapp

class Schema(webapp.RequestHandler):
	def addSchema(self):
	 	setting = Settings(name="ritesh",number= 3)
	 	return setting
	 
	def get(self):
	 	setting = self.addSchema()
	 	setting.put()	 
	        for s in Settings.all():
	  		self.response.out.write('Name='+str(s.name) +'   Number='+str(s.number))
	 
	 
	 


class Settings(db.Model):
	name = db.StringProperty(required=True)
	number = db.IntegerProperty()
	

