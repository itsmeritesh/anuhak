import cgi
from google.appengine.ext import webapp
from cachecontrol import cache
from google.appengine.ext.webapp.util import run_wsgi_app

class Mapviewer(webapp.RequestHandler):
	def get(self):
		
		self.response.out.write("""
			<html>
				<head>
				 <title>Viewer - Big Kahuna</title>
				 </head>
				<body>""")
		

                mycache = cache()
                maplist = mycache.get("store")
                self.response.out.write("Map store has: "+ str(len(maplist)) +"maps")
                resultlist = mycache.get("resultlist")
                self.response.out.write("Result store has: "+ str(len(resultlist)) +"results")
                self.response.out.write("<hr>")
                for i in range(0,len(maplist)-1):
                    map = maplist[i]
                    self.response.out.write("map id = "+str(map.uniqueid)+data +"\n" +map.text)
                    for j in range(0,len(resultlist)-1):
                        result=resultlist(i)
                        if (str(map.uniqueid) == int(result.token)):
                            self.response.out.write("result is "+ "\n" +result.data)
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
