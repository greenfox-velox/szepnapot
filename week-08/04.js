'use strict';

// Automated CarPark system
//
// All the dates in this examples should be stored as a number
// The milliseconds lasted from 1970-01-01
//
// Create a Car constructor
// it should take 3 parameters
//  - type: the cars type as a string (eg: 'volvo')
//  - color: the cars type as a string (eg: 'red')
//  - balance: the cars parking credis as a number (eg: 500)
//
// every car should have an id property (a number), that is
// unique for all the cars, staeting form 0
//
// Methods:
// enter()
//  - it should store the date of entering
//
// leave(price)
//  - it should decrease the balance with the price of the parking (that is given in an argument)
//
// getStats()
//

var Car = (function() {
  var nextId = 0;

  return function Car(type, color, balance){
    let getCurrentDate = function() { return new Date();}
    this.type = type;
    this.color = color;
    this.balance = balance;
    this.id = nextId++;
    this.enter = function() { return getCurrentDate().getTime(); }
    this.parkingTime = getCurrentDate().getTime() - this.enter;
    this.leave = function(price) { this.balance -= price ;}
    this.getStats = function() { return "Type: " + this.type + ", Color: " + this.color +
                                ", Balance: " + this.balance + ", ID: " + this.id + ", Parking for: " + this.parkingTime}
  }
})()

var ferrari = new Car("Enzo", "red", 500) ;
console.log(ferrari.enter());
ferrari.leave(100);
console.log(ferrari.balance);
console.log(ferrari.getStats());

var fiat = new Car("Fiat", "blue", 200) ;
console.log(fiat.getStats());

var opel = new Car("Opel", "pink", 400) ;
console.log(opel.getStats());

module.exports = Car;
