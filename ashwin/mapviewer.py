import cgi
from google.appengine.ext import webapp
from showstatus import status
from google.appengine.ext.webapp.util import run_wsgi_app

class Mapviewer(webapp.RequestHandler):
	def get(self):
		
		self.response.out.write("""
			<html>
				<head>
				 <title>Viewer - Big Kahuna</title>
                                 <meta http-equiv="refresh" content="600">
				 </head>
				<body>""")
		curstatus = status()
		#write code here

                
                self.response.out.write("""					
				</body>
			</html>""") 
                

application = webapp.WSGIApplication(
                                     [('/mapview', Mapviewer)],                                     
                                     debug=True)
def main():
  run_wsgi_app(application)  
  
if __name__ == "__main__":
  main()
