var count = 0;
var countElement = document.querySelector(".col-2 h2");

console.log(countElement);

function addLike() {
    count++;
    countElement.innerText = count + " like(s)";

    console.log(count);
}
