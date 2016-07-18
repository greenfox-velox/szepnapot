'use strict';

const dog = {
  getName: function () {
    console.log("Name: " + this.name);
  },

  sound: function () {
    console.log(this.bark);
  }
};

var sniffles = Object.create( dog, {
  name: { writable: true, configurable: true, value: 'Sniffles' },
  bark: { writable: true, configurable: true, value: "Waaaaaaff"}
});

sniffles.getName();
sniffles.sound();
