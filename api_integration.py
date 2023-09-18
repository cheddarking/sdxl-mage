```python
import requests
from constants import API_URL, API_KEY
from utils import format_error_message

def get_api_response(image_params):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
    }

    try:
        response = requests.post(API_URL, headers=headers, json=image_params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        error_message = format_error_message("HTTP error occurred", http_err)
        print(error_message)
    except Exception as err:
        error_message = format_error_message("An error occurred", err)
        print(error_message)
```