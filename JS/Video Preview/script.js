console.log("page loaded...");

function playVid(vid) { 
vid.play();
}

function pauseVid(vid) {
vid.pause();
vid.currentTime = 0;
}