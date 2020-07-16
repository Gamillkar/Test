import requests

text = 'привет'
URL = 'https://translate.yandex.net/api/v1/tr.json/translate?id=2d832986.5f0f237d.41882526.74722d74657874-0-0&srv=tr-text&lang=ru-en&reason=paste&format=text'
params = {
        "lang": "ru-en",
        'text': text
    }

def translate(data):
    if  data == '':
        raise Exception('нет данных')

    else:
        params = {
            "lang": "ru-en",
            'text': data
        }

        res = requests.post(URL,params=params)
        result = res.json()['text'][0]
        print(result)
        return result

if __name__ == '__main__':
    translate('Hi')

