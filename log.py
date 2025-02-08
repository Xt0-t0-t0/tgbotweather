from pyown import Client

def get_location(lat, lon):
    url = f"https://yandex.ru/pogoda/magnitogorsk?lat={lat}&lon={lon}&via=hnav&le_lightning=1"
    return url 

def weather(citys: str):
    own = Client("8d7d5dab829d9df163a54acd7b5156a0")
    mgr = own.weather_manager()
    server = mgr.weather_at_place(citys)
    weather = server.weather
    loc = get_location(server.loc.lat, server.loc.lon)
    temp = weather.temp("celsius")
    return temp, loc