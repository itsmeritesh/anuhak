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
    
    self.response.out.write("""
      <html> 
      <head>
      <script language="javascript" src="js/jquery.js"></script>
      <script src="js/gears_init.js"></script>
      <script language="javascript" src="js/testdb.js"></script>
      </head>
      <body>
      </body>
      </html>
    """)


application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                     ('/testgearsdb',MainPage)],                                     
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()