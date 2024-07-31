from city_functions import ciudad_pais, cargar_ciudades, guardar_ciudad
from pathlib import Path

def test_ciudad_pais():
    nombre_formato = ciudad_pais('chota', 'peru', 'cajamarca')
    assert nombre_formato == 'Chota, Cajamarca, Peru'

def test_guardar_y_cargar_ciudades():
    ruta = Path('test_ciudades.json')
    ciudades = [
        {'ciudad': 'chota', 'pais': 'perú', 'dpto': 'cajamarca'},
        {'ciudad': 'lima', 'pais': 'perú', 'dpto': ''}
    ]
    guardar_ciudad(ruta, ciudades)
    ciudades_cargadas = cargar_ciudades(ruta)
    assert ciudades == ciudades_cargadas
    ruta.unlink()