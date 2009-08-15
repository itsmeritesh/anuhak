import cgi
from admin import AdminData
from reducemanager import reducemanager
from cachecontrol import cache
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class GetReduce(webapp.RequestHandler):
	def get(self):
		rm = reducemanager();
		reducelist = rm.getreduceitems(10);
		if not reducelist:
			admin = AdminData()
			admin.changeStatus('Complete')
			return ""
		tosend=""
		for i in range(0,len(reducelist)-2):
			result = reducelist[i]
			tosend= tosend + '"'+ result.data +'",'
		tosend= tosend +'"'+str(reducelist[len(reducelist)-1].data)+'"'
		self.response.out.write(tosend)
		
	def post(self):
		rm = reducemanager();
		reducelist = rm.getreduceitems(30);
		if not reducelist:
			admin = AdminData()
			admin.changeStatus('Complete')
			return ""
		tosend=""
		for i in range(0,len(reducelist)-2):
			result = reducelist[i]
			tosend= tosend + '"'+ result.data +'",'
		tosend=tosend + '"'+reducelist[len(reducelist)-1].data+'"'
		self.response.out.write(tosend)


application = webapp.WSGIApplication(
                                     [('/getreduce', GetReduce)],                                     
                                     debug=True)


def main():
  run_wsgi_app(application)
  
  
if __name__ == "__main__":
  main()
        
