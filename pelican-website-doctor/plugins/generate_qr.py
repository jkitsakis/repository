import qrcode
from PIL import Image, ImageDraw, ImageFont


def generate_qr_with_text(data, filename="qrcode.png", output_size=(500, 500)):
    # Create QR code
    qr = qrcode.QRCode(
        version=3,  # Adjust complexity
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,  # Adjust QR code size
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create QR code image
    img = qr.make_image(fill="black", back_color="white").convert("RGB")

    # Resize QR code to desired size
    img = img.resize(output_size, Image.Resampling.LANCZOS)

    # Load font (adjust path if needed)
    try:
        font = ImageFont.truetype("arial.ttf", 40)  # Standard font
    except IOError:
        font = ImageFont.load_default()  # Fallback font

    draw = ImageDraw.Draw(img)

    # Define the text
    text = " Σκανάρετε για κλήση "

    # Calculate text size and position
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]  # Correct width calculation
    text_height = bbox[3] - bbox[1]  # Correct height calculation

    img_width, img_height = img.size
    text_x = (img_width - text_width) // 2
    text_y = (img_height - text_height) // 2

    # Draw white background for text
    draw.rectangle(
        [(text_x - 10, text_y - 5), (text_x + text_width + 10, text_y + text_height + 5)],
        fill="white"
    )

    # Draw the text
    draw.text((text_x, text_y), text, font=font, fill="black")

    # Save and show the image
    img.save(filename)
    img.show()
    print(f"QR Code saved as {filename}")


# Example Usage
if __name__ == "__main__":
    phone_number = "tel:2109921619"
    generate_qr_with_text(phone_number, "../content/images/telephone_qr.png", output_size=(500, 500))
