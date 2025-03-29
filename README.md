# Sistema de Clasificación de Imágenes

## Parte 1: Backend con Django (4 puntos)

### Aplicación Catalogo
- Aplicación Django llamada "catalogo" creada
- Configuración básica completada

### Modelo Imagen
- Modelo implementado con los campos:
  - nombre (CharField)
  - tipo_detectado (CharField)
  - descripcion (TextField)
  - archivo (FileField)

### Acceso a Datos
- CRUD habilitado mediante:
  - Interfaz de administración Django
  - API REST básica

### Despliegue
- Configuración lista para:
  - AWS Lightsail

## Parte 2: Función Lambda (4 puntos)

### Entrada de Datos
- Recibe imágenes mediante:
  - Carga directa en base64
  - Trigger desde S3

### Clasificación
- Implementa detección básica de:
  - Documentos
  - Fotos  
  - Facturas
  - Otros tipos

### Salida
- Devuelve objeto con:
  - tipo_detectado (string)
  - descripcion (string)
