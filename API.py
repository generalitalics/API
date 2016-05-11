import requests

city = str(input('City? '))
print(city)
url = 'http://api.openweathermap.org/data/2.5/weather'
param = { "q":city,
          "appid":"11c0d3dc6093f7442898ee49d2430d20",
          "units":"metric"
}

req = requests.get(url, params = param)
print(req.json())
data = req.json()

template = 'Current temperature in {} is {}'
print(template.format(city,data['main']['temp']))
