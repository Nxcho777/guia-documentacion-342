"""Aplicacion Flask de ejemplo para documentacion automatica con Doxygen.

Se usa en la Guia 3.4.2 de Ciberseguridad en desarrollo.
"""

from flask import Flask, request

app = Flask(__name__)


## \brief Devuelve un saludo personalizado.
#  \details Recibe el nombre por el parametro de consulta ``name``.
#  Si no se proporciona, utiliza ``mundo``.
#  \return Mensaje de texto con el saludo.
@app.get('/hello')
def hello():
    """Devuelve un saludo a traves del endpoint /hello."""
    name = (request.args.get('name') or '').strip() or 'mundo'
    return f'Hello, {name}!'


## \brief Comprueba si la aplicacion responde correctamente.
#  \return JSON con estado ``ok``.
@app.get('/health')
def health():
    """Devuelve un estado simple de salud para pruebas y monitoreo."""
    return {'status': 'ok'}


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=5000)
