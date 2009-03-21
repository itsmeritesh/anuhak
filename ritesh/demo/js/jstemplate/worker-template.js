var wp = google.gears.workerPool;
//set this variable to send reuslt back to master code
var result;

//write map code here
function kahuna_mapFunction()
 {
 } 
kahuna_mapFunction();

wp.onmessage = function(a, b, message) {
   var result = "send result here";
   //var reply = message.body[0] + message.body[1] + "... " + message.body[2].helloWorld;
   wp.sendMessage(result, message.sender);
 } 
