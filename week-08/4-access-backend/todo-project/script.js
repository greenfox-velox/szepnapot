var xhr = new XMLHttpRequest();
var addButton = document.querySelector('button');
var app = document.querySelector('.app');
console.log(app);
var responseObject;

function addOptionsToTask(parent){
  let options = createOptions();
  parent.appendChild(options);
}

function createOptions() {
  let menu = createDivWithClass('options')
  let del = createDivWithClass('option-delete')
  let check = createDivWithClass('option-check')
  addEventTo(del, deleteTodo)
  menu.appendChild(del);
  menu.appendChild(check);
  return menu;
}

function addEventTo(element, func) {
  element.addEventListener('click', func);
}

function createDivWithClass(className) {
  let div = document.createElement('div');
  div.className = className;
  return div;
}

function refreshList() {
  let todoList = document.querySelector('ul');
  app.removeChild(todoList);
  todoList = document.createElement('ul');
  app.appendChild(todoList);
}

function appendToDo(object, parent) {
  if (object.text.length < 1) { return ;}
  todoElement = document.createElement('li');
  todoElement.textContent = object.text;
  todoElement.className = object.id;
  parent.appendChild(todoElement);
  addOptionsToTask(todoElement);
}

function printTodos() {
  let todoList = document.querySelector('ul');
  todoList.className = 'todo-list';
  for (var i = 0; i < responseObject.length; i++) {
    appendToDo(responseObject[i], todoList);
  }
  app.appendChild(todoList);
}



function getContent() {
  xhr.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos', true);
  xhr.responseType = 'json';
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
      if (xhr.status === 200 || 201 || 202 || 304 )
        { responseObject = xhr.response;
          refreshList();
          printTodos();
        }
       else {
        console.log('Error: ' + xhr.status);
      }
    }
  };
  xhr.send(null);
}

function postContent(data) {
  xhr.open('POST', 'https://mysterious-dusk-8248.herokuapp.com/todos', true);
  xhr.setRequestHeader("content-type",'application/json',
                      "Accept","text/html; charset=utf-8");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
      if (xhr.status === 200 || 201 || 202 || 304 )
        { getContent();}
       else {
        console.log('Error: ' + xhr.status);
      }
    }
  };
  xhr.send(data);

}

function deleteContent(id) {
  xhr.open('DELETE', 'https://mysterious-dusk-8248.herokuapp.com/todos/' + id, true);
  xhr.setRequestHeader("Accept",'application/json');
  let deleteObject = {};
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
      if (xhr.status === 200 || 201 || 202 || 304 )
        { getContent();}
       else {
        console.log('Error: ' + xhr.status);
      }
    }
  };
  // deleteObject.id = id;
  // xhr.send(JSON.stringify(deleteObject));
  xhr.send(null);
}


function deleteTodo(event) {
  let target = event.currentTarget;
  let idToDelete = target.parentNode.parentNode.className;
  deleteContent(idToDelete);
}

function addTodo(event) {
  event.preventDefault();
  let taskToAdd = document.querySelector('input').value;
  let task = {};
  task.text = taskToAdd;
  postContent(JSON.stringify(task));

}
getContent();
addButton.addEventListener('click', addTodo)
