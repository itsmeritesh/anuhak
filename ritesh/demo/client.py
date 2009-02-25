import cgi
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class Client(webapp.RequestHandler):
	def get(self):
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




application = webapp.WSGIApplication(
                                     [('/client', Client)],                                     
                                     debug=True)
def main():
  run_wsgi_app(application)  
  
if __name__ == "__main__":
  main()
	
	
