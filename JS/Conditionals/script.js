var number = 5;
console.log(number < 3); // this will log `false`

var isSunny = false;
var isRaining = true;
    
if(isSunny) {
    console.log("Wear sunscreen");
}
    
if(isRaining) {
    console.log("Bring an umbrella");
}

var today = new Date();
if(today.getDay() == 1) {
    console.log("I hate Mondays!");
} else if(today.getDay() == 5) {
    console.log("Friday? More like Fri-yay!");
} else {
    console.log("Today is alright!");
}


var temperature = 60; // let's assume this is degrees Fahrenheit
var isRaining = false;
    
if(temperature >= 50 && !isRaining) {
    console.log("This is a good day to go for a walk!");
}

var is5even = 5 % 2 == 0;
var is500even = 500 % 2 == 0;
    
// console.log(is5Even);   // false
// console.log(is500Even); // true
