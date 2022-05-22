import requests
import unittest
TARGER_URL = 'https://playground.learnqa.ru/api/'
HTTP_OK = 200


class TestUserlogin(unittest.TestCase):


    def test_login_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response = requests.post(f'{TARGER_URL}user/login', data=data)
        self.assertEqual(HTTP_OK, response.status_code)

        headers = response.headers
        token = headers['x-csrf-token']
        auth_sid = response.cookies['auth_sid']

    def test_create_user(self):
        reg_data = {
            'username': 'helensan',
            'firstName': 'Helen',
            'lastName': 'Smith',
            'email': 'testuser22244'
                     '445@example.com',
            'password': '1234'
        }
        response = requests.post(f'{TARGER_URL}user', data=reg_data)
        self.assertEqual(HTTP_OK, response.status_code)
        print(response.json())
        data = response.json()
        user_id = data['id']
        self.assertTrue('id' in list(data.keys()))

        login_data = {
            'email': 'testuser22244445@example.com',
            'password': '1234'
        }

        response = requests.post(f'{TARGER_URL}user/login', data=login_data)
        self.assertEqual(HTTP_OK, response.status_code)
        print(response.json())
        headers = response.headers
        token = headers['x-csrf-token']
        auth_sid = response.cookies['auth_sid']

        #delete
        response = requests.delete(
            f'{TARGER_URL}user/{user_id}',
        headers={'x-csrf-token': token},
        cookies={'auth_sid': auth_sid},
        )
        self.assertEqual(HTTP_OK, response.status_code)

        response = requests.get(
            f'{TARGER_URL}user/{user_id}',
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid},
        )
        self.assertEqual(404, response.status_code)
        print(response.status_code)

