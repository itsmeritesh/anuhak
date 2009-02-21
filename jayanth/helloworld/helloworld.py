import Cookie
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
  id = 0
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.headers.add_header(
        'Set-Cookie', 
        'id='+str(self.id)+'; expires=Fri, 31-Dec-2020 23:59:59 GMT')
    username = self.request.cookies.get('id', '')
    self.response.out.write('Hello, webapp World!')
    self.response.out.write(username)
  id = id + 1

application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main() 
