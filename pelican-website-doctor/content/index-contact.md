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
            <img src="{{ SITEURL }}/{{ OFFICE_TEL_IMG }}" alt="Phone Icon"  class="contact-icon">
            <a href="tel:{{ OFFICE_TEL }}" target="_blank">{{ OFFICE_TEL }}</a></div>        
         <div class="contact-detail">
            <img src="{{ SITEURL }}/{{ MOBILE_IMG }}" alt="Phone Icon" class="contact-icon">
            <a href="tel:{{ MOBILE }}" target="_blank">{{ MOBILE }}</a></div>   
         <div class="contact-detail">
                <img src="{{ SITEURL }}/{{ EMAIL_IMG }}" alt="Phone Icon" class="contact-icon">
                <a href="mailto:{{ EMAIL }}" target="_blank">{{ EMAIL }}</a></div>   
         <div class="contact-detail">
            <img src="{{ SITEURL }}/{{ ADDRESS_IMG }}" alt="Location Icon" class="contact-icon">
            <a href="{{ ADDRESS_MAP_URL }}" target="_blank">{{ ADDRESS }}</a></div>   
    </div>
</div>





