var log_button = document.getElementById("log_button");

function new_log(){
  console.log("new log");
  var input = document.createElement('input'); 
  var p = document.createElement('p');
  //add increment
  p.id = "das";
  const date = new Date()
  var today = date.getDate().toString() +"/"+ (date.getMonth() + 1).toString() +"/"+ date.getFullYear().toString();
  p.innerHTML = "Log do dia " + today;
  input.type = "text";
  document.getElementById('Logs').appendChild(p);
  document.getElementById('das').appendChild(input);
}

log_button.addEventListener("click", new_log);