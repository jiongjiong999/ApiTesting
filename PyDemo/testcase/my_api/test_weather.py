import allure
import requests

@allure.feature("公开接口测试")
class TestWeatherApi:

    @allure.story("验证天气接口状态码")
    def test_weather_status_code(self):
        url = "http://www.weather.com.cn/data/sk/101010100.html"
        res = requests.get(url)
        assert res.status_code == 200

    @allure.story("验证天气接口返回内容")
    def test_weather_content(self):
        url = "http://www.weather.com.cn/data/sk/101010100.html"
        res = requests.get(url)
        res.encoding = "utf-8"
        assert "北京" in res.text
