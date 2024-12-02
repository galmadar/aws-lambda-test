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

    print(body)
    # Extract the 'Generated Post' argument
    body = json.loads(body)
    
    generated_post = body.get('Generated Post')
    if generated_post is None:
        raise ValueError("'Generated Post' argument is missing.")

        
    ai_creation_url = body.get("AI Creation")
    ai_creation_url = ai_creation_url[0]
    ai_creation_url = ai_creation_url.get("thumbnails").get("full").get("url")
    print(ai_creation_url)
    if ai_creation_url is None:
        raise ValueError("'AI Creation' argument is missing.")
    
    # save_path = download_photo(image_url)
    # print(f"image saved in {save_path}")

    print("about to upload post!")
    cl = login_instagram()
    upload_post(cl, ai_creation_url, generated_post)

    return 'Hello from AWS Lambda using Python' + sys.version + '!'


if __name__ == '__main__':
    handler({"hello": 2}, {"content": "hello"})
