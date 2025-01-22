Title: Επικοινωνία
Slug: contact
Order: 1


<div class="content-list">   
    <div class="content-info">
        {{ ADDRESS_MAP_IFRAME }}
    </div>  
    <div class="content-info">
       <h3>{{ TIME_SCHEDULE_TITLE }}:</h3>
       <p>{{ TIME_SCHEDULE }}</p>
    </div>
    <div class="content-info">
      <img src="{{ SITEURL }}/{{ OFFICE_TEL_IMG }}" alt="Phone Icon"style="width:8%" >
      <a href="tel:{{ OFFICE_TEL }}" target="_blank">{{ OFFICE_TEL }}</a>
    </div>
    <div class="content-info">
      <img src="{{ SITEURL }}/{{ MOBILE_IMG }}" alt="Phone Icon"style="width:8%" >
      <a href="tel:{{ MOBILE }}" target="_blank">{{ MOBILE }}</a>
    </div>    
    <div class="content-info">
      <img src="{{ SITEURL }}/{{ EMAIL_IMG }}" alt="Email Icon" style="width:8%">
      <a href="mailto:{{ EMAIL }}" target="_blank">{{ EMAIL }}</a>
    </div>  
    <div class="content-info">
      <img src="{{ SITEURL }}/{{ ADDRESS_IMG }}" alt="Location Icon" style="width:8%">
      <a href="{{ ADDRESS_MAP_URL }}" target="_blank">{{ ADDRESS }}</a>
    </div> 
</div>


