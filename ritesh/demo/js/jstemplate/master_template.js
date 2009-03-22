/*
  Use this template to write code any new problem that needs to be solved using the kahuna framework. This will contain code for both the gears and non gears version of the framework

*/

/****************************************
    Section to declare all global variables
*******************************************/

 var WORKER_FILENAME = "tfidf_worker.js";
 var workerPool = google.gears.factory.create('beta.workerpool');

/****************************************
  End Section variables
****************************************/


//This function is called when the worker finishes execution and returns the results
workerPool.onmessage = function(a, b, message) {
  alert('Received message from worker ' + message.sender + ': \n' + message.body);
  return;
};


//this function is called when onload of the body. Write any kind of initialization code here
function kahuna_init()
{
 
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
  
}

//this function is called when the application returns gearsMapReduce
function kahuna_onGearsMapreduce()
{

}

//this function is called when the application returns the status Map. write map logic here
function kahuna_onMap()
{
	createWorker();
	dispose();
}




//this function is called when the application returns the status reduce
function kahuna_onReduce()
{
}

