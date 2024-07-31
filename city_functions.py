import json

def ciudad_pais(ciudad, pais, dpto = ''):
    """Formateo de la ciudad y país"""
    if dpto:
        formateo = f"{ciudad.title()}, {dpto.title()}, {pais.title()}"
        return formateo
    else:
        formateo = f"{ciudad.title()}, {pais.title()}"
        return formateo
    
def cargar_ciudades(ruta):
    """Carga las ciudad guardadas en el archivo json"""
    if ruta.exists():
        contenido = ruta.read_text(encoding='utf-8')
        if contenido.strip(): 
            return json.loads(contenido)
    return []

def guardar_ciudad(ruta, ciudades):
    """Guarda las ciudades en el archivo json"""
    contenido = json.dumps(ciudades, indent=4, ensure_ascii=False)
    ruta.write_text(contenido, encoding='utf-8')
