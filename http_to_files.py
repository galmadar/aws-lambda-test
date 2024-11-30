import requests


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
