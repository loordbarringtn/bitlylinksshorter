from dotenv import load_dotenv
import requests
import os
import argparse

def show_total_clicks_bitly(bitly_token,url):
    try:
      api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary'
      headers = {"Authorization": "Bearer " + bitly_token}
      response = requests.get(api_url, headers=headers)
      response.raise_for_status()
      return response.text
    except requests.exceptions.HTTPError as errh:
        return "An Http Error occurred:" + repr(errh)
    except requests.exceptions.ConnectionError as errc:
        return "An Error Connecting to the API occurred:" + repr(errc)
    except requests.exceptions.Timeout as errt:
        return "A Timeout Error occurred:" + repr(errt)
    except requests.exceptions.RequestException as err:
        return "An Unknown Error occurred" + repr(err)

def short_links_bitly(bitly_token, url):
    try:
      api_url='https://api-ssl.bitly.com/v4/bitlinks'
      headers = {"Authorization":"Bearer"}
      headers['Authorization'] = headers['Authorization'] + " " + bitly_token
      payload = {"long_url":''}
      payload['long_url'] = payload['long_url'] + url
      response = requests.post(api_url, json=payload, headers=headers)
      response.raise_for_status()
      return response.json()
    except requests.exceptions.HTTPError as errh:
      return "An Http Error occurred:" + repr(errh)
    except requests.exceptions.ConnectionError as errc:
        return "An Error Connecting to the API occurred:" + repr(errc)
    except requests.exceptions.Timeout as errt:
        return "A Timeout Error occurred:" + repr(errt)
    except requests.exceptions.RequestException as err:
        return "An Unknown Error occurred" + repr(err)

def main():
    load_dotenv()
    bitly_token = os.getenv("bitly_token")
    parser = argparse.ArgumentParser(description="Вы можете сократить web адрес или посмотреть количество переходов!")
    parser.add_argument("website_url", help="Введите web адрес",type=str)
    args = parser.parse_args()
    url=args.website_url
    if url.startswith('bit.ly'):
       print(show_total_clicks_bitly(bitly_token,url))
    else:
       print(short_links_bitly(bitly_token,url))

if __name__ == '__main__':
    main()
