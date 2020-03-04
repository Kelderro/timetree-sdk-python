import requests
import json
from models import (
    UserResponse,
    AttributesResponse
)
import os


class TimeTreeApi():
    DEFAULT_API_ENDPOINT = 'https://timetreeapis.com'

    def __init__(self, access_token, endpoint=DEFAULT_API_ENDPOINT):
        self.endpoint = endpoint
        self.headers = {
            'Accept': 'application/vnd.timetree.v1+json',
            'Authorization': 'Bearer ' + access_token
        }

    def get_user(self):
        response = self._get('/user')
        print(json.dumps(response.json()['data'], indent=4))
        return UserResponse.new_from_json_dict(response.json()['data'])

    def _get(self, path, endpoint=None, params=None, headers=None):
        url = (endpoint or self.endpoint) + path

        if headers is None:
            headers = {}
        headers.update(self.headers)

        response = requests.get(url, headers=headers, params=params)

        self.__check_error(response)
        return response

    @staticmethod
    def __check_error(response):
        if 200 <= response.status_code < 300:
            pass
        else:
            print(response.headers)
            raise response.status_code


if __name__ == '__main__':
    api = TimeTreeApi(os.environ['TIME_TREE_API_ACCESS_TOKEN'])
    response = api.get_user()
    print(response)