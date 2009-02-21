
import sys

class Settings(object):
  def __init__(self):
    self.counter = 0
    
    def static_var(varname, value):
	    def decorate(func):
        	setattr(func, varname, value)
        	return func
    	    return decorate

  
  def getCounter(self):
  	self.counter = self.counter +1
  	return self.counter
  
  def __call__(self):
    self.counter += 1
    print self.counter
