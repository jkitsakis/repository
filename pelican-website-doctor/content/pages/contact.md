Title: Επικοινωνία
Slug: contact
Order: 1


<div class="content-list">   
    <div class="content-info">
        {{ ADDRESS_MAP_IFRAME }}
    </div>      
    <div class="content-info">
        <img src="{{ SITEURL }}/{{ OFFICE_TEL_IMG }}" alt="Phone Icon"style="width:8%" />
        <a href="javascript:void(0);" onclick="openPopupLink(this)">
            {{ OFFICE_TEL }}
            <img src="{{ SITEURL }}/{{ OFFICE_TEL_QR_IMG }}" style="display:none;" alt="Service Image"/>
        </a>
    </div>
    <div class="content-info">
        <img src="{{ SITEURL }}/{{ MOBILE_IMG }}" alt="Phone Icon"style="width:8%" />
        <a href="javascript:void(0);" onclick="openPopupLink(this)">
            {{ MOBILE }}
            <img src="{{ SITEURL }}/{{ MOBILE_QR_IMG }}" style="display:none;" alt="Service Image"/>
        </a>
    </div>    
    <div class="content-info">
      <img src="{{ SITEURL }}/{{ EMAIL_IMG }}" alt="Email Icon" style="width:8%"/>
      <a href="mailto:{{ EMAIL }}" target="_blank">{{ EMAIL }}</a>
    </div>  
    <div class="content-info">
      <img src="{{ SITEURL }}/{{ ADDRESS_IMG }}" alt="Location Icon" style="width:8%"/>
      <a href="{{ ADDRESS_MAP_URL }}" target="_blank">{{ ADDRESS }}</a>
    </div> 
    <div class="content-list">   
        <div class="content-info">
           <h3>{{ TIME_SCHEDULE_TITLE }}:</h3>
           <p>{{ TIME_SCHEDULE }}</p>
        </div>
    </div>
    <!-- Popup Container -->
    <div id="popup-container" class="popup-container">
        <span class="close-btn" onclick="closePopupLink()">&times;</span>
        <div class="popup-content">
            <a id="popup-link" class="popup-link" href="#" target="_blank">
                <img id="popup-image" class="popup-image" alt="Popup Image">
            </a>
        </div>
    </div>
</div>


