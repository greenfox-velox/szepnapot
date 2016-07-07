var xhr = new XMLHttpRequest();
var addButton = document.querySelector('button');
var app = document.querySelector('.app');
console.log(app);
var responseObject;

function refreshList() {
  let todoList = document.querySelector('ul');
  app.removeChild(todoList);
  todoList = document.createElement('ul');
  app.appendChild(todoList);
}

function appendToDo(text, parent) {
  if (text.length < 1) { return ;}
  todoElement = document.createElement('li');
  todoElement.textContent = text;
  parent.appendChild(todoElement);
}
var printTodos = function() {
  let todoList = document.querySelector('ul');
  todoList.className = 'todo-list';
  for (var i = 0; i < responseObject.length; i++) {
    appendToDo(responseObject[i].text, todoList);
  }
  app.appendChild(todoList);
}



var getContent = function() {
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

var postContent = function(data) {
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

var addTodo = function(event) {
  event.preventDefault();
  let taskToAdd = document.querySelector('input').value;
  let task = {};
  task.text = taskToAdd;
  console.log(task);
  postContent(JSON.stringify(task));

}
getContent();
addButton.addEventListener('click', addTodo)
