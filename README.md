Proyecto del Sprint 9: Ejercicio

- Comprobar la funcionalidad de la página web de Urban Rutes mediante diversas pruebas
- Clase: UrbanRoutesPage: contiene localizadores y métodos
- Clase: TestUrbanRoutes: contiene pruebas

Pruebas:

1. Configurar la dirección de partida y llegada
2. Elegir tarifa Comfort
3. Rellenar número de teléfono
4. Agregar tarjeta de crédito

- La función retrieve_phone_code() intercepta el código de confirmación para agregar una tarjeta

5. Escribir un mensaje para el conductor
6. Pedir una manta y pañuelos
7. Pedir dos helados
8. Elegir el modal para buscar un taxi
9. Esperar a que aparezca la información del conductor en el modal (opcional)

## Tecnologías utilizadas

- Python 3
- Selenium WebDriver
- pytest

## Cómo ejecutar las pruebas

```bash
pip install selenium pytest
pytest main.py -v
```