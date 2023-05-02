// function chooseLunch(element) {
//     alert("You picked " + element.value);
// }

var nameTag = document.querySelector("#name-tag");
function setName(element) {
    console.log(element.value);
    nameSpan.innerText = element.value;
}
