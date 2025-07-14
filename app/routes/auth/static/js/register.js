const username = document.getElementById("name")
var emailq = document.getElementById("email")
var password = document.getElementById("password")
var password_conf = document.getElementById("password-conf")
var submit_btn = document.getElementById("submit")
submit_btn.addEventListener("click" , function(){
    console.log("submit_clicked")
    console.log(username.value)
    send_data()
})

function send_data(){
    const csrf = document.getElementById("csrf")
fetch("/register-post" , {
    method : "POST" , 
    headers : { 
        "Content-Type" : "application/json",
        "X-CSRFToken" : csrf.value
    },
    body : JSON.stringify({
        username : username.value ,
        email : emailq.value , 
        password : password.value
    })
}).then(Response => Response.json())
.then(data =>{
console.log(data)
if(data.status === true){
    window.location.href = data.link
}else{
    console.log(data.reason)
    const sq =  document.getElementById("rd")
    sq.style = "display:flex; color:red;"
    sq.textContent = "Alert : " + data.reason
}
})
}