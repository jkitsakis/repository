// JavaScript to show/hide the Go to Top button
window.onscroll = function() {toggleGoToTopButton()};

function toggleGoToTopButton() {
    let button = document.getElementById("goToTop");
    // Show button if the user scrolls down 100px or more, otherwise hide it
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        button.style.display = "block";
    } else {
        button.style.display = "none";
    }
}

// Smooth scroll to the top
document.getElementById("goToTop").onclick = function() {
    window.scrollTo({ top: 0, behavior: "smooth" });
};
