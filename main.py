import json, requests, pprint

APPID = 'e10009724b5fae41113b72b06d103c3b'


def ingresar_ciudad():
    while True:
        nombre = input("Ingrese el nombre de la ciudad del Mundo (Pulse q/Q para salir): ").capitalize()
        if nombre == 'Q':
            exit()
        else:
            break
    return nombre

def validar_ciudad(location, APPID):
    while True:
        try:
            url = 'https://api.openweathermap.org/data/2.5/forecast?q=%s,ar&units=metric&lang=es&appid=%s' % (
            location, APPID)
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print("Ciudad inexistente:", errh)
            location = ingresar_ciudad()
            continue
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
            raise SystemExit(errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
            print("por favor, vuelva a intentar en unos segundos.")
            continue
        except requests.exceptions.RequestException as err:
            raise SystemExit(err)
        break
    return json.loads(response.text)

def mostrar_clima(weatherData):
    print('Clima proximas 24hs en %s:' % weatherData['city']['name'])
    w = weatherData['list']
    #el rango es de 0 a 8 porque la API devuelve el clima en intervalos de 3 hs. 24hs son 8 intervalos de 3hs
    for i in range(0, 8):
        print("Hora: " + w[i]['dt_txt'] + " - " + w[i]['weather'][0]['description'] + " - Temp: " + str(
            w[i]['main']['temp']) + "°C" +
              " - Temp MAX: " + str(w[i]['main']['temp_max']) + "°C - Temp MIN: " + str(
            w[i]['main']['temp_min']) + "°C" +
              " - Humedad: " + str(w[i]['main']['humidity']) + "%")


location = ingresar_ciudad()

weatherData = validar_ciudad(location,APPID)

mostrar_clima(weatherData)




