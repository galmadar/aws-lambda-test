import sys
from dotenv import load_dotenv
from http_to_files import download_photo

# Load environment variables from the .env file
load_dotenv()


def handler(event, context):
    print({"event": event, "context": context})

    image_url = "https://v5.airtableusercontent.com/v3/u/35/35/1733011200000/NqkUWIFWczhAiDYF8nYL-Q/nsdzwJtaSS6EgPFyPcfi6NxlQ5vJqdjGNizBjp5dWi7G_JvCYD4iu-ADTl48sVpj6aE60HTFraMj40JShUvJBNG6DYIVIQMMwYFcVO6aUyF1UjzQSWCxc2o4jEpf_9KgknpF5PzO8tlmSf89sY4Mvw/_PPYdmcKz23urDXG6fhc2HHcR33WW9rc4BsXAGW2kUE"
    save_path = download_photo(image_url)
    print(f"image saved in {save_path}")

    return 'Hello from AWS Lambda using Python' + sys.version + '!'


if __name__ == '__main__':
    handler({"hello": 2}, {"content": "hello"})
