import requests
from datetime import date


def obtener_tiempo_hoy():
    # Endpoint para obtener el pronóstico del tiempo para hoy en la ciudad de Madrid, España
    url = "https://www.el-tiempo.net/api/json/v2/provincias/28/municipios/28079"

    try:
        # Realizamos la solicitud GET a la API del tiempo
        response = requests.get(url)
        # Verificamos si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Convertimos la respuesta a formato JSON
            data = response.json()

            # Convertimos las cadenas de texto a números enteros
            temperaturas_int = [int(temperatura) for temperatura in data['pronostico']['hoy']['temperatura']]
            # Calculamos la media de las temperaturas
            media_temperaturas = sum(temperaturas_int) / len(temperaturas_int)
            #Test2
            if media_temperaturas:
                print(f"Media de las temperaturas para hoy en Madrid: {media_temperaturas}")
            else:
                print("No hay media de las temperaturas para hoy.")
        else:
            print("Error al realizar la solicitud:", response.status_code)
    except Exception as e:
        print("Error:", e)


# Llamamos a la función para obtener el pronóstico del tiempo de hoy
obtener_tiempo_hoy()
