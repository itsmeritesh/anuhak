import cgi
from cachecontrol import cache
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class cachetest(webapp.RequestHandler):
	def get(self):
		self.response.out.write("<h4>Test page for memcache</h4>")
		cc = cache()
		value1 = 100
		key1= "number"
		cc.put(key1,value1)
		returnValue = cc.get(key1)
		if returnValue == None:
			self.response.out.write("return value is null")
		else:
			self.response.out.write(returnValue)
	
		
		value2= []
		value2.append("january")
		value2.append("february")
		value2.append("march")
		key2="array"
		cc.put(key2,value2)
		returnValue=cc.get(key2)
		if returnValue == None:
			self.response.out.write("return value is null")
		else:
			self.response.out.write(returnValue)
		
application = webapp.WSGIApplication(
                                     [('/cachetest', cachetest)],                                     
                                     debug=True)


def main():
  run_wsgi_app(application)
  
  
if __name__ == "__main__":
  main()
	
	
		
	
