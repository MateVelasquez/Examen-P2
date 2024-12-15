# Guía para la Ejecución de los Servicios

Esta guía describe cómo ejecutar los tres servicios del sistema de gestión hotelera. Los servicios están desarrollados en Python utilizando Flask y almacenan datos en memoria temporal.

## **Requisitos Previos**
1. **Python instalado:** Asegúrate de tener Python 3.8 o superior instalado en tu máquina. Puedes verificar la versión ejecutando:
   ```bash
   python --version
   ```

2. **Instalar Flask:** Flask es el framework utilizado. Para instalarlo, ejecuta:
   ```bash
   pip install flask
   ```

3. **Herramientas para pruebas:**
   - Postman para pruebas HTTP.
   - `curl` como alternativa en la línea de comandos.

---

## **Servicio Web SOAP: Disponibilidad de Habitaciones**

### Descripción
Este servicio permite consultar la disponibilidad de habitaciones según el tipo y las fechas ingresadas.

### Pasos para Ejecutar
1. Guarda el archivo del servicio como `soap_room_availability.py`.

2. Inicia el servidor ejecutando:
   ```bash
   python soap_room_availability.py
   ```

3. El servidor se ejecutará en `http://127.0.0.1:5000`.

### Endpoints
- **POST /soap/availability**
  - Solicita disponibilidad de habitaciones.
  - Ejemplo de solicitud (en formato XML):
    ```xml
    <Request>
        <start_date>2024-12-20</start_date>
        <end_date>2024-12-25</end_date>
        <room_type>simple</room_type>
    </Request>
    ```

---

## **API REST: Gestión de Reservas**

### Descripción
Este servicio permite realizar, consultar y cancelar reservas de habitaciones.

### Pasos para Ejecutar
1. Guarda el archivo del servicio como `rest_reservation_management.py`.

2. Inicia el servidor ejecutando:
   ```bash
   python rest_reservation_management.py
   ```

3. El servidor se ejecutará en `http://127.0.0.1:5001`.

### Endpoints
- **POST /reservations**
  - Crea una nueva reserva.
  - Ejemplo de solicitud (JSON):
    ```json
    {
        "room_number": 101,
        "customer_name": "John Doe",
        "start_date": "2024-12-20",
        "end_date": "2024-12-25"
    }
    ```

- **GET /reservations/<reservation_id>**
  - Consulta una reserva específica.

- **DELETE /reservations/<reservation_id>**
  - Cancela una reserva.

---

## **Microservicio: Gestión del Inventario**

### Descripción
Este servicio permite registrar nuevas habitaciones y actualizar su estado.

### Pasos para Ejecutar
1. Guarda el archivo del servicio como `microservice_inventory_management.py`.

2. Inicia el servidor ejecutando:
   ```bash
   python microservice_inventory_management.py
   ```

3. El servidor se ejecutará en `http://127.0.0.1:5002`.

### Endpoints
- **POST /rooms**
  - Registra una nueva habitación.
  - Ejemplo de solicitud (JSON):
    ```json
    {
        "room_number": 101,
        "room_type": "simple",
        "status": "disponible"
    }
    ```

- **PATCH /rooms/<room_id>**
  - Actualiza el estado de una habitación.
  - Ejemplo de solicitud (JSON):
    ```json
    {
        "status": "mantenimiento"
    }
    ```

---
