import os
from dotenv import load_dotenv
import requests
from instagrapi import Client

# Load environment variables from the .env file
load_dotenv()

# Access environment variables


def get_env_variable(variable_name):
    value = os.getenv(variable_name)
    if value is None:
        print(f"Warning: {variable_name} not found.")
    return value


username = get_env_variable("USERNAME")
password = get_env_variable("PASSWORD")

print({"fromdotenv": "hi", "username": username, "password": password})

cl = Client()
cl.login(username, password)


def download_photo(url, save_path):
    """
    Downloads a photo from the given URL and saves it to the specified path.

    :param url: str - The URL of the photo.
    :param save_path: str - The local file path where the photo will be saved.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Write the content to a file in binary mode
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Photo successfully downloaded and saved to {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download the photo: {e}")


def upload_post(image_url, post_text):
    image_path = "./New_Image.JPG"
    download_photo(image_url, image_path)

    media = cl.photo_upload(
        image_path,
        post_text,
        extra_data={
            "custom_accessibility_caption": "alt text example",
            "like_and_view_counts_disabled": 0,
            "disable_comments": 0,
        }
    )


# image_path = get_env_variable("IMAGE_PATH")
# post_text = "Test caption for photo with #hashtags and mention users such @example"
if __name__ == "__main__":
    image_url = "https://v5.airtableusercontent.com/v3/u/35/35/1733011200000/NqkUWIFWczhAiDYF8nYL-Q/nsdzwJtaSS6EgPFyPcfi6NxlQ5vJqdjGNizBjp5dWi7G_JvCYD4iu-ADTl48sVpj6aE60HTFraMj40JShUvJBNG6DYIVIQMMwYFcVO6aUyF1UjzQSWCxc2o4jEpf_9KgknpF5PzO8tlmSf89sY4Mvw/_PPYdmcKz23urDXG6fhc2HHcR33WW9rc4BsXAGW2kUE"
    post_text = """🌱 Staying fit isn’t just about hitting the gym; it’s a holistic journey! Here are a few tips to keep your body and mind in top shape:

1. **Move Daily**: Find an activity that brings you joy – whether it’s dancing, hiking, or yoga. It’s all about consistency!
2. **Nourish, Don't Deprive**: Fuel your body with wholesome foods. Think colorful plates packed with nutrients! 🥗
3. **Hydrate**: Water is your best friend. Stay hydrated to keep your energy levels up! 💧
4. **Rest & Recover**: Never underestimate the power of sleep. It’s essential for both physical and mental recovery.😴

Remember, fitness is a lifestyle, not a destination. Embrace the journey and celebrate your progress! 💪✨ #StayFit #SelfDevelopment #HealthyLiving
    """

    upload_post(image_url, post_text)
