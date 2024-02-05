function loadData() {
    var total = 0;

    var firstName = sessionStorage.firstname;
    var lastName = sessionStorage.lastname;
    var name = lastName + " " + firstName;
    var email = sessionStorage.email;
    var phoneNumber = sessionStorage.phonenumber;
    var age = sessionStorage.age;
    var occupation = sessionStorage.occupation;
    document.getElementById("name").textContent = name;
    document.getElementById("email").textContent = email;
    document.getElementById("phonenumber").textContent = phoneNumber;
    document.getElementById("age").textContent = age;
    document.getElementById("occupation").textContent = occupation;

    var courses = document.getElementById("courses");
    var myCourses = "";
    if (sessionStorage.course_logicmath == "true"){
        total += 499;
        myCourses += "Logic Math, ";
    }
    if (sessionStorage.course_python == "true"){
        total += 799;
        myCourses += "Python, ";
    }
    if (sessionStorage.course_web == "true"){
        total += 749;
        myCourses += "Web Basic, ";
    }
    if (sessionStorage.course_game == "true"){
        total += 199;
        myCourses += "Game, ";
    }
    if (sessionStorage.course_ai == "true"){
        total += 499;
        myCourses += "AI, ";
    }
    if (sessionStorage.course_ds == "true"){
        total += 249;
        myCourses += "Data Science, ";
    }
    myCourses = myCourses.substring(0, myCourses.length-2);
    courses.textContent = myCourses;

    var payment = document.getElementById("payment");
    payment.textContent = sessionStorage.payment;

    var totalHTML = document.getElementById("total");
    totalHTML.textContent = total;
}

function cancelButton() {
    window.location = "D:/FrontEnd/JavaScript/5.9/register1.html";
}

function init() {
    loadData();
    var cancel = document.getElementById("cancel");
    cancel.onclick = cancelButton;
}

window.onload = init;