import cgi,os
from google.appengine.ext import webapp
from showstatus import status
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from admin import AdminData

class Mapviewer(webapp.RequestHandler):
	def get(self):
		values={}	
		curstatus = status()
		admindata  = AdminData()
		values['status']=admindata.get()
		values['datastoremapcount'] = curstatus.datstoremapcount()
		values['currentmapcount'] = curstatus.currentmapcount()
		values['resultcount'] = curstatus.resultcount()
		#values['status'] = curstatus.whatsgoinon()
		values['lastresult'] = curstatus.resultobject()
		path = os.path.join(os.path.dirname(__file__), 'templates/mapview.html')
                self.response.out.write(template.render(path, values))
                

application = webapp.WSGIApplication(
                                     [('/mapview', Mapviewer)],                                     
                                     debug=True)
def main():
  run_wsgi_app(application)  
  
if __name__ == "__main__":
  main()
