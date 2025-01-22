Title: Το Ιατρείο
Slug: gallery
Order: 3

<div class="container section-padding"> 
	<div id="gallery">        
		<div class="isotope">
			<div class="item height14x cat-space">
				<div class="gallery-item">
					<img src="{{ SITEURL }}/{{ EOPYY_SERVICE_IMG }}" alt="{{ EOPYY_SERVICE }}" class="gallery-img" onclick="openPopup(this)"/>
                </div>
			</div><!-- /.item --> 
			<div class="item squire cat-aeronautics">
				<div class="gallery-item">
                    <img src="{{ SITEURL }}/{{ PREVENTIVE_MEDICINE_SERVICE_IMG }} " alt="{{ PREVENTIVE_MEDICINE_SERVICE }}" class="gallery-img" onclick="openPopup(this)"/>
                </div>
			</div><!-- /.item -->
			<div class="item squire cat-aeronautics">
				<div class="gallery-item">
					<img src="{{ SITEURL }}/{{ EMERGENCY_SERVICE_IMG }} " alt="{{ EMERGENCY_SERVICE }}" class="gallery-img" onclick="openPopup(this)"/>
				</div>
			</div><!-- /.item -->
			<div class="item squire cat-aeronautics">
				<div class="gallery-item">
					<img src="{{ SITEURL }}/{{ CHRONIC_DISEASES_SERVICE_IMG }} " alt="{{ CHRONIC_DISEASES_SERVICE }}" class="gallery-img" onclick="openPopup(this)"/>
				</div>
			</div><!-- /.item --> <div class="item height14x cat-space">
				<div class="gallery-item">
					<img src="{{ SITEURL }}/{{ ASSISTANCE_SERVICE_IMG }} " alt="{{ ASSISTANCE_SERVICE }}" class="gallery-img" onclick="openPopup(this)"/>
				</div>
			</div><!-- /.item --> 
			<div class="item squire cat-aeronautics">
				<div class="gallery-item">
					<img src="{{ SITEURL }}/{{ CERTIFICATES_SERVICE_IMG }} " alt="{{ CERTIFICATES_SERVICE }}" class="gallery-img" onclick="openPopup(this)"/>
				</div>						
			</div><!-- /.item -->            
		</div><!-- /.isotope -->
        <a href="{{ SITEURL }}/pages/contact.html" > Επικοινωνήστε </a>
	</div><!--  /.gallery -->
    <!-- Popup Container -->
    <div id="popup-container" class="popup-container">
        <span class="close-btn" onclick="closePopup()">&times;</span>
        <div class="popup-content">
            <img id="popup-image" class="popup-image" alt="Popup Image">
        </div>
    </div>
</div>


