from instagrapi import Client
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
def get_env_variable(variable_name):
    value = os.getenv(variable_name)
    if value is None:
        print(f"Warning: {variable_name} not found in .env file.")
    return value

username = get_env_variable("USERNAME")
password = get_env_variable("PASSWORD")

cl = Client()
cl.login(username, password)

image_path = get_env_variable("IMAGE_PATH")

media = cl.photo_upload(
    image_path,
    "Test caption for photo with #hashtags and mention users such @example",
    extra_data={
        "custom_accessibility_caption": "alt text example",
        "like_and_view_counts_disabled": 1,
        "disable_comments": 1,
    }
)
