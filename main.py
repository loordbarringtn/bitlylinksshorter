from dotenv import load_dotenv
load_dotenv()
import requests
import os
import argparse

Bitly_token=os.getenv("Bitly_TOKEN")

def show_total_clicks_bitly(Bitly_token,url):
    try:
      api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary'
      headers = {"Authorization": "Bearer " + Bitly_token}
      response = requests.get(api_url, headers=headers)
      response.raise_for_status()
      print(response.text)
    except:
      return print("Что-то пошло не так... Возможно Вы ввели неправильно ссылку...")

def short_links_bitly(Bitly_token, url):
    try:
      api_url='https://api-ssl.bitly.com/v4/bitlinks'
      headers = {"Authorization":"Bearer"}
      headers['Authorization'] = headers['Authorization'] + " " + Bitly_token
      payload = {"long_url":''}
      payload['long_url'] = payload['long_url'] + url
      response = requests.post(api_url, json=payload, headers=headers)
      response.raise_for_status() 
      print(response.json())
    except:
      return print("Что-то пошло не так... Возможно Вы ввели неправильно ссылку...")


parser = argparse.ArgumentParser(description="Вы можете сократить web адрес или посмотреть количество переходов!")
parser.add_argument("website_url", help="Введите web адрес",type=str)
args = parser.parse_args()
url=args.website_url


if url.startswith('bit.ly'):
    show_total_clicks_bitly(Bitly_token,url)
else:
    short_links_bitly(Bitly_token,url)