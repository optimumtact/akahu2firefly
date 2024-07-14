import requests
import os
from dotenv import load_dotenv


url = "https://api.akahu.io/v1/refresh"

load_dotenv()
headers = {

    "Accept": "application/json",

    "X-Akahu-Id": os.getenv('AKAHU_APP_CLIENTID'),

    "Authorization": "Bearer "+os.getenv('AKAHU_TOKEN')

}
response = requests.post(url, headers=headers)
print(response.text)


url = os.getenv("FIREFLY_CRON_URL")
response = requests.get(url)
print(response.text)
