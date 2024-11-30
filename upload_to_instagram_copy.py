import os

from http_to_files import download_photo

from instabot import Bot


# Upload a story


def get_env_variable(variable_name):
    value = os.getenv(variable_name)
    if value is None:
        print(f"Warning: {variable_name} not found.")
    return value


username = get_env_variable("USERNAME")
password = get_env_variable("PASSWORD")

print({"username": username, "password": password})

# Initialize a bot instance
bot = Bot()

# Login to your Instagram account
bot.login(username=username, password=password)

def upload_post(image_url, post_text):
    image_path = download_photo(image_url)
    bot.upload_story_photo(image_path, caption=post_text)
    
    # Logout from your Instagram account
    bot.logout()


# image_path = get_env_variable("IMAGE_PATH")
# post_text = "Test caption for photo with #hashtags and mention users such @example"
if __name__ == "__main__":
    # image_url = "https://v5.airtableusercontent.com/v3/u/35/35/1733011200000/NqkUWIFWczhAiDYF8nYL-Q/nsdzwJtaSS6EgPFyPcfi6NxlQ5vJqdjGNizBjp5dWi7G_JvCYD4iu-ADTl48sVpj6aE60HTFraMj40JShUvJBNG6DYIVIQMMwYFcVO6aUyF1UjzQSWCxc2o4jEpf_9KgknpF5PzO8tlmSf89sY4Mvw/_PPYdmcKz23urDXG6fhc2HHcR33WW9rc4BsXAGW2kUE"
    image_url = "https://v5.airtableusercontent.com/v3/u/35/35/1733018400000/CgCpUrqlzcF291coVfPkOA/aKqiUIovamZKeEcps5mvOBmLHyCgrLNjfNMeOflWE3DPoOHz7sJeFcC_WgjtbD-f3BDFOt1wq4BgeEJ97YSKUanRzp07B7-LDrVC4nrjU6K-fxb4vgct4j2H9CGTKIuGur9gVwIfqmUjc_VC27E4IA/KeRz5hDLZJhKvD-b3rsSX6spGN8R9bOdUtPQ8CC_d5o"
    post_text = """🌱 Staying fit isn’t just about hitting the gym; it’s a holistic journey! Here are a few tips to keep your body and mind in top shape:

1. **Move Daily**: Find an activity that brings you joy – whether it’s dancing, hiking, or yoga. It’s all about consistency!
2. **Nourish, Don't Deprive**: Fuel your body with wholesome foods. Think colorful plates packed with nutrients! 🥗
3. **Hydrate**: Water is your best friend. Stay hydrated to keep your energy levels up! 💧
4. **Rest & Recover**: Never underestimate the power of sleep. It’s essential for both physical and mental recovery.😴

Remember, fitness is a lifestyle, not a destination. Embrace the journey and celebrate your progress! 💪✨ #StayFit #SelfDevelopment #HealthyLiving
    """

    upload_post(image_url, post_text)
