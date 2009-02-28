/* 
  file: client.js
  author: ritesh
  purpose: contains calls for synchronization of the workflow and handshakes   */



function getStatus()
 {
  $.post("status", handleStatusResponse,"text");
 }
 
 
function handleStatusResponse(data)
 {
	if(data.find("uninitialized")!= -1)
		{
		 setTimeout("getStatus()",2000);
		 alert('sending');
		}
	else
	   {
	    alert( "still to be implemented");
	   }
 }


function onload_function()
 {
	$.post("status", handleStatusResponse,"text");

 }


onload_function();

