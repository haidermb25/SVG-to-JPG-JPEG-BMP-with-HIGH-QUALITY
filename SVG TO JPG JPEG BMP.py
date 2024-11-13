import requests
from wand.image import Image
from io import BytesIO

# URL of the SVG file
url = "https://stockiconblob.blob.core.windows.net/notes/Billfold Wallet_38.051.svg"

# Download the SVG file
response = requests.get(url)

if response.status_code == 200:
    with Image(file=BytesIO(response.content), resolution=2400) as img:
        img.resize(1024, 1024)
        img.format = 'jpg'
        img.save(filename="/content/output.jpg")

        img.format = 'jpeg'
        img.save(filename="/content/output.jpeg")

        img.format = 'bmp'
        img.save(filename="/content/output.bmp")

    print("Conversion successful. Saved as output.jpg, output.jpeg, and output.bmp")
else:
    print(f"Failed to fetch the SVG. Status code: {response.status_code}")
