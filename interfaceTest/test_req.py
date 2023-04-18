import requests


class TestReq:
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_data(self):
        data = {"hogwarts": "school"}
        # 通过data参数传入请求体信息
        r = requests.post("https://httpbin.testing-studio.com/post", data=data,
                          verify=False)
        print(r.json())
        pass

    def test_json(self):
        data = {"hogwarts": "school"}
        # 通过json参数传入请求体信息
        r = requests.post("https://httpbin.testing-studio.com/post", json=data,
                          verify=False)
        print(r.json())
        pass
