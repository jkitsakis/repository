Title: {{ CONTACT_TITLE }}
Slug: contact
Order: 2

<h2>{{ CONTACT_TITLE }}</h2>
<div class="flex-container-contact"> 
    <div class="flex-item-contact">
        {{ ADDRESS_MAP_IFRAME }}
    </div>   
    <div class="flex-item-contact">
         <div class="contact-detail">
            <img src="{{ SITEURL }}/{{ OFFICE_TEL_IMG }}" alt="Phone Icon"  class="contact-icon"/>
            <a href="javascript:void(0);" onclick="openPopupLink(this)">
                {{ OFFICE_TEL }}
                <img src="{{ SITEURL }}/{{ OFFICE_TEL_QR_IMG }}" style="display:none;" alt="Service Image"/>
            </a>
        </div>  
         <div class="contact-detail">
            <img src="{{ SITEURL }}/{{ MOBILE_IMG }}" alt="Phone Icon" class="contact-icon"/>
            <a href="javascript:void(0);" onclick="openPopupLink(this)">
                {{ MOBILE }}
                <img src="{{ SITEURL }}/{{ MOBILE_QR_IMG }}" style="display:none;" alt="Service Image"/>
            </a>
        </div>  
         <div class="contact-detail">
                <img src="{{ SITEURL }}/{{ EMAIL_IMG }}" alt="Email Icon" class="contact-icon"/>
                <a href="mailto:{{ EMAIL }}" target="_blank">{{ EMAIL }}</a></div>   
         <div class="contact-detail">
            <img src="{{ SITEURL }}/{{ ADDRESS_IMG }}" alt="Location Icon" class="contact-icon"/>
            <a href="{{ ADDRESS_MAP_URL }}" target="_blank">{{ ADDRESS }}</a></div>   
    </div>
    <!-- Popup Container -->
    <div id="popup-container" class="popup-container">
        <span class="close-btn" onclick="closePopupLink()">&times;</span>
        <div class="popup-content">
            <img id="popup-image" class="popup-image" alt="Popup Image">
        </div>
    </div>
</div>





