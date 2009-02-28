import cgi
import os,glob
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

class Jstest(webapp.RequestHandler):
	def get(self):
		path = os.path.join(os.path.dirname(__file__), 'templates/jstest.html')
		template_values={ }
		self.response.out.write(template.render(path, template_values))
		

application = webapp.WSGIApplication(
                                     [('/jstest', Jstest)],                                     
                                     debug=True)


def main():
  run_wsgi_app(application)
  
  
if __name__ == "__main__":
  main()
	
