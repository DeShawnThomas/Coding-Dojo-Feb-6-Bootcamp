var helpTool = document.getElementById('operation')
//we will use this later, for now...disregard.
var display = document.getElementById('display')
var displayNum = ""
var storedNum = ""
var op = ""


//STEP 1: GRAB DISPLAY
//STEP 2: DECLARE VARIABLES (we can always add more later)
//STEP 3: WRITE PRESS FUNCTION (think about what we want to show the user)
//STEP 4: WRITE CLR FUNCTION (this is like a reset)
//STEP 5: WRITE OP FUNCTION
//STEP 6: WRITE CALCULATE FUNCTION

function press(num) {
    displayNum += num
    display.innerText = displayNum
    console.log(num)
}

function clr() {
    display.innerText = 0
    displayNum = ""
}

function setOP(operators) {
    op = operators
    storedNum = displayNum
    displayNum = ""
    helpTool.innerText = `You Stored ${storedNum} | Operand is ${op}`
}

function calculate() {
    storedNum = +storedNum
    displayNum = parseFloat(displayNum)
    console.log(storedNum, displayNum)
    if(op == '+'){
        display.innerText = storedNum + displayNum
    }else if(op == '-'){
        display.innerText = storedNum - displayNum
    }else if(op == '*'){
        display.innerText = storedNum * displayNum
    }
    else{
        display.innerText = storedNum / displayNum
    }
    // op == '+' ? display.innerText = storedNum + displayNum : null
    // op == '-' ? display.innerText = storedNum - displayNum : null
    // op == '*' ? display.innerText = storedNum * displayNum : null
    // op == '/' ? display.innerText = storedNum / displayNum : null
    storedNum = display.innerText
    helpTool.innerText = `Congratulations! Your result is ${storedNum}`
}