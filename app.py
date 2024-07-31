from flask import Flask, render_template, request, redirect, url_for
from pathlib import Path
import city_functions as cf

app = Flask(__name__)
ruta = Path('ciudad.json')

@app.route('/')
def index():
    ciudades = cf.cargar_ciudades(ruta)
    return render_template('index.html', ciudades=ciudades)

@app.route('/add', methods=['GET', 'POST'])
def add_city():
    if request.method == 'POST':
        ciudad = request.form['ciudad'].lower()
        pais = request.form['pais'].lower()
        dpto = request.form.get('dpto', '').lower()

        salida_formato = cf.ciudad_pais(ciudad, pais, dpto)
        ciudades = cf.cargar_ciudades(ruta)
        ciudades.append({'ciudad': ciudad, 'pais': pais, 'dpto': dpto})
        cf.guardar_ciudad(ruta, ciudades)
        return redirect(url_for('index'))
    return render_template('add_city.html')

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_city(index):
    ciudades = cf.cargar_ciudades(ruta)
    ciudad = ciudades[index]

    if request.method == 'POST':
        ciudad['ciudad'] = request.form['ciudad'].lower()
        ciudad['pais'] = request.form['pais'].lower()
        ciudad['dpto'] = request.form.get('dpto', '').lower()
        cf.guardar_ciudad(ruta, ciudades)
        return redirect(url_for('index'))
    
    return render_template('edit_city.html', ciudad=ciudad, index=index)

@app.route('/delete/<int:index>', methods=['POST'])
def delete_city(index):
    ciudades = cf.cargar_ciudades(ruta)
    if 0 <= index < len(ciudades):
        del ciudades[index]
        cf.guardar_ciudad(ruta, ciudades)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)