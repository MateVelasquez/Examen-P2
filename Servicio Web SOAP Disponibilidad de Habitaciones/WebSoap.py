from flask import Flask, request, Response
import xml.etree.ElementTree as ET

app = Flask(__name__)

# Datos en memoria temporal
data = [
    {"room_id": 1, "room_type": "simple", "available_date": "2024-12-16", "status": "disponible"},
    {"room_id": 2, "room_type": "doble", "available_date": "2024-12-16", "status": "disponible"},
    {"room_id": 3, "room_type": "suite", "available_date": "2024-12-16", "status": "disponible"},
    {"room_id": 4, "room_type": "simple", "available_date": "2024-12-17", "status": "disponible"},
    {"room_id": 5, "room_type": "doble", "available_date": "2024-12-17", "status": "reservada"},
    {"room_id": 6, "room_type": "suite", "available_date": "2024-12-17", "status": "disponible"},
    {"room_id": 7, "room_type": "simple", "available_date": "2024-12-18", "status": "en mantenimiento"},
    {"room_id": 8, "room_type": "doble", "available_date": "2024-12-18", "status": "disponible"},
    {"room_id": 9, "room_type": "suite", "available_date": "2024-12-18", "status": "reservada"},
    {"room_id": 10, "room_type": "simple", "available_date": "2024-12-19", "status": "disponible"},
    {"room_id": 11, "room_type": "doble", "available_date": "2024-12-19", "status": "disponible"},
    {"room_id": 12, "room_type": "suite", "available_date": "2024-12-19", "status": "en mantenimiento"},
    {"room_id": 13, "room_type": "simple", "available_date": "2024-12-20", "status": "disponible"},
    {"room_id": 14, "room_type": "doble", "available_date": "2024-12-20", "status": "reservada"},
    {"room_id": 15, "room_type": "suite", "available_date": "2024-12-20", "status": "disponible"},
]


# Helper function para construir la respuesta XML
def build_xml_response(rooms):
    root = ET.Element("Rooms")
    for room in rooms:
        room_element = ET.SubElement(root, "Room")
        for key, value in room.items():
            ET.SubElement(room_element, key).text = str(value)
    return ET.tostring(root, encoding="utf-8", method="xml")

@app.route('/soap/availability', methods=['POST'])
def soap_availability():
    # Parsear la solicitud XML
    try:
        request_data = request.data.decode('utf-8')
        root = ET.fromstring(request_data)
        
        # Extraer los parámetros de la solicitud
        start_date = root.findtext("start_date")
        end_date = root.findtext("end_date")
        room_type = root.findtext("room_type")

        if not start_date or not end_date or not room_type:
            return Response("<Error>Missing parameters</Error>", status=400, mimetype='application/xml')

        # Filtrar las habitaciones según los parámetros
        available_rooms = [
            room for room in data
            if room["room_type"] == room_type and
               room["available_date"] >= start_date and
               room["available_date"] <= end_date and
               room["status"] == "disponible"
        ]

        # Construir y devolver la respuesta XML
        response_xml = build_xml_response(available_rooms)
        return Response(response_xml, status=200, mimetype='application/xml')

    except ET.ParseError:
        return Response("<Error>Invalid XML</Error>", status=400, mimetype='application/xml')

if __name__ == '__main__':
    app.run(debug=True, port=5000)