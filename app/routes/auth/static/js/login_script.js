var username = document.getElementById("username")
var password = document.getElementById("password")
var submit_btn = document.getElementById("submit")
var warn = document.getElementById("rd")
submit_btn.addEventListener("click" , function(){
    if(username.value === "" || password.value === ""){

    }else{
        send_info()
    }
})
function send_info(){
    const csrf = document.getElementById("csrf")
    fetch("/login-post" , {
    method : "POST",
    headers : {"Content-Type" : "application/json",
        "X-CSRFToken" : csrf.value
    },
    body : JSON.stringify({username:username.value , password:password.value})
    })
    .then(Response =>Response.json())
    .then(data=>{
        console.log(data)
        if(data.status === false){
            warn.textContent = data.reason
        }else{
             window.location.href = data.link   
        }
    })
}