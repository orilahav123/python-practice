import requests


def get_temperature(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["current"]["temperature_2m"]
    else:
        return None


print("Tel Aviv:", get_temperature(32.08, 34.78))
print("Eilat:", get_temperature(29.56, 34.95))
print("Val Thorens:", get_temperature(45.1753, 6.3448))
