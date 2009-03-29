/* 
  file: client.js
  author: ritesh
  purpose: contains calls for synchronization of the workflow and handshakes   */

var timerObject;
var db;
var mapdone=false;
var gearsenabled=false;


function getStatus()
 {
  $.post("status", {gearsenabled:gearsenabled},handleStatusResponse,"text");
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
	else if(data.match(/gearsmapreduce/)) {
		if(mapdone) { 
			  //document.write("Map done once");
		}
		else {
		      kahuna_onGearsMapReduce();
		      mapdone=true;
		      timerObject=setInterval("getStatus()",500);
		      getStatus();
		}
	}
	else if(data.match(/map/)) {
		//clear the timer to stop the pinging behavior and wait for the dataload to finish
		clearInterval(timerObject);
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
	$.post("setgears", {gearsenabled:gearsenabled}, function(data) { 
	      
	},"text");
 	$.post("status", {gearsenabled:gearsenabled}, handleStatusResponse,"text");
	var success = false;
    
 }

//start the execution of this logic engine 
onload_function();
