# QR Code Generator with Logo

This project generates QR codes with embedded logos using Python. The QR codes are created with high error correction to ensure the logo can be embedded without affecting the readability of the QR code.

## Requirements

- Python 3.x
- segno
- Pillow

## Installation

Install the required packages using pip:

```sh
pip install segno pillow
```

## Usage

1. Create a dictionary of QR code names and URLs.
2. Specify the path to the logo image.
3. Generate the QR codes and embed the logo.

## Example

`main.py`:

```python
import segno
from PIL import Image

# Step 1: Create a dictionary of QR code names and URLs
qrcodes = {
    "als": "https://als.lbl.gov",
    "google": "https://google.com",
}

# Choose logo here
logo_dir = "ALS-Logos/ALS Logos Files for Electronic Applications (RGB)/ALS Vertical Signature/PNGs/"
logo_path = logo_dir + "0002_2016_ALS_VERTICAL_SIgnature_2_COLOR_RGB_ELECTRONIC.png"

# Save the QR codes with logos in the "finished_qrcodes" folder
path = "finished_qrcodes/"
for name in qrcodes.keys():
    qr = segno.make(qrcodes[name], error="h")  # High error correction level to ensure logo embedding
    qr.save(path + f"{name}.png", scale=50, dark="#00395A", light="white")  # Generate a larger QR code with higher resolution

    # Step 2: Open the high-resolution QR code and the logo image
    qr_img = Image.open(path + f"{name}.png").convert("RGBA")
    logo = Image.open(logo_path).convert("RGBA")

    # Step 3: Resize the logo while maintaining its aspect ratio
    logo_size_ratio = 4  # Adjust this ratio to control the size of the logo
    qr_width, qr_height = qr_img.size
    logo_width, logo_height = logo.size
    ratio = min(qr_width // logo_size_ratio / logo_width, qr_height // logo_size_ratio / logo_height)
    new_logo_size = (int(logo_width * ratio), int(logo_height * ratio))
    logo = logo.resize(new_logo_size, Image.LANCZOS)

    # Calculate position to paste the logo on the QR code (centered)
    x = (qr_width - logo_width) // 2
    y = (qr_height - logo_height) // 2

    # Step 4: Create a copy of the QR code to draw on
    qr_img_with_logo = qr_img.copy()

    # Step 5: Paste the logo onto the QR code
    qr_img_with_logo.paste(logo, (x, y), logo)  # Use logo as the mask directly

    # Save the final QR code with logo
    qr_img_with_logo.save(path + f"{name}_with_logo.png")
    print(f"{name} QR code with logo created successfully!")
```

## License

This project is licensed under the MIT License.