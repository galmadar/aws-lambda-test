import sys
from dotenv import load_dotenv
import json
from upload_to_instagram import upload_post, login_instagram

# Load environment variables from the .env file
load_dotenv()


def handler(event, context):
    print({"event": event, "context": context})

    body = event.get('body')
    body = event.get('body')

    if not body:
        raise ValueError("Request body is missing.")

    body = json.loads(body)
    
    generated_post = body.get('Generated Post')
    if generated_post is None:
        raise ValueError("'Generated Post' argument is missing.")

        
    ai_creation_url = body.get("AI Creation")
    ai_creation_url = ai_creation_url[0]
    ai_creation_url = ai_creation_url.get("thumbnails").get("full").get("url")
    if ai_creation_url is None:
        raise ValueError("'AI Creation' argument is missing.")
    
    print("about to upload post!")
    cl = login_instagram()
    upload_post(cl, ai_creation_url, generated_post)

    return 'Hello from AWS Lambda using Python' + sys.version + '!'
