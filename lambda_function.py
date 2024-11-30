import sys
from dotenv import load_dotenv
import json
from upload_to_instagram import upload_post, login_instagram

# Load environment variables from the .env file
load_dotenv()


def handler(event, context):
    print({"event": event, "context": context})

    # image_url = "https://v5.airtableusercontent.com/v3/u/35/35/1733011200000/NqkUWIFWczhAiDYF8nYL-Q/nsdzwJtaSS6EgPFyPcfi6NxlQ5vJqdjGNizBjp5dWi7G_JvCYD4iu-ADTl48sVpj6aE60HTFraMj40JShUvJBNG6DYIVIQMMwYFcVO6aUyF1UjzQSWCxc2o4jEpf_9KgknpF5PzO8tlmSf89sY4Mvw/_PPYdmcKz23urDXG6fhc2HHcR33WW9rc4BsXAGW2kUE"
    # generated_post = "some post"

    
    body = event.get('body')
    if not body:
        raise ValueError("Request body is missing.")

    # Assume the body is JSON and parse it
    body_json = json.loads(body)

    # Extract the 'Generated Post' argument
    generated_post = body_json.get('Generated Post')
    if generated_post is None:
        raise ValueError("'Generated Post' argument is missing.")
    
    # save_path = download_photo(image_url)
    # print(f"image saved in {save_path}")

    print(generated_post)

    # print("about to upload post!")
    # cl = login_instagram()
    # upload_post(cl, image_url, generated_post)

    return 'Hello from AWS Lambda using Python' + sys.version + '!'


if __name__ == '__main__':
    handler({"hello": 2}, {"content": "hello"})
