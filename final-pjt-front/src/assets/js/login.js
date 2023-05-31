const loginForm = document.getElementById("login-form")
const loginButton = document.getElementById("login-form-submit")
const loginErrMsg = document.getElementById("login-err-msg")

loginButton.addEventListener("click", (event) => {
    event.preventDefault()
    console.log(loginForm.username)
    const username = loginForm.username.value
    const password = loginForm.password.value

    if (username === "user" && password === "web_dev") {
        alert("You have successfully logged in.")
        location.reload()
    } else {
        loginErrMsg.style.opacity = 1
    }
})