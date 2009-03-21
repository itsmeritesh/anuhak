/* 
  file: client.js
  author: ritesh
  purpose: contains calls for synchronization of the workflow and handshakes   */

var timerObject;
var db;



function getStatus()
 {
  $.post("status", handleStatusResponse,"text");
 }
 
 
function handleStatusResponse(data)
 {
	if(data.match(/inactive/))
	{		
		 kahuna_onInactive();
	}
	else if(data.match(/dataload/))
	{
		//clear the timer to stop the pinging behavior and wait for the dataload to finish
		 if(timerObject!=null)
			clearInterval(timerObject);
		//call the dataload code
		kahuna_onDataLoad();
		//ping to see if status has changed. Sequentialize the pinging mechanism
		getStatus();
		
	}
	else if(data.match(/map/)) {
		kahuna_onMap();
	}	
	else if(data.match(/reduce/)) {
		kahuna_onReduce();
	}
}




function onload_function()
 {
	//call the init function and then start pinging.
	kahuna_init();	
	timerObject = setInterval("getStatus()",500);
	$.post("status", handleStatusResponse,"text");
	var success = false;
    
 }

//start the execution of this logic engine 
onload_function();
