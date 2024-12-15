from flask import Flask, request, jsonify

app = Flask(__name__)

# Datos en memoria temporal para reservas
reservations = []
next_id = 1  # Variable global para generar IDs incrementales

# Helper function para encontrar una reserva por ID
def find_reservation(reservation_id):
    for reservation in reservations:
        if reservation["reservation_id"] == reservation_id:
            return reservation
    return None

# Endpoint para crear una nueva reserva
@app.route('/reservations', methods=['POST'])
def create_reservation():
    global next_id
    data = request.get_json()

    # Validar los parámetros de entrada
    required_fields = ["room_number", "customer_name", "start_date", "end_date"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    # Crear la reserva
    reservation = {
        "reservation_id": str(next_id),  # Generar un ID incremental
        "room_number": data["room_number"],
        "customer_name": data["customer_name"],
        "start_date": data["start_date"],
        "end_date": data["end_date"],
        "status": "active"
    }
    reservations.append(reservation)
    next_id += 1  # Incrementar el ID para la próxima reserva

    return jsonify(reservation), 201

# Endpoint para consultar una reserva específica
@app.route('/reservations/<reservation_id>', methods=['GET'])
def get_reservation(reservation_id):
    reservation = find_reservation(reservation_id)
    if reservation is None:
        return jsonify({"error": "Reservación no encontrada"}), 404

    return jsonify(reservation), 200

# Endpoint para cancelar una reserva
@app.route('/reservations/<reservation_id>', methods=['DELETE'])
def cancel_reservation(reservation_id):
    reservation = find_reservation(reservation_id)
    if reservation is None:
        return jsonify({"error": "Reservación no encontrada"}), 404

    reservations.remove(reservation)
    return jsonify({"message": "Reservación cancelada"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)
