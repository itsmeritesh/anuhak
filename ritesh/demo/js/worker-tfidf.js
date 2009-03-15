var wp = google.gears.workerPool;
//set this variable to send reuslt back to master code
var result;
var success=false;
var db;
var debug = true;


function init_db() {
	if (google.gears) {
		try {
			db = google.gears.factory.create('beta.database');

			if (db) {
				  db.open('kahuna');
				  success = true;
			}

		} catch (ex) {
			result+="Could not create database:" + ex.message;
		}
	}

}


function tfidf() {
	var words=new Array();
	var input=new Array();
	var i;
	var j;
	var k;
	var l;
	var count=0;
	var tf;
	var doccount=0;
	var tfidf;
	var idf;
	var str;
	var totaldocsrs = db.execute('select count(*) from Input');        
	var totaldocs = parseInt(totaldocsrs.field(0));

	var rs=db.execute('select * from Input');
	
	while(rs.isValidRow()) {
	      words=rs.field(1).split(" ");
	      for(i=0;i<words.length;i++) {
		      count=0;
		      doccount=0;
		      for(j=1;j<words.length;j++) {
				if(words[i]==words[j])
					count=count+1;
		      }
		      tf=count/words.length;
		    //  for(l=0;l<input.length;l++) {
			
			//	if(input[l].indexOf(words[i])!=-1) {
			
			//		doccount=doccount+1; }
		    //  }
		      var countrs=db.execute("select count(*) from (select * from Input where input like '%"+words[i]+"%') t");
		      doccount=parseInt(countrs.field(0));		      
		      idf=totaldocs/doccount;
		    
		      
		      tfidf=tf*idf;
		      //document.write("Tfidf of "+words[i]+" is "+tfidf);
		      result+="Tfidf of "+words[i]+" is "+tfidf+"<br>";
		      //document.write("<br>");
		      db.execute('Insert into Termfreq values(?,?,?)',[words[i],rs.field(0),tfidf]);
	      }
	      rs.next();
	}
 	return;
}


//write map code here
function kahuna_mapFunction()
 {
   init_db();
   tfidf();
 } 
kahuna_mapFunction();

wp.onmessage = function(a, b, message) {
   var result = "send result here";
   //var reply = message.body[0] + message.body[1] + "... " + message.body[2].helloWorld;
   wp.sendMessage(result, message.sender);
 } 
