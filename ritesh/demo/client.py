import cgi
from google.appengine.ext import webapp
from cachecontrol import cache
from google.appengine.ext.webapp.util import run_wsgi_app

class Client(webapp.RequestHandler):
	def get(self):
		self.checkCookie(self.request,self.response)
		self.response.out.write("""
			<html>
				<head>
				 <title>Client page - Big Kahuna</title>
				 <script language="javascript" src="js/jquery.js"></script>
				 <script language="javascript" src="js/client.js"></script>
				<head>
				<body>
					A dummy client page for now
				</body>
			</html>""")
			
	def checkCookie(self,request,response):
		    """ Get the IP address and cookie of app from the http request object """
		    ipAddress = request.remote_addr
		    clientCookie = request.cookies.get('BigKahuna', '')
		    cc = cache()
		    """ create a unique key value pair to track max value of cookie set """
		    cookieKey = "cookieKey"
		    cookieValue = cc.get(cookieKey)
		    """ If that key value pair doesnt exist, create one and set it to zero """
		    if cookieValue == None:
		    	cc.put(cookieKey,0)
		    	cookieValue = 0
		    """ If client cookie isnt set, increment max value by one and set it as the cookie in the response object """  
		    if clientCookie == "":
		    	cookieValue = cc.incr(cookieKey)
		    	cc.put(ipAddress,cookieValue)
		    	response.headers.add_header('Set-Cookie', 'BigKahuna='+str(cookieValue)+'; expires=Fri, 31-Dec-2020 23:59:59 GMT')	
		    	""" Client cookie is also set. Place to send map/reduce/app status. Currently doing nothing """
		    else:
		    	response.out.write("Nothing Doing")

		    response.out.write('Hello, webapp World!')
		    response.out.write("Cookie:" + clientCookie)
		    response.out.write("IP:" + ipAddress)
		
		




application = webapp.WSGIApplication(
                                     [('/client', Client)],                                     
                                     debug=True)
def main():
  run_wsgi_app(application)  
  
if __name__ == "__main__":
  main()
	
	
