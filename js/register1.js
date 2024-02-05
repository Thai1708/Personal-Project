function saveData() {
    var firstName = document.getElementById("firstname").value;
    sessionStorage.firstname = firstName;
    var lastName = document.getElementById("lastname").value;
    sessionStorage.lastname = lastName;
    var email = document.getElementById("email").value;
    sessionStorage.email = email;
    var phoneNumber = document.getElementById("phonenumber").value;
    sessionStorage.phonenumber = phoneNumber;
    var age = document.getElementById("age").value;
    sessionStorage.age = age;

    // if (document.getElementById("highschool").checked == true){
    //     sessionStorage.occupation = document.getElementById("highschool").value;
    // }
    // if (document.getElementById("university").checked == true){
    //     sessionStorage.occupation = document.getElementById("university").value;
    // }
    // if (document.getElementById("working").checked == true){
    //     sessionStorage.occupation = document.getElementById("working").value;
    // }
    // if (document.getElementById("retired").checked == true){
    //     sessionStorage.occupation = document.getElementById("retired").value;
    // }

    occupationArray = document.getElementById("occupation_group").getElementsByTagName("input");
    for (var i=0; i < occupationArray.length; i++){
        if (occupationArray[i].checked == true){
            sessionStorage.occupation = occupationArray[i].value;
        }

    }

    var course_logicmath = document.getElementById("course_logicmath").checked;
    var course_python = document.getElementById("course_python").checked;
    var course_web = document.getElementById("course_web").checked;
    var course_game = document.getElementById("course_game").checked;
    var course_ai = document.getElementById("course_ai").checked;
    var course_ds = document.getElementById("course_ds").checked;

    // luu du lieu duoi dang string
    sessionStorage.course_logicmath = course_logicmath;
    sessionStorage.course_python = course_python;
    sessionStorage.course_web = course_web;
    sessionStorage.course_game = course_game;
    sessionStorage.course_ai = course_ai;
    sessionStorage.course_ds = course_ds;

    var payment = document.getElementById("payment");
    sessionStorage.payment = payment.value;

}

function prefillData() {
    if (sessionStorage.firstname != null){
        document.getElementById("firstname").value = sessionStorage.firstname;
        document.getElementById("lastname").value = sessionStorage.lastname;
        document.getElementById("email").value = sessionStorage.email;
        document.getElementById("phonenumber").value = sessionStorage.phonenumber;
        document.getElementById("age").value = sessionStorage.age;
    }
    switch (sessionStorage.occupation){
        case "highschool":
            document.getElementById("highschool").checked = true;
        case "university":
            document.getElementById("university").checked = true;
        case "working":
            document.getElementById("working").checked = true;
        case "retired":
            document.getElementById("retired").checked = true;
    }

    if (sessionStorage.course_logicmath == "true"){
        document.getElementById("course_logicmath").checked = true;
    }
    if (sessionStorage.course_python == "true"){
        document.getElementById("course_python").checked = true;
    }
    if (sessionStorage.course_web == "true"){
        document.getElementById("course_web").checked = true;
    }
    if (sessionStorage.course_game == "true"){
        document.getElementById("course_game").checked = true;
    }
    if (sessionStorage.course_ai == "true"){
        document.getElementById("course_ai").checked = true;
    }
    if (sessionStorage.course_ds == "true"){
        document.getElementById("course_ds").checked = true;
    }

    document.getElementById("payment").value = sessionStorage.payment;
}

function init() {
    prefillData();
    var submitButton = document.getElementById("submit");
    submitButton.onclick = saveData;
}

window.onload = init;