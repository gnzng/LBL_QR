import segno
from PIL import Image, ImageDraw, ImageFont


def create_qr_with_logo_and_text(url, output_path, logo_path, text=None, text_font="Arial.ttf", text_size=160):
    # Generate the QR code
    qr = segno.make(url, error="h")
    qr.save(output_path, scale=50, dark="#00395A", light="white")

    # Open the high-resolution QR code and the logo image
    qr_img = Image.open(output_path).convert("RGBA")
    logo = Image.open(logo_path).convert("RGBA")

    # Resize the logo while maintaining its aspect ratio
    logo_size_ratio = 4
    qr_width, qr_height = qr_img.size
    logo_width, logo_height = logo.size
    ratio = min(qr_width // logo_size_ratio / logo_width, qr_height // logo_size_ratio / logo_height)
    new_logo_size = (int(logo_width * ratio), int(logo_height * ratio))
    logo = logo.resize(new_logo_size, Image.LANCZOS)

    # Calculate position to paste the logo on the QR code (centered)
    x = (qr_width - logo.size[0]) // 2
    y = (qr_height - logo.size[1]) // 2

    # Create a copy of the QR code to draw on
    qr_img_with_logo = qr_img.copy()

    # Paste the logo onto the QR code
    qr_img_with_logo.paste(logo, (x, y), logo)

    if text:
        # Add text field at the top of the QR code
        draw = ImageDraw.Draw(qr_img_with_logo)
        try:
            font = ImageFont.truetype(text_font, text_size)  # Ensure the font file is available
        except IOError:
            font = ImageFont.load_default()  # Use default bitmap font if specified font is not available

        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        # text_height = text_bbox[3] - text_bbox[1]
        text_x = (qr_width - text_width) // 2
        text_y = 10  # Adjust the y position as needed

        draw.text((text_x, text_y), text, fill="#00395A", font=font)

    # Save the final QR code with logo and text
    qr_img_with_logo.save(output_path)
    # Delete the QR code without the logo
    qr_img.close()
    print(f"QR code with logo and text created successfully at {output_path}!")
