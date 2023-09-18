```python
import os
from PIL import Image

def format_error_message(error):
    return f"An error occurred: {str(error)}"

def save_image(image_data, filename):
    if not os.path.exists('images'):
        os.makedirs('images')
    image_path = os.path.join('images', filename)
    with open(image_path, 'wb') as file:
        file.write(image_data)
    return image_path

def display_image(image_path):
    image = Image.open(image_path)
    image.show()
```