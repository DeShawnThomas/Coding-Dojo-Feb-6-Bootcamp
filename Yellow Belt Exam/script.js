console.log("bark meow");

var donation = document.querySelector(".donation")

function getMoney() {
    donation.remove();
}

var likes = [3, 5, 8];
var spans = [document.querySelector("#post-1"), document.querySelector("#post-2"), document.querySelector("#post-3")];

function like(id)   {
    likes[id] ++;
    spans[id].innerHTML = likes[id] + " petting(s)";
}

function choice(select) {
    alert(select.options[select.selectedIndex].text);
}
