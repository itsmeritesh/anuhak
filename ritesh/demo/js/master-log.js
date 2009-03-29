/*
  Use this template to write code any new problem that needs to be solved using the kahuna framework. This will contain code for both the gears and non gears version of the framework

*/

/****************************************
    Section to declare all global variables
*******************************************/
var id;
var reqXML;
var cookieValue;
var response;
var jsarray=new Array();
var callParameter = 1;
var dblMinutes = 500;
var result=new Array();
var resultString="List=";
var parsedInput = new Array();
var board=new Array();
var searchPattern="4**3**2511";
var iterator=0;
var finalcount=0;
var sumReduce;
var log1=new Array();
var startPosition;
var logFlag=false;
/****************************************
  End Section variables
****************************************/


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


//This function is called when the application returns the value unitialized
function kahuna_onInactive()
{
}


//this function is called when the application returns dataload. Write dataload logic here
function dataLoad()
{             
		$.post("getdata",function(data) { 
			var obj = eval('(' + data + ')');
			id = obj.id;
			var str = obj.data.replace(/@/g,"\"");
			log("received data =" +str);
			log1=eval('[' + str + ']');
		},"json");
}


//this function is called when the application returns the status Map. write map logic here
function kahuna_onMap()
{
	dataLoad();
	log_cruncher();
}

function kahuna_onGearsMapReduce() {

}

function sendResults() {
	$.post("resultmanager",{result:finalcount,id:id,resultType:"map"},function(data) { 
	      log("results sent" + data);	      
	},"text");
	getStatus();
}



//this function is called when the application returns the status reduce
function kahuna_onReduce()
{
              $.post("getreduce",function(data) { 
			log("reduce received data =" + data);
			var obj = eval('[' + data + ']');
			//id = obj.id;
			//var str = obj.data.replace(/@/g,"\"");
			
			jsarray=obj
			reduce_counts();
		},"json");
}






//log crunching here

	  function reset()
	 {
		for(var i=0;i<result.length;i++) {
		result[i]="";
		}
		resultString="List=";
		result="";
	}
	
	function log_cruncher()
	 {	
		reset();

		for(iterator=0;iterator<64;iterator++){
		     board[iterator]="*";
		}
		loadboard();	
		sendResults();
	}	

	function genericLoadBoard()
	 
	{
	while(startPosition<=log1.length){
	var values=new Array();
	var prev=new Array();
	 var next=startPosition;
	startPosition+=1;
	if("ICHECK"==log1[next].match("ICHECK") || "ICASTLE"==log1[next].match("ICASTLE")){
	continue;
	}

	 var index=log1[next].lastIndexOf("#");
	 var str=log1[next].substring(log1[next].lastIndexOf("#")+1,log1[next].length);
	var old=log1[next].substring(log1[next].indexOf("#")+1,log1[next].lastIndexOf("#"));
		var pawn=log1[next].substring(0,log1[next].indexOf("#"));
		values=str.split(",");
		if("NULL"!=log1[next].match("NULL")){
		prev=old.split(",");
		var k=parseInt(prev[0])*8+parseInt(prev[1]);
		board[k]="*";
		}
		var j=parseInt(values[0])*8+parseInt(values[1]);
		
		board[j]=pawn+"";
		startPosition+=1;
	getPatterns();

	}
	findPattern();
	}
	
	
	
	function findPattern(){
		finalcount =0;
		log("finalcount before starting ="+ finalcount)
		splitarr=result.split("|");
		var i;
		for(i=0;i<splitarr.length;i++){
			//console.log(splitarr[i]);
			if(splitarr[i]==searchPattern){
				finalcount+=1;
			}
		}	
	     if(finalcount>1) 
		log("Final COunt =" + finalcount);
	     log("Find pattern returned :" + finalcount);
	    
	 }


	function loadboard(){
	var i;var index;
	var str,pawn;
	var j;
	var values=new Array();
	for(i=1;i<log1.length;i++){
		if("START"==log1[i].match("START")){
		 startPosition = i+1;	
		break;
		}
		else{
		
		index=log1[i].lastIndexOf("#");
		str=log1[i].substring(log1[i].lastIndexOf("#")+1,log1[i].length);
		pawn=log1[i].substring(0,log1[i].indexOf("#"));
		values=str.split(",");
		j=parseInt(values[0])*8+parseInt(values[1]);
		board[j]=pawn+"";
		}
	}


	//log("Pattern result =" +result);
	getPatterns();
	genericLoadBoard();

	}	


function getPatterns(){

	var row;
	var col;
	var n=3,i,j;
	var seed;var pattern="";
		for(row=0;row<= 56-[8*(n-1)];row+=8){
			for(col=row;col<=row+8-n;col+=1)
						{
					seed = col;
				//remove this to make it a continious string,else pattern will b overwritten
					pattern="";
					for(j=0;j<n;j+=1){
						
						 for(i=0;i<n;i++){
							pattern=pattern+""+board[seed+i];
						}
	seed +=8;
	}
	
	result=result+"|"+pattern;
	 
	}
	}

	}
	
	/* the reduce function in our case */
	 function reduce_counts()
	 {
	 	var sum=0;
	 	for(var i=0;i<jsarray.length;i++)
		{
			sum += parseInt(jsarray[i]);
		}
		log("sum =" + sum);
		sumReduce=sum;

		$.post("resultmanager",{result:sumReduce,resultType:"reduce"},function(data) { 
		      log("reduce results sent" + data);
			},"text");
	getStatus();
	 }

function log(toappend)
	{
	 if (logFlag) {
	 	var str = toappend;
	 	var newdiv = document.createElement("div")
	 	document.getElementById("logwindow").appendChild(newdiv) //append new div to another div
			newdiv.innerHTML = str;
			document.location = "#bottom";
		}
	}
