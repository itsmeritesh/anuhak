
import datetime
from google.appengine.ext import db
from definemap import *

class MapDataLoader(Loader):
  def __init__(self):
    Loader.__init__(self, 'Map',
                    [('uniqeuid', int),
                     ('dataset_name', str),
                     ('date', lambda x: datetime.datetime.strptime(x, '%m/%d/%Y').date()),
                     ('text', str),
                     ('filename', str)
                     ])
