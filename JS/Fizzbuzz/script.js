var x = 0;

for(var i=1; i<101; i++) {
    x += 1;
    if(x % 3 == 0 && x % 5 == 0)
    console.log("FizzBuzz");
    else if(x % 3 == 0)
    console.log("Fizz");
    else if(x % 5 == 0)
    console.log("Buzz");
    else
    console.log(x);
}
