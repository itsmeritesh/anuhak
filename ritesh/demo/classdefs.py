from google.appengine.ext import db

class Results(db.Model):
    resultid = db.StringProperty(required = True)
    dataset_name = db.StringProperty(required = True)
    token = db.IntegerProperty(required = True)
    data = db.TextProperty()

class resultlet:
    token = None
    data = None
    

        
