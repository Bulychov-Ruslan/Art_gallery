// Проверка, работает ли JavaScript
document.addEventListener("DOMContentLoaded", function () {
    var jsMessage = document.getElementById("js-message");
    if (jsMessage) {
        jsMessage.innerHTML = "JavaScript работает на этой странице!";
    }
});

