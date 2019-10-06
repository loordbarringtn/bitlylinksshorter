from dotenv import load_dotenv
import requests
import os
import argparse

def show_total_clicks_bitly(bitly_token,url):
      api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary'
      headers = {"Authorization": "Bearer " + bitly_token}
      response = requests.get(api_url, headers=headers)
      response.raise_for_status()
      return response.text

def short_links_bitly(bitly_token, url):
      api_url='https://api-ssl.bitly.com/v4/bitlinks'
      headers = {"Authorization":"Bearer"}
      headers['Authorization'] = headers['Authorization'] + " " + bitly_token
      payload = {"long_url":''}
      payload['long_url'] = payload['long_url'] + url
      response = requests.post(api_url, json=payload, headers=headers)
      response.raise_for_status()
      return response.json()

def main():
    load_dotenv()
    bitly_token = os.getenv("bitly_token")
    parser = argparse.ArgumentParser(description="Вы можете сократить web адрес или посмотреть количество переходов!")
    parser.add_argument("website_url", help="Введите web адрес",type=str)
    args = parser.parse_args()
    url=args.website_url
    try:
        if url.startswith('bit.ly'):
           print(show_total_clicks_bitly(bitly_token,url))
        else:
           print(short_links_bitly(bitly_token,url))
    except requests.exceptions.HTTPError as errh:
        print  ("An Http Error occurred:" + repr(errh))
    except requests.exceptions.ConnectionError as errc:
        print ("An Error Connecting to the API occurred:" + repr(errc))
    except requests.exceptions.Timeout as errt:
        print ("A Timeout Error occurred:" + repr(errt))
    except requests.exceptions.RequestException as err:
        print ("An Unknown Error occurred" + repr(err))

if __name__ == '__main__':
    main()
