var wp = google.gears.workerPool;
//set this variable to send reuslt back to master code
var result;
var success=false;
var db;
var debug = true;


function Hash()
{
	this.length = 0;
	this.items = new Array();
	for (var i = 0; i < arguments.length; i += 2) {
		if (typeof(arguments[i + 1]) != 'undefined') {
			this.items[arguments[i]] = arguments[i + 1];
			this.length++;
		}
	}
   
	this.removeItem = function(in_key)
	{
		var tmp_value;
		if (typeof(this.items[in_key]) != 'undefined') {
			this.length--;
			var tmp_value = this.items[in_key];
			delete this.items[in_key];
		}
	   
		return tmp_value;
	}

	this.getItem = function(in_key) {
		return this.items[in_key];
	}

	this.setItem = function(in_key, in_value)
	{
		if (typeof(in_value) != 'undefined') {
			if (typeof(this.items[in_key]) == 'undefined') {
				this.length++;
			}

			this.items[in_key] = in_value;
		}
	   
		return in_value;
	}

	this.hasItem = function(in_key)
	{
		return typeof(this.items[in_key]) != 'undefined';
	}
}




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

//delegate to run the sort for our objects
function sortNumber(obj1,obj2)
{
    return  -(obj1.tfidf - obj2.tfidf);
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

	//populate the tdht for term doc reference
	var tdht = new Hash();
	var currentDocument =0;

	var rs=db.execute('select * from Input');	
	while(rs.isValidRow()) {
	   currentDocument ++;
	   words=rs.field(1).split(" ");
	     for(i=0;i<words.length;i++) {
		     var word = words[i];
			if(tdht.hasItem(word))
			{
			  if (tdht.getItem(word).currentDocument != currentDocument)			
			    {
				tdht.getItem(word).currentDocument = currentDocument;
				tdht.getItem(word).docCount++;
			     }
			}
			else
			{
				var object = {'currentDocument': currentDocument, 'docCount' :1};
				tdht.setItem(word,object);
			}
		}
	   rs.next();
	 }

	//populate term frequency
	var rs=db.execute('select * from Input');	
	while(rs.isValidRow()) {
	      words=rs.field(1).split(" ");
		var tfht = new Hash();
		//get term count into tfht	
	       for(i=0;i<words.length;i++) {
			if(tfht.hasItem(words[i])) {
				var wc =tfht.getItem(words[i])+1;
				tfht.removeItem(words[i]);
				tfht.setItem(words[i],wc);
			   }
			else	
				tfht.setItem(words[i],1);	    
		      }
	        //noramlize tf by dividing it by the number of terms in the document
		 var toSort = new Array();
		 for (var j in tfht.items) {
			  var tf = tfht.getItem(j) / words.length ;			  
			  tfidf = tf * (totaldocs / tdht.getItem(j).docCount );
			  tfht.removeItem(j);
			  tfht.setItem(j,tfidf);			  
			  var obj = { 'word': j, 'tfidf': tfidf }
			  toSort.push(obj);
			}	
		
	   	  toSort.sort(sortNumber);
		  var topcount =0;
		  for(var count=0;count<toSort.length  ;count ++)
		   {			
			if(topcount <15) {
		 	db.execute('Insert into Termfreq values(?,?,?)',[toSort[count].word,rs.field(0),toSort[count].tfidf]);			
			topcount ++;
			}
			else break;
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

var errorMessage = "done"
wp.onerror = function (object) {
  errorMessage = object.message;
 }
wp.onmessage = function(a, b, message) {
   var result = "send result here";
   //var reply = message.body[0] + message.body[1] + "... " + message.body[2].helloWorld;
   wp.sendMessage(errorMessage, message.sender);
 } 
