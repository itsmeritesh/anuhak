import cgi,os
from cachecontrol import cache
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class MainPage(webapp.RequestHandler):
  def get(self):
  	template_values={
  		'staticvalue':1
  	}
	path = os.path.join(os.path.dirname(__file__), 'templates/dbquery.html')
	self.response.out.write(template.render(path,template_values))
	

   

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                     ('/dbquery',MainPage)],                                     
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()

