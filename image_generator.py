```python
import requests
from constants import API_URL, API_KEY
from utils import save_image

def generate_image(image_params):
    """
    Function to generate image using Stable Diffusion algorithm
    """
    response = get_api_response(image_params)
    if response.status_code == 200:
        image_data = response.json()
        save_image(image_data)
    else:
        raise Exception(f"Failed to generate image. API response: {response.text}")

def get_api_response(image_params):
    """
    Function to get response from AI image generation REST API
    """
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(API_URL, headers=headers, json=image_params)
    return response
```