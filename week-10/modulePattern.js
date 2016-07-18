'use strict';

const dog = (function() {
  let sound = 'woof';

  return {

    talk: function() {
      console.log(sound);
    }
  }
})();

dog.talk();
