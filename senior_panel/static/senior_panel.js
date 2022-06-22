$('#datetime').datetimepicker({ 
  format: 'YYYY-MM-DD',
  defaultDate: moment(),
});

function showTime(){
  var date = new Date();
  var h = date.getHours();
  var m = date.getMinutes();
  var s = date.getSeconds();
  var session = "AM"

  if(h>12){
      h = h - 12;
      session = "PM"
  }

  h = (h<10) ? "0" + h : h;
  m = (m<10) ? "0" + m : m;
  s = (s<10) ? "0" + s : s; 
  
  var time = h + ":" + m + ":" + s + " " + session;
  document.getElementById("clock").innerHTML = time;
  document.getElementById("clock").textContent = time;

  setTimeout(showTime, 1000);
}
showTime();

function getWeek(){
  var date = new Date();
  var weekday = date.getDay();
  var d = date.getDate();
  var m = date.getMonth();
  var y = date.getFullYear();

  var arr = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

 document.getElementById("week").textContent = arr[weekday];

  var info = arr[weekday] + ", " + d + ", " + m + ", " + y; 
  document.getElementById("week").innerHTML = info
  document.getElementById("week").textContent = info
}
getWeek();

function showEditCalendar(show){
  var elements = document.getElementsByClassName('my-calendar');
  for (var i = 0; i < elements.length; ++i) {
      elements[i].style.display = (show) ? 'none' : 'block';
  }

  elements = document.getElementsByClassName('my-calendar-edit');
  for (var i = 0; i < elements.length; ++i) {
      elements[i].style.display = (show) ? 'inline-block' : 'none';
  }

  elements = document.getElementsByClassName('my-calendar-edit-2');
  for (var i = 0; i < elements.length; ++i) {
      elements[i].style.display = (show) ? 'inline-block' : 'none';
  }
}

function showEditPicture(show){
  var elements = document.getElementsByClassName('carousel-display');
  for (var i = 0; i < elements.length; ++i) {
      elements[i].style.display = (show) ? 'none' : 'block';
  }

  elements = document.getElementsByClassName('carousel-edit');
  for (var i = 0; i < elements.length; ++i) {
      elements[i].style.display = (show) ? 'inline-block' : 'none';
  }
}

function showEditHeader(show){
  var elements = document.getElementsByClassName('header-display');
  for (var i = 0; i < elements.length; ++i) {
      elements[i].style.display = (show) ? 'none' : 'block';
  }

  elements = document.getElementsByClassName('header-edit');
  for (var i = 0; i < elements.length; ++i) {
      elements[i].style.display = (show) ? 'block' : 'none';
  }
}
