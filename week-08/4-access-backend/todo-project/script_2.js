var host;
var addButton;
var app;
var todoList;

getGlobalElements();

function getGlobalElements() {
  addButton = document.querySelector('button');
  app = document.querySelector('.app');
  host = 'https://mysterious-dusk-8248.herokuapp.com/todos';
  todoList = document.querySelector('ul');
}

function initTasks(object) {
  object.forEach(function(task) {
    updateList(task);
  })
}

function addTaskToList(task) {
  todoList.appendChild(task);
}

function addEventTo(element, func) {
  element.addEventListener('click', func);
}

function addOptionsToTask(task){
  let options = createOptions(task);
  task.appendChild(options);
}

function createOptions(task) {
  let menu = createNodeWithClass('div','options')
  let del = createNodeWithClass('div','option-delete')
  let check = createNodeWithClass('input','option-check')
  check.type = 'checkbox';
  check.checked = task.completed;
  addEventTo(del, deleteTodo);
  addEventTo(check, completeTodo);
  menu.appendChild(del);
  menu.appendChild(check);
  return menu;
}

function createElement(type, className) {
  let element = document.createElement(elementType);
  element.className = className;
  return element;
}

function createNewTask(type, object) {
  let newTask = createElement('li', object.id);
  if (object.text.length < 1) { return; }
  newTask.innerHTML = '<span>' + object.text + '</span>';
  newTask.completed = object.completed;
  return newTask
}

function updateList(object) {
  console.log(object.id);
  let task = createNewTask(object);
  addTaskToList(task);
}

function makeRequest(type, endpoint, data, cb) {
  let xhr = new XMLHttpRequest();
  xhr.open(type, host + endpoint, true);
  xhr.responseType = 'json';
  xhr.setRequestHeader('Accept', 'text/html');
  xhr.setRequestHeader("content-type",'application/json');
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
      if (xhr.status === 200 || 201 || 202 || 304 )
        {
          cb(xhr.response);
        }
       else {
        console.log('Error: ' + xhr.status);
      }
    }
  };
  xhr.send(data);
}


function loadContent() {
  makeRequest('GET', '', null, function(response) { initTasks(response)})
}

loadContent()
