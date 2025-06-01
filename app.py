from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite CORS para todas las rutas y orígenes, para probar local

@app.route('/usuario', methods=['POST'])
def recibir_usuario():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No se recibió JSON en el body'}), 400
    nombre = data.get('nombre')
    email = data.get('email')
    password = data.get('password')
    if not nombre or not email:
        return jsonify({'error': 'Faltan datos de usuario: nombre y email son requeridos'}), 400
    print(f"Datos recibidos - Nombre: {nombre}, Email: {email}, password: {password}")
    return jsonify({'mensaje': f'Usuario recibido: {nombre} con email {email} y su password'}), 200

if __name__ == '__main__':
    app.run(debug=True)

