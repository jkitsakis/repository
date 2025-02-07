// Function to open the popup and display the clicked image
function openPopupLink(linkElement) {
    const popupContainer = document.getElementById('popup-container');
    const popupImage = document.getElementById('popup-image');
    const popupLink = document.getElementById('popup-link');
    const phoneNumber = linkElement.textContent.trim();

    // Set the source of the popup image to the clicked image's src
    popupImage.src = linkElement.querySelector('img').src;
    popupLink.href = "tel:" + phoneNumber;


    // Show the popup
     popupContainer.style.display = 'flex'; // Only show the popup when triggered
}

// Function to close the popup
function closePopupLink() {
    const popupContainer = document.getElementById('popup-container');
    popupContainer.style.display = 'none'; // Hide the popup

    // Clear the image source to avoid displaying empty space
    document.getElementById('popup-image').src = '';
}

// Ensure the popup stays hidden when the page is loaded or refreshed
window.onload = function() {
    const popupContainer = document.getElementById('popup-container');
    popupContainer.style.display = 'none'; // Make sure it's hidden by default
};
