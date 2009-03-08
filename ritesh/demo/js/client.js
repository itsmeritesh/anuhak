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
		
		 //alert('sending');
	}
	else if(data.match(/dataload/))
	{
		$.post("getdata",function(data) { 
			toput = data.replace(/@#/g,",");
			db.execute('Insert into Map values(?,?)',[null,toput]);
		},"text");
		
		
	}	
}


function onload_function()
 {
	timerObject = setInterval("getStatus()",5000);
	$.post("status", handleStatusResponse,"text");
	var success = false;

	if (google.gears) {
		try {
			db = google.gears.factory.create('beta.database');

			if (db) {
				  db.open('database-demo');
				  db.execute('create table if not exists Map' + '(id integer primary key, map longtext)');

				  success = true;
			}

		} catch (ex) {
			//setError('Could not create database: ' + ex.message);
			alert('Could not create database: ' + ex.message);
		}
	}	
}


onload_function();