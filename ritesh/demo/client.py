import cgi
import os
from google.appengine.ext import webapp
from cachecontrol import cache
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
import logging

class Client(webapp.RequestHandler):

	
	

	def get(self):
		self.checkCookie(self.request,self.response)
		self.response.out.write("""
			<html>
				<head>
				 <title>Client page - Big Kahuna</title>
				 <script src="js/gears_init.js"></script>
				 <script language="javascript" src="js/jquery.js"></script>	 
 				 <script language="javascript" src="js/master-log.js"></script>
				 <script language="javascript" src="js/client.js"></script>
				 <head>
				<body>
					Client page
					<div id="logwindow">Debug Window:</div>
					<a name="bottom" id="bottom"></a>
				</body>
			</html>""")
			
	def checkCookie(self,request,response):

		clientlist = []
		cc = cache()
		templist = cc.get("clientlist")
		if templist == None:
		    cc.put("clientlist",clientlist)
		    logging.info("created client list")

		clientCookie = request.cookies.get('BigKahuna', '')


		""" create a unique key value pair to track max value of cookie set """
		cookieKey = "cookieKey"
		cookieValue = cc.get(cookieKey)
		""" If that key value pair doesnt exist, create one and set it to zero """
		if cookieValue == None:
		    cc.put(cookieKey,0)
		    cookieValue = 0
		    logging.info("created cookie counter")
		""" If client cookie isnt set, increment max value by one and set it as the cookie in the response object """  
		if clientCookie == "":

		    resource = Resource()
		    resource.ip = request.remote_addr
		    resource.clienttype = os.environ['HTTP_USER_AGENT']
		    resource.cookie = cc.incr(cookieKey)
		    logging.info("created resource object")
		    clientlist = cc.get("clientlist")
		    clientlist.append(resource)
		    cc.replace("clientlist",clientlist)
		    logging.info("replaced client list")  
		    response.headers.add_header('Set-Cookie', 'BigKahuna='+str(resource.cookie)+'; expires=Fri, 31-Dec-2020 23:59:59 GMT')	
		    response.out.write('Hello, webapp World!')
		    response.out.write("Cookie:" + str(resource.cookie))
		    response.out.write("IP:" + resource.ip)
		    response.out.write("IP:" + resource.clienttype)

		else:
		    response.out.write("You have already visited us once")
		    tlist = cc.get("clientlist")
		    response.out.write("Cookie:" + clientCookie)
		    response.out.write("IP:" + request.remote_addr)
		    response.out.write("IP:" + os.environ['HTTP_USER_AGENT'])
		    resource = Resource()
		    resource.ip = request.remote_addr
		    resource.clienttype = os.environ['HTTP_USER_AGENT']
		    resource.cookie = clientCookie
		    tlist.append(resource)
		    cc.replace("clientlist",tlist)
		    for obj in tlist:
			  if obj == "":
				if obj.cookie == int(clientCookie):
				      logging,info("Details already in cache")
				else:
				      logging.info("Inside for in client")
				      obj = resource
				      tlist.remove(obj)
				      tlist.append(obj)
				      cc.replace("clientlist",tlist)
				      logging.info("replaced client list")
		    
		
		

class Resource:
	cookie = None
	ip = None
	clienttype = None
	gearsenabled = None




application = webapp.WSGIApplication(
                                     [('/client', Client)],                                     
                                     debug=True)
def main():
  run_wsgi_app(application)  
  
if __name__ == "__main__":
  main()
	
	
