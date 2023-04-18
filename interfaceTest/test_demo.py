from jsonpath import jsonpath
import requests
from hamcrest import assert_that, equal_to


class TestDemo:
    def test_get(self):
        r = requests.get("https://httpbin.testing-studio.com/get")
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        payload = {
            "level": 1,
            "name":  "seveniruby"
        }
        r = requests.get("https://httpbin.testing-studio.com/get", params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "level": 1,
            "name":  "seveniruby"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_upload(self):
        files = {
            "file": open('test.txt', 'rb')
        }
        r = requests.post("https://httpbin.testing-studio.com/post", files=files)
        print(r.text)
        assert r.status_code == 200

    def test_header(self):
        r = requests.get("https://httpbin.testing-studio.com/get", headers={"h": "header demo"})
        print(r.text)
        assert r.status_code == 200
        assert r.json()['headers']['H'] == 'header demo'

    def test_post_json(self):
        payload = {
            "level": 1,
            "name":  "seveniruby"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['level'] == 1

    def test_json(self):
        url = "https://home.testing-studio.com/categories.json"
        r = requests.get(url)
        # print(r.text)
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == '提问区'

    def test_hamcrest(self):
        r = requests.get("https://home.testing-studio.com/categories.json")
        # print(r.text)
        assert r.status_code == 200
        assert_that(r.json()['category_list']['categories'][0]['name'], equal_to('提问区'))

    def test_hogwarts_jsonpath(self):
        r = requests.get("https://home.testing-studio.com/categories.json")
        assert r.status_code == 200

        # assert r.json()['category_list']['categories'][0]['name'] == '提问区'
        assert jsonpath(r.json(), '$..name')[0] == '提问区'

    def test_cookies(self):
        url = "https://httpbin.testing-studio.com/cookies"
        header = {
            # "Cookie":     "hogwarts=school",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit"
        }
        cookie_data = {
            "hogwarts": "school",
            "teacher":  "Ad"
        }
        r = requests.get(url, headers=header, cookies=cookie_data)
        print(r.request.headers)
