function setCookie(name, value, days) {
    var date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000)); // Set expiry date
    var expires = "expires=" + date.toUTCString();
    document.cookie = name + "=" + value + ";" + expires + ";path=/";
}

// Function to get a cookie value
function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i].trim();
        if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

window.onload = function() {
    // Check if the user has already accepted cookies
//    if (getCookie('cookies-accepted') === 'true') {
//        // If the cookie is set, hide the banner
//        document.getElementById('cookie-banner').style.display = 'none';
//    } else {
//        // If the cookie is not set, show the banner
//        document.getElementById('cookie-banner').style.display = 'block';
//    }
//
//    // Handle the "Accept" button click
//    document.getElementById('accept-cookies').addEventListener('click', function() {
//        // Set the cookie indicating the user has accepted cookies
//        setCookie('cookies-accepted', 'true', 365); // Expires in 1 year
//        // Hide the banner after acceptance
//        document.getElementById('cookie-banner').style.display = 'none';
//    });
//
//    // Handle the "Accept" button click
//    document.getElementById('reject-cookies').addEventListener('click', function() {
//         document.getElementById('cookie-banner').style.display = 'none';
//    });
};