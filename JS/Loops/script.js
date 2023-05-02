for(var i=0; i<3; i++) {
    console.log(i);
}

for(var i=10; i>0; i--) {
    console.log(i);
}


for(var i=12; i>3; i-=2) {
    console.log(i);
}
// this will print 12, 10, 8, 6, 4
    
for(var i=0.25; i<3; i+=0.5) {
    console.log(i);
}
// this will print 0.25, 0.75, 1.25, 1.75, 2.25, 2.75

for(var i=0; i<3; i++) {
    console.log(i);
}
    
var i = 0;
while(i<3) {
    console.log(i);
    i++;
}

var start = 0;
var end = 10;
    
while(start <= end) {
    console.log("start: " + start + ", end: " + end);
    start++;
    end--;
}

var x = 0;
for(var i=1; i<5; i++) {
    x += i;
}
console.log(x);