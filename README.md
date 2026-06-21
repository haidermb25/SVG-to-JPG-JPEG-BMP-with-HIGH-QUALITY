# SVG to Image Converter

A simple Python script that downloads an SVG file from a URL and converts it into multiple image formats such as JPG, JPEG, and BMP using the Wand library.

## Features

* Download SVG from remote URL
* Convert SVG to high-resolution raster images
* Export in multiple formats (JPG, JPEG, BMP)
* Easy and lightweight script

## Technologies Used

* Python
* Requests
* Wand (ImageMagick binding)
* BytesIO

## How It Works

1. Fetch SVG file from URL using `requests`
2. Load image using `wand.image`
3. Convert and resize image
4. Save output in multiple formats

## Installation

Install dependencies:

```bash id="ins1"
pip install requests wand
```

Ensure ImageMagick is installed on your system.

## Usage

Run the script:

```bash id="run1"
python script.py
```

## Output

* output.jpg
* output.jpeg
* output.bmp

## Author

Ali Haider
Software Engineer
Python Developer
GitHub: https://github.com/haidermb25
