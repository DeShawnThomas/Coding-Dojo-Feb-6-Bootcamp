console.log("page loaded...");

// var count = 0;
// var countprofileChange = document.querySelector(".col-2 h2");

// console.log(countprofileChange);




function editProfile(profileChange) {
    var profileChange = document.querySelector(".card-body h1");
    if(profileChange.innerText == "Jane Doe") {
        profileChange.innerText = "Casey Martin";
    } 
    else {profileChange.innerText = "Jane Doe";
    }
}
