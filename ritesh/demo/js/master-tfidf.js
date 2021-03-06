/*
  Use this template to write code any new problem that needs to be solved using the kahuna framework. This will contain code for both the gears and non gears version of the framework

*/

/****************************************
    Section to declare all global variables
*******************************************/

 var WORKER_FILENAME = "worker-tfidf.js";
 var workerPool = google.gears.factory.create('beta.workerpool');

/****************************************
  End Section variables
****************************************/


//This function is called when the worker finishes execution and returns the results
workerPool.onmessage = function(a, b, message) {
  $.post("resultmanager", {result:message.body, resulttype:"map"},
    function(data){
      alert("Map done");
    }
  ,"text");
  return;
};


//this function is called when onload of the body. Write any kind of initialization code here
function kahuna_init()
{
	if (google.gears) {
		try {
			db = google.gears.factory.create('beta.database');

			if (db) {
				  db.open('kahuna');
				   db.execute('drop table if exists Input');
				   db.execute('drop table if exists Termfreq');
				  db.execute('create table if not exists Termfreq' + '(keyword text, docid integer,tfidf integer)');
				 // db.execute('create table if not exists Input' + '(id integer primary key,input longtext)');
  	     			db.execute('create table if not exists Input' + '(id integer,input longtext)');
				  success = true;
			}

		} catch (ex) {
			//setError('Could not create database: ' + ex.message);
			alert('Could not create database: ' + ex.message);
			//result+="Could not create database:" + ex.message;
		}
	} 
}



//this function is called to dispose or output things on to the screen after the computation phase is complete
function dispose()
 {
 //alert('done');
 return "done";
 }


//this function is called to create the new worker thread. Based on your usage you can spawn multiple workers as well.
function createWorker()
 {
     var childWorkerId = workerPool.createWorkerFromUrl('js/'+WORKER_FILENAME);
     workerPool.sendMessage(["3..2..", 1, {helloWorld: "Hello world!"}], childWorkerId);
 }




//This function is called when the application returns the value unitialized
function kahuna_onInactive()
{
}


//this function is called when the application returns dataload. Write dataload logic here
function kahuna_onDataLoad()
{             
		$.post("getdata",function(data) { 
			var obj = eval('(' + data + ')');
			db.execute('Insert into Input values(?,?)',[obj.id,obj.data]);
		},"text");
}


//this function is called when the application returns the status Map. write map logic here
function kahuna_onMap()
{
	
}


function kahuna_onGearsMapReduce()
{
	createWorker();
	dispose();
}


//this function is called when the application returns the status reduce
function kahuna_onReduce()
{
}
createWorker();
	dispose();
