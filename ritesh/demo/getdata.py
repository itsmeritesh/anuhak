import cgi
from maploader import Maploader
from admin import Admin
from cachecontrol import cache
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class GetData(webapp.RequestHandler):
    """
     this is mostly a post call but get is used to test whether its working
    """
    
    def get(self):
        maploader = Maploader("logs")
        map = maploader.getmap()        
        if not map:
            admin = Admin()
            admin.changeStatus("map")
        else:
            self.response.out.write(map.text)

    def post(self):
        maploader = Maploader("logs")
        map = maploader.getmap() 
        if not map:
            admin = Admin()
            admin.changeStatus("map")
        else:
            self.response.out.write(map.text)    


application = webapp.WSGIApplication(
                                     [('/getdata', GetData)],                                     
                                     debug=True)


def main():
  run_wsgi_app(application)
  
  
if __name__ == "__main__":
  main()
        