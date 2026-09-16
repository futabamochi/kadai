import requests
city = input("都市名を入力して下さい：")
url = "https://api.weatherapi.com/v1/current.json"

params = {
    "key": "c159d390db47429682681640261609",
    "q": city
}
response = requests.get(url, params=params)
data = response.json()

print(data["current"]["temp_c"], "°c")
