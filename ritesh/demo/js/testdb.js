function onload_function()
{
/*	timerObject = setInterval("getStatus()",5000);
	$.post("status", handleStatusResponse,"text");*/
	var success = false;

	if (google.gears) {
		try {
			db = google.gears.factory.create('beta.database');

			if (db) {
				  db.open('database-demo');
				  var rs=db.execute('select * from Map');
				  while(rs.isValidRow()) {
					  alert("" + rs.field(1));
					  rs.next();
				  }

				  success = true;
			}
		}
		catch (ex) {
			//setError('Could not create database: ' + ex.message);
			alert('Could not create database: ' + ex.message);
		}
	}
}	

onload_function(); 
