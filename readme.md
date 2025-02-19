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
    "name1": "https://als.lbl.gov",
    "name2": "https://google.com",
}

# Choose logo here
logo_dir = "ALS-Logos/ALS Logos Files for Electronic Applications (RGB)/ALS Vertical Signature/PNGs/"
logo_path = logo_dir + "0002_2016_ALS_VERTICAL_SIgnature_2_COLOR_RGB_ELECTRONIC.png"

# Save the QR codes with logos in the "finished_qrcodes" folder
path = "finished_qrcodes/"

for name, urls in qrcodes.items():
    output_path = path + f"{name}_with_logo.png"
    text = f"{name}"
    create_qr_with_logo_and_text(urls, output_path, logo_path, text, text_size=120)
print("Done.")
```

## Example:

`name1_with_logo.png`

![Example QR Code with Logo](static/name1_with_logo.png)

## License

This project is licensed under the MIT License.