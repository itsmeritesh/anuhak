import os
import glob
from google.appengine.ext import db
from definemap import Map
"""This is not a part of the main kahuna app as the appengine filesystem is read only
   use this to dump your maps to a csv and call the bulkloader app
 """

class uploader:
	
	pathname = ""
	
	def __init__(self,path):
		#filename = 'toupload.csv'
		#variable path is the path to the folder where the maps are located
		#global file
		#file = open(path+"/"+filename,"w")
		global pathname
		pathname = path
		
	def makecsv(self):
		"""iterates through each file in the folder and puts it into toupload.csv
		   in the same folder along with an dentifier and filename
		"""
		#since we use json, we replace all commas(',') in the file with @#
		
		"""The bulkuploader cannot do this as it can work only with csv's
		   The dirty way to do this is to get the map from th datastore and
		   replace all @#'s with commas
		"""
		filelist=os.listdir(pathname)
		count=0
		for filename in filelist:
			count = count+1
			cur_file = open(pathname+"/"+filename)
			content=cur_file.read()
			#oneline = str(count)+","+"logs"+","+content.strip().replace(",","@#")+","+filename
			map = Map(uniqueid=count,
			dataset_name="logs",
			text=content.strip().replace(",","@#"),
			filename=filename)
			map.put()
			#file.write(oneline+"\n")
		#file.close()
		
		
