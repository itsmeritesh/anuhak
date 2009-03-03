/* 
  file: client.js
  author: ritesh
  purpose: contains calls for synchronization of the workflow and handshakes   */

var timerObject;

function getStatus()
 {
  $.post("status", handleStatusResponse,"text");
 }
 
 
function handleStatusResponse(data)
 {
	if(data.match(/uninitialized/))
		{
		 timerObject = setInterval("getStatus()",2000);
		 //alert('sending');
		}
	else
	   {
	    alert( "still to be implemented");
	   }
 }


function onload_function()
 {
	$.post("status", {name:"ashwin"}, handleStatusResponse,"text");

 }


onload_function();

