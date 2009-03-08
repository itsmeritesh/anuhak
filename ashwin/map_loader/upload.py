import os

from definemap import Map
def upload():
    
    file=open("toupload.csv","r")
    for line in file:
        list = line.split(",")
        map = Map(uniqueid=int(list[0]),
        dataset_name=list[1],
	text=list[2],
        filename="logs.txt")
        map.put()
        list=[]
        
        
