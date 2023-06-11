console.log("le js est géchar");

function getPassword(itemId) {
    var passwordSpan = document.getElementById("password-" + itemId);

    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://127.0.0.1:8000/item/' + itemId + '/');
    xhr.onload = function() {   
        if (xhr.status === 200) {
            passwordSpan.textContent = xhr.responseText;
        }
    };
    xhr.send();
}