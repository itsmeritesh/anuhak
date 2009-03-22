from google.appengine.ext import db

class Map(db.Model):
  uniqueid = db.IntegerProperty(required=True)
  dataset_name = db.StringProperty(required=True)
  dated = db.DateTimeProperty(auto_now_add=True)
  text = db.TextProperty()
  filename = db.StringProperty(required=True)
  
class Maplet:  
  uniqueid = None
  dataset_name = None
  dated = None
  text = None
  filename = None
  
  
	
