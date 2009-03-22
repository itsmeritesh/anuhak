from classdefs import *
import logging
from google.appengine.ext import db
import uuid

#call this class to dump results to the datastore

def loadresult(dataset,ip,id,result):
    res  = Results(resultid = uuiu.uuid4(),
              dataset_name = dataset,
              client_ip = ip,
              client_id = id     
              data=result)
    res.put()


# delete rows based on dataset name, if none is passed then delete all rows in datastore

def clearstore(dataset):
    if dataset == None:
        filter = ""
    else:
        filter = "where dataset_name ='"+dataset+"'"
        
    query = "select * from Results" + filter
    queryresult = db.GqlQuery(query)
    for oneresult in queryresult:
        oneresult.delete()

