'use strict';

const dog = (function() {
  let sound = 'woof';
  let name = "Borzos";

  function setName( dogName ) {
    name = dogName;
  }

  function getName(){
    console.log( "Name: " + name );
  }

  function talk() {
    console.log( sound );
  }

  return {
    talk: talk,
    getName: getName,
    setName: setName
  };
})();


dog.getName();
dog.talk();
