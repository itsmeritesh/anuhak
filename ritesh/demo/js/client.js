/* 
  file: client.js
  author: ritesh
  purpose: contains calls for synchronization of the workflow and handshakes   */


function handleStatusResponse(data)
 {
	alert(data);
 }


function onload_function()
 {
	$.post("status", handleStatusResponse,"text");

 }


onload_function();

