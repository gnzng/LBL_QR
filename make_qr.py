from qrcode import create_qr_with_logo_and_text


# Step 1: Create a dictionary of QR code names and URLs
qrcodes = {
    "name1": "https://als.lbl.gov",
    "name2": "https://google.com",
    "name3": "https://github.com",
}

# Choose logo here, alqays use the .jpg version
# logo_path = "LBL_logos_bitmap/15_BL_Alt_Stack_Tile_rgb.jpg"
logo_dir = "ALS-Logos/ALS Logos Files for Electronic Applications (RGB)/ALS Vertical Signature/PNGs/"
logo_path = logo_dir + "0002_2016_ALS_VERTICAL_SIgnature_2_COLOR_RGB_ELECTRONIC.png"
# Save the QR codes with logos in the "finished_qrcodes" folder
path = "finished_qrcodes/"

for name, urls in qrcodes.items():
    output_path = path + f"{name}_with_logo.png"
    text = f"{name}"
    create_qr_with_logo_and_text(urls, output_path, logo_path, text, text_size=120)
print("Done.")
