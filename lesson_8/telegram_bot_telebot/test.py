import requests
import json

API_URL_NUMBERS = "http://numbersapi.com/100?json"
answer = requests.get(API_URL_NUMBERS)

print(json.loads(answer.text)['text'])