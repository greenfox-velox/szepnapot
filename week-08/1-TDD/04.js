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
// enter(enterDate)
//  - it should store the date of entering
//
// getEnterDate()
//  - it should return the date of the last entering
//
// leave(price)
//  - it should decrease the balance with the price of the parking (that is given in an argument)
//
// getStats()
//  - it should give back a string like:
//    "Type: volvo, Color: red, Balance: 500"
//
//

var Car = (function() {
  var nextId = 0;

  return function Car(type, color, balance){
    this.type = type;
    this.color = color;
    this.balance = balance;
    this.id = nextId++;
    this.startedParkingTime = 0;
    this.enter = function(date) { this.startedParkingTime += date; }
    this.getEnterDate = function() {return this.startedParkingTime; }
    this.leave = function(price) { this.balance -= price ;}
    this.getStats = function() { return "Type: " + this.type + ", Color: " + this.color +
                                ", Balance: " + this.balance + ", ID: " + this.id}
  }
})();

var ferrari = new Car("Enzo", "red", 500) ;
// ferrari.leave(100);
// console.log(ferrari.getStats());
var fiat = new Car("Fiat", "blue", 200) ;
// console.log(fiat.getStats());
//
var opel = new Car("Opel", "pink", 400) ;
// console.log(opel.getStats());


function CarPark(income, startTime) {
  this.parkingFee = 40;
  this.income = 0;
  this.garage = []
  this.openTime = startTime;
  this.currentTime = this.openTime;
  this.elapseTime = function(hours) { this.currentTime += hours;}
  this.carEnter = function(car) { car.enter(this.currentTime); this.garage.push(car);}
  this.carLeave = function(id) {
    var _this = this;
     this.garage.forEach(function(car) {
        if(car.id === id) {
          let dateWhenCarEntered = car.getEnterDate();
          let payedAmount = _this.parkingFee * (_this.currentTime - dateWhenCarEntered);
          car.balance -= payedAmount;
          _this.income += payedAmount;
        }
      })
    }
  this.getStats = function() { return "Cars: " + this.garage.length + " Time: " + (this.currentTime - this.openTime) * 3600000 +
                              " Income: " + this.income};

  this.getParkingCarsSince= function(hours) {
    let matchingCars = [];
    this.garage.forEach(function(car) {
      if (car.startedParkingTime >= hours) { matchingCars.push(car);}
    });
  return matchingCars;
}
}

var park = new CarPark(0, 12);
console.log("Opened at:" + park.openTime);

park.carEnter(ferrari);
park.carEnter(opel);
console.log(park.garage);

park.elapseTime(2);
console.log("Current time: " + park.currentTime);

park.carLeave(0);
console.log(park.income);

console.log(park.getStats());
console.log(park.getParkingCarsSince(11));
park.elapseTime(1);
park.carEnter(fiat);
console.log(park.getParkingCarsSince(14));
module.exports = Car;
