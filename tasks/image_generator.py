from dotenv import load_dotenv
import requests
import os
load_dotenv()
access_key = os.getenv("UNSPLASH_ACCESS_KEY")
query = "page"

def dowload_image(query):
    url = f"https://api.unsplash.com/photos/random?query={query}&client_id={access_key}"
    response = requests.get(url)
    print(response.status_code)
    if response.status_code==200:
        data = response.json()
        img_url = data['urls']["full"]
        image_data = requests.get(img_url).content
        with open("download.jpg", "wb") as f:
            f.write(image_data)
            print("Image download sucessfully!")

dowload_image(query=query)