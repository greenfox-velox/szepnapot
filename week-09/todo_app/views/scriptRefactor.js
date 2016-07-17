'use strict';

var host = 'http://localhost:3000/todos';
var addButton = document.querySelector('button');
var app = document.querySelector('.app');
var todoList = document.querySelector('ul');
todoList.className = 'todo-list';
app.appendChild(todoList);



function sendRequest(method, url, data, cb) {
  var xhr = new XMLHttpRequest();
  xhr.open(method, host + url);
  xhr.setRequestHeader("content-type",'application/json');
  xhr.setRequestHeader('Access-Control-Allow-Origin', '*');
  xhr.setRequestHeader("Accept","text/plain");
  xhr.onload = function() {
    if ( xhr.readyState === 4) {
      cb(null, JSON.parse(xhr.responseText))
    }
  }
  xhr.send(data && JSON.stringify(data));
}

function initTodo(){
  sendRequest('GET', '', '', initTasks)
}

function update(err, res) {
  if (err) {
    console.log(err);
    return
  }
  createListElement(res, todoList)
}

function errorHandler(err, res) {
  if (err) {
    console.log("Error: " + err, "Response: " + res);
  }
  return
}

function resetList() {
  app.removeChild(todoList);
  todoList = document.createElement('ul');
  app.appendChild(todoList);
}

function createListElement(object, parent) {
  if (object.text === null || object.text.length < 1) { return ;}
  let todoElement = document.createElement('li');
  todoElement.innerHTML = '<span>' + object.text + '</span>';
  todoElement.className = object.id;
  todoElement.completed = String(object.completed).toLowerCase() === 'true';
  if (todoElement.completed) {todoElement.classList.toggle('checked');}
  parent.appendChild(todoElement);
  addOptionsTo(todoElement);
}

function addOptionsTo(task){
  let options = createOptions(task);
  task.appendChild(options);
}

function addEventTo(element, func) {
  element.addEventListener('click', func);
}

function createNodeWithClass(elementType, className) {
  let element = document.createElement(elementType);
  element.className = className;
  return element;
}

function createOptions(task) {
  let menu = createNodeWithClass('div','options')
  let del = createNodeWithClass('div','option-delete')
  let check = createNodeWithClass('input','option-check')
  check.type = 'checkbox';
  check.checked = String(task.completed).toLowerCase() === 'true';
  addEventTo(del, deleteTask);
  addEventTo(check, completeTodo);
  menu.appendChild(del);
  menu.appendChild(check);
  return menu;
}

function initTasks(err, res) {
  if (err) {
    console.log(err);
  }
  for (var i = 0; i < res.length; i++) {
    createListElement(res[i], todoList);
  }
}

function addTask(event) {
  event.preventDefault();
  let form = document.querySelector('form');
  let taskToAdd = document.querySelector('input').value;
  if (taskToAdd.length < 1) { return; }
  form.reset();
  taskToAdd = {text: taskToAdd, completed: 'false'};
  sendRequest('POST', '', taskToAdd, update);
}

function deleteTask(event) {
  event.preventDefault();
  let target = event.currentTarget;
  todoList.removeChild(target.parentNode.parentNode)
  let task = {id: target.parentNode.parentNode.className,
              text: target.parentNode.parentNode.textContent,
              completed: event.target.nextSibling.checked};
  sendRequest('DELETE', '/' + task.id, task, errorHandler);
}

function completeTodo(event) {
  let target = event.currentTarget;
  target.parentNode.parentNode.classList.toggle('checked');
  let task = {id: target.parentNode.parentNode.className,
              text: target.parentNode.parentNode.textContent,
              completed: target.checked}
  sendRequest('PUT', '/' + task.id, task, errorHandler);
}

addButton.addEventListener('click', addTask);
initTodo();
