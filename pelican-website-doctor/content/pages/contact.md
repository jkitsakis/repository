Title: Επικοινωνία
Slug: contact
Order: 1


<table class="post-content" style="background:none; border:none">
    <tr >
        <!-- Map in the first row -->
        <td colspan="2" style="background:none; border:none">
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3147.470283633111!2d23.737692499999994!3d37.919442499999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14a1bddd0c15cecd%3A0x6b4c9fdbd96baeb1!2zzonPgc-Jzr_PgiDOnM6sz4TPg863IDcwLCDOhs67zrnOvM6_z4IgMTc0IDU2!5e0!3m2!1sel!2sgr!4v1707293961096!5m2!1sel!2sgr"
                style="border:0; height:350px; width:100%;" 
                allowfullscreen="true" 
                loading="eager" 
                referrerpolicy="no-referrer-when-downgrade"></iframe>
        </td>
    </tr>
    <tr>
        <!-- Contact details in the second row -->
        <td style="background:none; border:none">
            <div class="contact-item">
                <img src="{{ SITEURL }}/images/locate.png" alt="Location Icon" class="reduced-width">
                <p><a href="https://maps.app.goo.gl/RstcEQ91LDKZVg2d8" target="_blank">{{ ADDRESS }}</a></p>
            </div>
        </td>
    </tr>
    <tr>
        <td style="background:none; border:none">
            <div class="contact-item">
                <img src="{{ SITEURL }}/images/email.png" alt="Email Icon" class="reduced-width">
                <p><a href="mailto:{{ EMAIL }}" target="_blank">{{ EMAIL }}</a></p>
            </div>
        </td>
    </tr>
    <tr>
         <td style="background:none; border:none">
            <div class="contact-item">
                <img src="{{ SITEURL }}/images/tel.png" alt="Phone Icon" class="reduced-width">
                <p><a href="tel:{{ MOBILE }}" target="_blank">{{ MOBILE }}</a></p>
            </div>
        </td>
    </tr>
</table>
