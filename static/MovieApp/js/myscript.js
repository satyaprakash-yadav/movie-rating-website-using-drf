// Message/Nofication timer

var message_timeout = document.getElementById("message-timer");

setTimeout(function(){

    message_timeout.style.display = "none";

}, 1000);

function ShowPass(){
    var pass1 = document.getElementById('id_password');

    if (pass1.type == 'password'){
        pass1.type = 'text';
    }
    else{
        pass1.type = 'password';
    }
}

/*
function incrementButton(){
    let element = document.getElementById("incrementText");
    let value = element.innerHTML;

    ++value;

    console.log(value);
    // document.getElementById("incrementText").innerHTML = value;
}
*/