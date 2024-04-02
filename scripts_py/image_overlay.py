from PIL import Image
import pytesseract
import requests
from io import BytesIO
from googletrans import Translator
import cv2
import numpy as np
from PIL import ImageDraw, ImageFont

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image_url = 'https://hips.hearstapps.com/hmg-prod/images/color-quotes44-1603314416.jpg?crop=0.96xw:1xh;center,top&resize=980:*'
response = requests.get(image_url)
image_data = BytesIO(response.content)
image = Image.open(image_data)

extracted_text = pytesseract.image_to_string(image)
print("Extracted Text:", extracted_text)
avg_color = 'black'
translator = Translator()
translated_text = translator.translate(extracted_text, dest='hi').text
print("Translated Text:")
# print(translated_text.encode("utf-8").decode("cp1252"))


def remove_text(input_image_path, output_image_path, text_region):
    # Load the image
    if input_image_path.startswith('http'):
        response = requests.get(input_image_path)
        image = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)
    else:
        image = cv2.imread(input_image_path)

    if image is None:
        raise ValueError("Failed to load the image. Check the input path.")

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create a binary mask using adaptive thresholding
    _, mask = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

    # Extract the region where the text is located
    x, y, w, h = text_region
    roi = mask[y:y+h, x:x+w]

    # Check if the ROI has a valid size
    if np.count_nonzero(roi) == 0:
        raise ValueError("Text region is empty.")

    # Ensure mask and image have the same size
    roi = cv2.resize(roi, (image.shape[1], image.shape[0]))
    
    # Inpainting to fill the text region with the surrounding background
    result = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)

    # Save the output image
    cv2.imwrite(output_image_path, result)

    average_color = cv2.mean(image, mask=roi)[:3]
    complementary_color_int = tuple(int(255 - component) for component in average_color)
    return complementary_color_int

# Example usage
input_image_path = image_url
output_image_path = r'C:\Users\PARAM\Desktop\img_without_txt.jpeg'

# Text region (specify the coordinates and dimensions of the text region)
text_region_coordinates = (100, 100, 200, 50)  # Example coordinates (x, y, width, height)

avg_color = remove_text(input_image_path, output_image_path, text_region_coordinates)
print("Text Color (BGR):", avg_color)
image_o = Image.open(output_image_path)
draw = ImageDraw.Draw(image_o)
font = ImageFont.truetype(r"C:\Users\PARAM\Downloads\Noto_Sans_Devanagari\NotoSansDevanagari-VariableFont_wdth,wght.ttf", size=40)
text_position = (30, 30)

# Use Unicode characters directly in the draw.text function
draw.text(text_position, translated_text, font=font, fill=avg_color)
image_o.save(r'C:\Users\PARAM\Desktop\translated.jpeg')
