from flask import Flask

app = Flask(__name__)

# Ruta principal
@app.route('/')
def inicio():
    return '<h1>Bienvenido a mi aplicación web con Flask</h1>'

# Ruta con parámetro
@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f'<h2>¡Hola, {nombre.capitalize()}!</h2>'

# Ejecutar la app
if __name__ == '__main__':
    app.run(debug=True)
