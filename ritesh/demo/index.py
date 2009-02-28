import cgi
import os,glob
from utils import Settings
from Schema import Schema
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.ext import db

class MainPage(webapp.RequestHandler):
  def get(self):
  	#self.reponse.write('Testing rendering')
  	settings = Settings()
  	mylist=[]
  	mylist.append(1)
  	mylist.append(2)
  	mylist.append(3)
  	count=10
	path = os.path.join(os.path.dirname(__file__),'inputFiles/')
	files=[]
	for infile in glob.glob( os.path.join(path, '*') ):
		files.append(infile)
		
	template_values = {
	      'mylist': mylist,
	      'count': count,
	      'staticvalue':1,
	      'pathinfo': path,
	      'files':files
	      }	      
	path = os.path.join(os.path.dirname(__file__), 'index.html')
	self.response.out.write(template.render(path, template_values))
	

   

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                     ('/schema',Schema)],                                     
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
  



