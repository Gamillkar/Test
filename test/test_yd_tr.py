import unittest
from yandex_translate import translate
import yandex_translate
import requests


class Test_yd_translate(unittest.TestCase):
    """Тестирвоание yandex_translate"""

    def test_response_200(self): #проверка response 200
        test_res = requests.post(yandex_translate.URL, params=yandex_translate.params)
        self.assertEqual(200, test_res.json()['code'])

    def test_translate_hi(self): #проверка правильного перевода
        result = translate('привет')
        self.assertEqual('hi', result)

    def test_neg(self): #негативный тест на проверку отсутствия введенных данных
        with self.assertRaises(Exception):
            translate('')

