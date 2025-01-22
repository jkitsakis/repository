Title: {{ CONTACT_TITLE }}
Slug: contact
Order: 2

<h2>{{ CONTACT_TITLE }}</h2>
<div class="content-list">   
    <div class="content-info">
      {{ ADDRESS_MAP_IFRAME }}
    </div>   
    <div class="content-info">
      <img src="{{ SITEURL }}/{{ OFFICE_TEL_IMG }}" alt="Phone Icon"style="width:40px" >
      <a href="tel:{{ OFFICE_TEL }}" target="_blank">{{ OFFICE_TEL }}</a>
    </div>
    <div class="content-info">
      <img src="{{ SITEURL }}/{{ MOBILE_IMG }}" alt="Phone Icon"style="width:40px" >
      <a href="tel:{{ MOBILE }}" target="_blank">{{ MOBILE }}</a>
    </div>    
    <div class="content-info">
      <img src="{{ SITEURL }}/{{ EMAIL_IMG }}" alt="Email Icon" style="width:40px">
      <a href="mailto:{{ EMAIL }}" target="_blank">{{ EMAIL }}</a>
    </div>  
    <div class="content-info">
      <img src="{{ SITEURL }}/{{ ADDRESS_IMG }}" alt="Location Icon" style="width:40px">
      <a href="{{ ADDRESS_MAP_URL }}" target="_blank">{{ ADDRESS }}</a>
    </div> 
</div>



