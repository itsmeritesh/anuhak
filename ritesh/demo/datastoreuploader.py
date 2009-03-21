import cgi
from dumptocsv import uploader
from cachecontrol import cache
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


class DataStoreUploader(webapp.RequestHandler):
    def get(self):
        #uploaderObject = uploader("logs")
        uploaderObject = uploader("blogs")
        uploaderObject.makecsv()
        self.response.out.write("Finished uploading Logs into the datastore")




application = webapp.WSGIApplication(
                                     [('/datastoreuploader', DataStoreUploader)],                                     
                                     debug=True)


def main():
  run_wsgi_app(application)
  
  
if __name__ == "__main__":
  main()
        