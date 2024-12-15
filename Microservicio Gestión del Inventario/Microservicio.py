from flask import Flask, request, jsonify

app = Flask(__name__)

# Datos en memoria temporal para habitaciones
rooms = []
next_room_id = 1  # Variable global para generar IDs incrementales

# Helper function para encontrar una habitación por ID
def find_room(room_id):
    for room in rooms:
        if room["room_id"] == room_id:
            return room
    return None

# Endpoint para registrar una nueva habitación
@app.route('/rooms', methods=['POST'])
def create_room():
    global next_room_id
    data = request.get_json()

    # Validar los parámetros de entrada
    required_fields = ["room_number", "room_type", "status"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    # Crear la habitación
    room = {
        "room_id": str(next_room_id),  # Generar un ID incremental
        "room_number": data["room_number"],
        "room_type": data["room_type"],
        "status": data["status"]
    }
    rooms.append(room)
    next_room_id += 1  # Incrementar el ID para la próxima habitación

    return jsonify(room), 201

# Endpoint para actualizar el estado de una habitación
@app.route('/rooms/<room_id>', methods=['PATCH'])
def update_room_status(room_id):
    room = find_room(room_id)
    if room is None:
        return jsonify({"error": "Habitacion no encontrada"}), 404

    data = request.get_json()
    if "status" not in data:
        return jsonify({"error": "Missing field: status"}), 400

    # Actualizar el estado de la habitación
    room["status"] = data["status"]
    return jsonify(room), 200

if __name__ == '__main__':
    app.run(debug=True, port=5002)
