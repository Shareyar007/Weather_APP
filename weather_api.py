# weather api
import requests

def format_response(weather_json):
    #format json data of weather
    try:
        city_name       = weather_json['name']
        condition       = weather_json['weather'][0]['description']
        temparature     = weather_json['main']['temp']
        icon_name       = weather_json['weather'][0]['icon']
        weather_report    = 'City: %s \nCondition: %s \nTemperature (°F): %s' % (city_name, condition, temparature)
    except:
        weather_report = 'OOPS!, Failed to retriving information'
        icon_name = ''
    return (weather_report, icon_name)

def weather_information(city_name):
    #get weather information by calling openweather api
    weather_key = '393cdd3b59458f24abdadaf41ffe29d8'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q':city_name, 'units': 'imperial'}
    response = requests.get(url, params)
    weather_data = response.json()
    # print(weather_data)
    weather_report = format_response(weather_data)
    return weather_report
